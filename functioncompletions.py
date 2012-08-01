import sublime
import sublime_plugin
import re, os

completions = []
SETTINGS = sublime.load_settings('ColdFusion.sublime-settings')

# props to @boundincode for imoplemntation
def add_methods(cfc_file, hint_text):
    with open(cfc_file, 'r') as f:
        read_data = f.read()
    methods = []
    method_lines = re.findall('function\s[^{]+', read_data)

    for l in method_lines:
        l = re.sub("[\\n|\s]+"," ",l)
        s = re.search('(\w+)\s?\(.*\)', l)
        if s:
            methods.append(s.group().strip())

    for c in methods:
        snippet = c
        params = re.sub("\w+\(","",snippet,1)[:-1].split(",")

        num = 1
        if len(params[0]):
            for p in params:
                snippet = snippet.replace(p, '${' + str(num) + ':' + p + '}')
                num = num + 1
        # removes parens
        c = re.sub("\(.*\)","",c)
        completions.append((c + "\tfn. " + hint_text, snippet))


class MethodsAutoComplete(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        if not view.match_selector(locations[0],
                "source.cfscript.cfc - text - meta - string - comment"):
            return []

        if not SETTINGS.get("component_method_completions"):
            return

        # set local _completions variable
        _completions = []

        # try and find the cfc file and add it's methods
        try:
            cfc_region = view.find_by_selector("meta.component-operator.extends.value.cfscript")[0]
        except IndexError:
            cfc_region = ""

        if len(cfc_region):
            extendspath =  view.substr(cfc_region).replace(".","/")

            # first check the current directory for nested cfc path
            # get the dir this file is in first
            this_file = view.file_name()
            dir_len = this_file.rfind('/') #(for OSX)
            if not dir_len > 0:
                dir_len = this_file.rfind('\\') #(for Windows)
            this_dir = this_file[:(dir_len + 1)] # adds ending '/'

            cfc_file = this_dir + extendspath + ".cfc"
            if not os.path.isfile(cfc_file):
                # check for the cfc in root folders
                for folder in sublime.active_window().folders():
                    if os.path.isfile(folder + "/" + extendspath + ".cfc"):
                        cfc_file = folder + "/" + extendspath + ".cfc"
                        break
            try:
                add_methods(cfc_file, view.substr(cfc_region).split(".")[-1] )
            except UnboundLocalError:
                pass
            except IOError:
                pass

        # add this files methods to autocomplete
        add_methods(view.file_name(), "this")

        # add the completions to the local _completions variable
        _completions.extend(completions)

        # prevents dups
        del completions[:]
        return _completions
