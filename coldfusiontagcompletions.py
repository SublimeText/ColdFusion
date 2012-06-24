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

class TagAttributeAutoComplete(sublime_plugin.EventListener):
    cflib = get_class()()
    valid_scopes_tags = ["meta.tag.inline.cf", "meta.tag.block.cf"]

    def on_modified(self, view):
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
        sel = view.sel()[0].a
        completions = []

        if any(s in view.scope_name(sel) for s in self.valid_scopes_tags):
            scopestart = view.extract_scope(sel).a
            if scopestart == sel:
                scopestart = view.extract_scope(sel - 1).a
            word = view.substr(view.word(scopestart + 1))
            if word in self.cflib.completions.keys():
                completions = self.cflib.completions[word]['completions']
        if completions == []:
            return
        return (completions, sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)
