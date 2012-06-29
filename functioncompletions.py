import sublime
import sublime_plugin
import re

completions = []
SETTINGS = sublime.load_settings('ColdFusion.sublime-settings')

def add_methods(cfc_file):
    with open(cfc_file, 'r') as f:
        read_data = f.read()
    methods = []
    method_lines = re.findall('function\s[^{]+', read_data)

    for l in method_lines:
        l = re.sub("[\\n|\s]+"," ",l)
        s = re.search('(\w+)\s?\(.*\)', l)
        if s:
            methods.append(s.group().strip())

    completions.extend(methods)

class MethodsAutoComplete(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        if not view.match_selector(locations[0],
                "source.cfscript.cfc - meta - string - comment"):
            return []

        if not SETTINGS.get("component_method_completions"):
            return

        _completions = []
        add_methods(view.file_name())

        for c in completions:
            snippet = c
            params = re.sub("\w+\(","",snippet,1)[:-1].split(",")

            num = 1
            if len(params[0]):
                for p in params:
                    snippet = snippet.replace(p, '${' + str(num) + ':' + p + '}')
                    num = num + 1
            c = re.sub("\(.*\)","",c)
            _completions.append((c + "\tFunction (component)", snippet))

        del completions[:]
        return _completions
