import sublime
import sublime_plugin
class ColdFusionTagComplete(sublime_plugin.EventListener):
    valid_scopes_tags = ["meta.tag.inline.cfml", "meta.tag.block.other.cfml", "meta.tag.block.function.cfml", "meta.tag.block.flow-control.cfml", "meta.tag.block.exceptions.cfml"]


    def on_modified(self, view):
        sel = view.sel()[0].a
        if view.substr(sel - 1) == " ":
            if any(s in view.scope_name(sel) for s in self.valid_scopes_tags):
                sublime.set_timeout(lambda:
                    view.run_command("auto_complete", { 'disable_auto_insert': True, 'next_completion_if_showing': False }), 50
                )


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

    def get_class( kls ):
        parts = kls.split('.')
        module = ".".join(parts[:-1])
        m = __import__( module )
        for comp in parts[1:]:
            m = getattr(m, comp)
        return m

    cflib = get_class('taglib.cf10.tags')()

