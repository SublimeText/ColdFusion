import sublime, sublime_plugin, json
# for sorting COMPLETIONS SCOPES in on_query_completions
from operator import itemgetter
# for accessing cflib.org in CFLIB Command
from urllib.request import urlopen

# load dictionary selectors and completions
try:
    import dictionaries as dic
    from dictionaries.cf10 import *
except:
    import ColdFusion.dictionaries as dic
    from ColdFusion.dictionaries.cf10 import *


# *****************************************************************************************
# COMPLETIONS
# *****************************************************************************************
class ColdFusionAutoComplete(sublime_plugin.EventListener):
    def cfml_all(self, view, prefix, pos):
        # adds opening markup bracket if it isn't found
        lt = '<' if view.substr(pos) != '<' else ''
        return [(v + '\tTag (cmfl)', lt + v) for v in sorted(TAGS.keys())]

    def cfml_tag_attributes(self, view, prefix, pos):
        tag = dic.get_tag_name(view, pos)
        return sorted(TAGS.get(tag, []))

    def cfscript_all(self, view, prefix, pos):
        if view.substr(pos) == ".": # completions for dot variables
            var = view.substr(view.word(pos)).lower()
            return [(v,v) for v in VARIABLES[var]] if var in VARIABLES.keys() else []
        functions = [(v.split('(').pop(0) + '\tfn. (cfscript)', v) for v in FUNCTIONS.keys()]
        # add language variables
        functions.extend([(v + '\tvar (cfscript)',v) for v in VARIABLES.keys()])
        # TODO: add tag operators
        return functions

    def cfscript_variables(self, view, prefix, pos):
        return []
    def cfscript_function_arguments(self, view, prefix, pos):
        return []
    def cfscript_tagoperator_attributes(self, view, prefix, pos):
        return []

    # ****************************************************************
    def on_query_completions(self, view, prefix, locations):
        pos = view.sel()[0].b - 1

        COMPLETIONS = (
            (view.score_selector(pos, dic.CFML_TAG_SCOPE), self.cfml_all),
            (view.score_selector(pos, dic.CFML_TAG_ATTRIBUTE_SCOPE),self.cfml_tag_attributes),
            (view.score_selector(pos, dic.CFSCRIPT_FUNCTION_SCOPE),self.cfscript_all),
            (view.score_selector(pos, dic.CFSCRIPT_FUNCTION_ARGS_SCOPE),self.cfscript_function_arguments),
            (view.score_selector(pos, dic.CFSCRIPT_VARIABLES_SCOPE),self.cfscript_variables),
            (view.score_selector(pos, dic.CFSCRIPT_TAGOPERATOR_ATTRIBUTE_SCOPE),self.cfscript_tagoperator_attributes)
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
