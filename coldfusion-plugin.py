import sublime, sublime_plugin, json, os
# for sorting COMPLETIONS SCOPES in on_query_completions
from operator import itemgetter

# try imports due to ST2/ST3 compatability
try:
    import ColdFusion.dictionaries as dic
    from urllib.request import urlopen
except ImportError:
    import dictionaries as dic
    from urllib import urlopen

# *****************************************************************************************
# COMPLETIONS
# *****************************************************************************************
class ColdFusionAutoComplete(sublime_plugin.EventListener):
    def on_cfml_all(self, view, prefix, pos):
        # adds opening markup bracket if it isn't found
        lt = '<' if view.substr(pos) != '<' else ''
        return [(v + '\tTag (cmfl)', lt + v) for v in sorted(dic.lang.TAGS.keys())]

    def on_cfml_tag_attributes(self, view, prefix, pos):
        tag = dic.get_tag_name(view, pos)
        return sorted(dic.lang.TAGS.get(tag, []))

    def on_cfscript_all(self, view, prefix, pos):
        if view.substr(pos) == ".": # completions for dot variables
            var = view.substr(view.word(pos)).lower()
            return [(v,v) for v in dic.lang.VARIABLES[var]] if var in dic.lang.VARIABLES.keys() else []
        functions = [(v.split('(').pop(0) + '\tfn. (cfscript)', v) for v in dic.lang.FUNCTIONS.keys()]
        # add language variables
        functions.extend([(v + '\tvar (cfscript)',v) for v in dic.lang.VARIABLES.keys()])

        # add the current view's cfscript methods
        functions.extend(dic.get_function_completions_from_file(view.file_name(), "this"))

        # lets try and grab cfscript methods from the inherited cfc
        try:
            extends_value = view.find_by_selector("meta.component-operator.extends.value.cfscript").pop(0)
        except IndexError:
            extends_value = None

        if extends_value:
            extends_path = view.substr(extends_value).replace('.','/')

            # get base path of project
            this_file = view.file_name()
            dir_len = this_file.rfind('/') #(for OSX)
            if not dir_len > 0:
                dir_len = this_file.rfind('\\') #(for Windows)
            this_dir = this_file[:(dir_len + 1)] # adds ending '/'

            cfc_file = this_dir + extends_path + ".cfc"
            # check the cfc_file exists else look for it in project folders
            if not os.path.isfile(cfc_file):
                # check for the cfc in root folders
                for folder in sublime.active_window().folders():
                    if os.path.isfile(folder + "/" + extends_path + ".cfc"):
                        cfc_file = folder + "/" + extends_path + ".cfc"
                        break
            try:
                functions.extend(dic.get_function_completions_from_file(cfc_file, view.substr(extends_value).split(".").pop(0)))
            except (UnboundLocalError, IOError):
                pass
        # TODO: add tag operators
        return functions

    def on_cfscript_variables(self, view, prefix, pos):
        return []
    def on_cfscript_function_arguments(self, view, prefix, pos):
        return []
    def on_cfscript_tagoperator_attributes(self, view, prefix, pos):
        return []

    # ****************************************************************
    def on_query_completions(self, view, prefix, locations):
        pos = view.sel()[0].b - 1

        COMPLETIONS = (
            (view.score_selector(pos, dic.CFML_TAG_SCOPE), self.on_cfml_all),
            (view.score_selector(pos, dic.CFML_TAG_ATTRIBUTE_SCOPE),self.on_cfml_tag_attributes),
            (view.score_selector(pos, dic.CFSCRIPT_FUNCTION_SCOPE),self.on_cfscript_all),
            (view.score_selector(pos, dic.CFSCRIPT_FUNCTION_ARGS_SCOPE),self.on_cfscript_function_arguments),
            (view.score_selector(pos, dic.CFSCRIPT_VARIABLES_SCOPE),self.on_cfscript_variables),
            (view.score_selector(pos, dic.CFSCRIPT_TAGOPERATOR_ATTRIBUTE_SCOPE),self.on_cfscript_tagoperator_attributes)
        )

        for score, completions in sorted(COMPLETIONS,key=itemgetter(0),reverse=True):
            if score: return completions(view, prefix, pos)

    def on_modified(self, view):
        if not view.settings().get("auto_complete"):
            return None
        pos = view.sel()[0].b - 1

        # triggers auto complete using just the space bar or the dot character
        if view.score_selector(pos, dic.AC_ON_DOT_SCOPE) and view.substr(pos) == "." or \
            view.score_selector(pos, dic.AC_ON_SPACE_SCOPE) and view.substr(pos) == " ":

            t = view.settings().get("auto_complete_delay")
            sublime.set_timeout(lambda:
            view.run_command("auto_complete", {
                                    'disable_auto_insert': True,
                                    'next_completion_if_showing': False,
                                    'api_completions_only': True}), t)

