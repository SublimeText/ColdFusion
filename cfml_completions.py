import sublime, sublime_plugin

# Provide completions that match just after typing an opening angle bracket
class TagCompletions(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        # Only trigger within HTML
        if not view.match_selector(locations[0],
                "text.html.cfm - source"):
            return []

        pt = locations[0] - len(prefix) - 1
        ch = view.substr(sublime.Region(pt, pt + 1))
        if ch != '<':
            return []

        return ([
            ("cfset\tCfml", "cfset $1 />"),
            ("cfdump\tCfml", "cfdump var=\"#${1:selection}#\" >"),

        ], sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)
