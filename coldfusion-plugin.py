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
            self.view.insert(edit, region.b, ">")

        # return if disabled in ColdFusion.sublime-settings file
        if not s.get("auto_close_cfml"):
            return None

        # prevents triggering inside strings and other scopes that are not block tags
        # this should be taken care of in keybindings, but it's not working for cfcomponent
        # TODO ST3: use scope_selector or clean this out it may work through keybindings now

        # cursor position
        # pos = self.view.sel()[0].b
        # if self.view.match_selector(pos, "string") \
        #     or self.view.match_selector(pos, "source.cfscript.embedded.cfml") \
        #     or not self.view.match_selector(pos, "meta.tag.block.cf"):
        #     return

        if self.view.match_selector(region.b - 1,"meta.tag.block.cf")  \
            and not self.view.substr(region.b - 2) == "/": # don't close an already closed tag


            for temp in self.view.sel():
                tag_name = dic.get_tag_name(self.view, temp.b)
                indent = not s.get("auto_indent_on_close") or tag_name == "cfoutput"
                if not indent:
                    self.view.insert(edit,temp.b,"\n\t\n</" + tag_name + ">")
                else:
                    self.view.insert(edit, temp.b, "</" + tag_name + ">")

            self.view.run_command("move", {"by": "lines", "forward": False})

        # if not s.get("auto_indent_on_close") or tag_name == "cfoutput":
            # self.view.run_command("insert_snippet", {"contents": "$0</" + tag_name + ">"})
        # else:
            # self.view.run_command("insert_snippet", {"contents": "\n\t$0\n</" + get_current_name() + ">"})

        return None

# *****************************************************************************************
# DEFAULT.SUBLIME-COMMANDS
# *****************************************************************************************
class ShowCflibCommand(sublime_plugin.WindowCommand):
    cflib_category_url = r"http://www.cflib.org/api/api.cfc?method=getlibraries&returnformat=json"
    cflib_udfs_url = r"http://www.cflib.org/api/api.cfc?method=getudfs&returnformat=json&libraryid="
    cflib_udf_url = r"http://www.cflib.org/api/api.cfc?method=getudf&returnFormat=json&udfid="
    libIndex = -1

    def run(self):
        global libs, udfs
        if not 'libs' in globals():
            libs = self.fetch_json(self.cflib_category_url)['DATA']
            udfs = {}
        sublime.set_timeout(lambda:self.window.show_quick_panel([[v] for k, v in (libs)], self.on_select_library), 10)

    def on_select_library(self, index):
        self.libIndex = index
        if index == -1:
            return
        if not index in udfs:
            udfs[index] = self.fetch_json(self.cflib_udfs_url + str(libs[index][0]))['DATA']
        sublime.set_timeout(lambda:self.window.show_quick_panel([[v.strip(), c.strip()] for k, v, c in udfs[index]], self.on_select_udf), 10)

    def on_select_udf(self, index):
        if index == -1:
            self.run()
        else:
            code = str(self.fetch_json(self.cflib_udf_url + str(udfs[self.libIndex][index][0]))['CODE'])
            self.window.active_view().run_command("insert_udf", {"code":code})

    def fetch_json(self,url):
        req = urlopen(url)
        return json.loads(req.read().decode('UTF-8'))

class InsertUdfCommand(sublime_plugin.TextCommand):
    def run(self, edit, code):
        for region in self.view.sel():
            self.view.replace(edit, region, code.replace("\r",""))


# *****************************************************************************************
# FUNCTION AUTO-FOLD COMMANDS
# *****************************************************************************************
class FoldCffunctionsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        contentRegions = self.findCffunctionContent()
        contentRegions += self.findScriptFunctionContent()

        # if the regions are already folded, unfold them
        if self.view.fold(contentRegions) == False:
            self.view.unfold(contentRegions)

    # Find the CFFunction regions to fold
    def findCffunctionContent(self):
        contentRegions = []

        try:
            cffunctionOpens = self.view.find_all('<cffunction.*?name=".*?".*?>')
            cffunctionEnds = self.view.find_all('</cffunction>')
            functionCnt = len(cffunctionOpens)
            i = 0
            n = 0

            # Loop through opening & ending regions...create a new region containing the function content
            while i < functionCnt:
                nextElem = i + 1

                if cffunctionOpens[i].end() > cffunctionEnds[n].end():
                    # function ending doesn't match up with function start (have an orphaned function close, skip the end tag)
                    i -= 1
                elif (nextElem < functionCnt and cffunctionOpens[nextElem].end() > cffunctionEnds[n].end()) or nextElem == functionCnt:
                    # Create new region from end of function start tag to the end of the function close tag
                    contentRegions.append(sublime.Region(cffunctionOpens[i].end(),cffunctionEnds[n].end()))
                else:
                    # function start doesn't match up with function end (missing closing function tag for this one, skip the open tag)
                    n -= 1

                i += 1
                n += 1
        except:
            print ("Fold Functions Plugin: Unexpected error when trying to find CFFUNCTIONS.")

        return contentRegions

    # Find the script function regions to fold
    def findScriptFunctionContent(self):
        contentRegions = []

        try:
            scriptFuncOpens = self.view.find_all('function.*?\{')

            for func in scriptFuncOpens:
                startPosition = func.end()

                closingBracket = self.findClosingBracket(startPosition)

                if closingBracket != None:
                    contentRegions.append(sublime.Region(startPosition,closingBracket))
        except:
            print ("Fold Functions Plugin: Unexpected error when trying to find CFSCRIPT functions.")

        return contentRegions

    # Find the closing bracket for a script function
    def findClosingBracket(self, startPosition):
        openBlocks = 1

        try:
            # Loop through & track all opening/closing brackets (that come after our initial function opener) until
            # we find a closing bracket to match our origiinal opening bracket or we run out of brackets to check
            while openBlocks > 0:
                bracketRegion = self.view.find("\{|\}", startPosition)
                bracket = self.view.substr(bracketRegion)

                if(bracket != None):
                    if bracket == "{":
                        openBlocks += 1
                    else:
                        openBlocks -= 1

                    startPosition = bracketRegion.end()
                else:
                    # Ran out of brackets to check, get us out the loop
                    openBlocks = -1

            if openBlocks == 0:
                return bracketRegion.end()
        except:
            print ("Fold Functions Plugin: Unexpected error when trying to find a closing bracket for CFSCRIPT function.")

        return None
