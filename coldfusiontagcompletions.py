import sublime
import sublime_plugin

SETTINGS = sublime.load_settings('ColdFusion.sublime-settings')
SUBLIME_SETTINGS = sublime.load_settings('Preferences.sublime-settings')

def get_class():
    kls = "taglib." + SETTINGS.get("dictionary") + ".tags"
    parts = kls.split('.')
    module = ".".join(parts[:-1])
    m = __import__( module )
    for comp in parts[1:]:
        m = getattr(m, comp)
    return m

class CloseCftagCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        sel = self.view.sel()[0]

        # insert the actual &gt; character
        for region in self.view.sel():
            self.view.insert(edit, region.end(), ">")

        # prevents auto_complete pop up from triggering
        self.view.run_command("hide_auto_complete")

        # return if disabled in settings file
        if not SETTINGS.get("auto_close_cfml"):
            return

        # prevents triggering inside strings and other scopes that are not block tags
        # this should be taken care of in keybindings, but it's not working for cfcomponent
        if self.view.match_selector(sel.end(), "string") \
            or self.view.match_selector(sel.end(), "source.cfscript.embedded.cfml") \
            or not self.view.match_selector(sel.end(), "meta.tag.block.cf"):
            return

        for region in self.view.sel():
            pos = region.begin()

            tagdata = self.view.substr(sublime.Region(0, pos)).split("<")
            tagdata.reverse()
            tagdata = tagdata.pop(0).split(" ")
            tagname = tagdata[0]

        if self.view.match_selector(sel.end(),"meta.tag.block.cf")  \
            and not self.view.substr(sel.end() - 1) == "/" \
            and not tagname[0] == "/":

            if not tagname[-1] == ">":
                tagname = tagname + ">"
            if not SETTINGS.get("auto_indent_on_close") or tagname == "cfoutput>":
                self.view.run_command("insert_snippet", {"contents": "$0</" + tagname})
            else:
                self.view.run_command("insert_snippet", {"contents": "\n\t$0\n</" + tagname})

class TagAutoComplete(sublime_plugin.EventListener):
    cflib = get_class()()

    def on_query_completions(self, view, prefix, locations):
        completions = []
        if not view.match_selector(locations[0],
                "meta.scope.between-output-tags.cfml - meta.tag - comment - string, \
                text.html.cfm - meta - source - comment - string, \
                text.html.cfm.embedded.cfml - meta - source.cfscript.embedded.cfml - comment - string, \
                punctuation.definition.tag.cf.begin, \
                source.sql.embedded.cfml - string - comment - meta.name.interpolated.hash"):
            return
        if SETTINGS.get("verbose_tag_completions"):
            return

        sel = view.sel()[0]
        if view.substr(sel.begin() - 1) == ".":
            return []

        pt = locations[0] - len(prefix) - 1
        # view.match_selector being bonky so we're going nuclear here
        if any(s in view.scope_name(pt) for s in ["meta.tag.block.cf","meta.tag.inline.cf","string","comment"]):
            return

        for s in self.cflib.completions.keys():
            completions.extend([(s + "\tTag (cmfl)",s)])

        # if the less than opening tag is missing lets add it
        if view.substr(pt) != '<':
            completions = [(list(item)[-2],"<" + list(item)[1]) for item in completions]

        return sorted(completions)

class TagAttributeAutoComplete(sublime_plugin.EventListener):
    cflib = get_class()()
    valid_scopes_tags = ["meta.tag"]

    def on_modified(self, view):
        if SETTINGS.get("verbose_tag_completions"):
            return
        if not SUBLIME_SETTINGS.get("auto_complete"):
            return
        sel = view.sel()[0].a

        # we're starting a new tag don't trigger auto_complete
        if "punctuation.definition.tag.cf.begin" in view.scope_name(sel):
            return

        if view.substr(sel - 1) == " ":
            if any(s in view.scope_name(sel) for s in self.valid_scopes_tags):
                t = view.settings().get("auto_complete_delay")
                sublime.set_timeout(lambda:
                    view.run_command("auto_complete", {
                                            'disable_auto_insert': True,
                                            'next_completion_if_showing': False,
                                            'api_completions_only': True}), t)


    def on_query_completions(self, view, prefix, locations):
        sel = view.sel()[0].a
        completions = []

        # Do not trigger if we are in a string or comment
        pt = locations[0] - len(prefix) - 1
        if any(s in view.scope_name(pt) for s in ["string","comment"]):
            return

        if any(s in view.scope_name(sel) for s in self.valid_scopes_tags):
            for region in view.sel():
                pos = region.begin()

                tagdata = view.substr(sublime.Region(0, pos)).split("<")
                tagdata.reverse()
                tagdata = tagdata.pop(0).split(" ")
                tagname = tagdata[0]

            if tagname in self.cflib.completions.keys():
                completions = self.cflib.completions[tagname]['completions']

        if completions == []:
            return
        return (completions, sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)
