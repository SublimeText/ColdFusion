import sublime
import sublime_plugin

SETTINGS = sublime.load_settings('ColdFusion.sublime-settings')

def get_class():
    kls = "taglib." + SETTINGS.get("dictionary") + ".tags"
    parts = kls.split('.')
    module = ".".join(parts[:-1])
    m = __import__( module )
    for comp in parts[1:]:
        m = getattr(m, comp)
    return m

class TagAutoComplete(sublime_plugin.EventListener):
    cflib = get_class()()

    def on_query_completions(self, view, prefix, locations):
        completions = []
        if not view.match_selector(locations[0],
                "text.html.cfm - source - meta, text.html.cfm.embedded.cfml - source.cfscript.embedded.cfml - source.sql.embedded.cfml"):
            return
        s = sublime.load_settings('ColdFusion.sublime-settings')
        if s.get("verbose_tag_completions"):
             return

        # Do not trigger if we are in a tag or string or comment
        pt = locations[0] - len(prefix) - 1
        if any(s in view.scope_name(pt) for s in ["tag","string","comment"]):
            return

        for s in self.cflib.completions.keys():
            completions.extend([(s + "\t(cmfl) Tag",s)])

        # if the less than opening tag is missing lets add it
        if view.substr(pt) != '<':
            completions = [(list(item)[-2],"<" + list(item)[1]) for item in completions]

        return sorted(completions)

class TagAttributeAutoComplete(sublime_plugin.EventListener):
    cflib = get_class()()
    valid_scopes_tags = ["meta.tag.inline.cf", "meta.tag.block.cf"]

    def on_modified(self, view):
        s = sublime.load_settings('ColdFusion.sublime-settings')
        if s.get("verbose_tag_completions"):
             return
        sel = view.sel()[0].a

        if view.substr(sel - 1) == " ":
            if any(s in view.scope_name(sel) for s in self.valid_scopes_tags):
                t = view.settings().get("auto_complete_delay")
                sublime.set_timeout(lambda:
                    view.run_command("auto_complete", {
                                            'disable_auto_insert': True,
                                            'next_completion_if_showing': False,
                                            'api_completions_only': True}), t)


    def on_query_completions(self, view, prefix, locations):
        s = sublime.load_settings('ColdFusion.sublime-settings')
        if s.get("verbose_tag_completions"):
             return
        sel = view.sel()[0].a
        completions = []

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