# *****************************************************************************************
# KEYBINDING TEXT COMMANDS
# *****************************************************************************************
class CloseCftagCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        s = sublime.load_settings('ColdFusion.sublime-settings')
        # current carat position
        pos = self.view.sel()[0].end()

        # insert the "&gt;" char
        for region in self.view.sel():
            self.view.insert(edit, region.end(), ">")

        # return if disabled in ColdFusion.sublime-settings file
        if not s.get("auto_close_cfml"):
            return None

        # prevents triggering inside strings and other scopes that are not block tags
        # this should be taken care of in keybindings, but it's not working for cfcomponent
        # TODO ST3: use scope_selector or clean this out it may work through keybindings now
        if self.view.match_selector(pos, "string") \
            or self.view.match_selector(pos, "source.cfscript.embedded.cfml") \
            or not self.view.match_selector(pos, "meta.tag.block.cf"):
            return

        # only close tag if it's a block tag
        if self.view.match_selector(pos,"meta.tag.block.cf")  \
            and not self.view.substr(pos - 1) == "/": # don't close an already closed tag

            tagname = dic.get_tag_name(self.view, pos) + ">"

            if not s.get("auto_indent_on_close") or tagname == "cfoutput>":
                self.view.run_command("insert_snippet", {"contents": "$0</" + tagname})
            else:
                self.view.run_command("insert_snippet", {"contents": "\n\t$0\n</" + tagname})
        return None

# *****************************************************************************************
# DEFAULT.SUBLIME-COMMANDS
# *****************************************************************************************
class ShowCflibCommand(sublime_plugin.WindowCommand):

    CFLIBCATS = r"http://www.cflib.org/api/api.cfc?method=getlibraries&returnformat=json"
    CFLIBUDFS = r"http://www.cflib.org/api/api.cfc?method=getudfs&returnformat=json&libraryid="
    CFLIBUDF = r"http://www.cflib.org/api/api.cfc?method=getudf&returnFormat=json&udfid="

    def run(self):
        self.getCategories()
        self.window.show_quick_panel([[v] for k, v in (self.categories)], self.on_select_categories)

    def getCategories(self):
        d = json.load(urlopen(CFLIBCATS))
        self.categories = d['DATA']

    def getUdfs(self,index):
        d = json.load(urlopen(CFLIBUDFS + str(self.categories[index][0])))
        self.udfs = d['DATA']

    def on_select_categories(self, index):
        if index == -1:
            return
        self.getUdfs(index)
        self.window.show_quick_panel([[v.strip(), c.strip()] for k, v, c in self.udfs], self.on_select_udf)

    def on_select_udf(self, index):
        if index == -1:
            self.run()
        else:
            d = json.load(urlopen(CFLIBUDF + str(self.udfs[index][0])))
            self.window.active_view().run_command("insert_udf", {"code":str(d['CODE'])})

class InsertUdfCommand(sublime_plugin.TextCommand):
    def run(self, edit, code):
        for region in self.view.sel():
            self.view.replace(edit, region, code)
