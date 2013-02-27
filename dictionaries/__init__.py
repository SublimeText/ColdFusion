import sublime, sublime_plugin, re

def _init():
    global lang

    s = sublime.load_settings('ColdFusion.sublime-settings')
    # need to use __import__ here because it's a dynamic module name
    lang = __import__(s.get('dictionary','cf10'),globals(),locals(),['*'],1)


# load dictionary selectors and completions for ST2
if sublime.version() and int(sublime.version()) < 3000:
    _init()

# load dictionary selectors and completions for ST3
def plugin_loaded():
    sublime.set_timeout_async(_init)

# scopes in which to trigger cfml tags auto complete
CFML_TAG_SCOPE = 'text.html.cfm -source -meta -comment, text.html.cfm source.js -meta -comment, meta.scope.between-output-tags.cfml -comment, text.html.cfm.embedded -source.cfscript.embedded -meta -comment'
# scopes in which to trigger cfml tag attributes auto complete
CFML_TAG_ATTRIBUTE_SCOPE = 'meta.tag.inline.cf -string, meta.tag.block.cf -string'
# scopes in which to trigger cfscript functions auto complete
CFSCRIPT_FUNCTION_SCOPE = 'source.cfscript -meta.function -meta.function-call -variable.other.dot -variable.other.local -string -comment'
# scopes in which to trigger function call parameters auto complete
CFSCRIPT_FUNCTION_ARGS_SCOPE = 'meta.function-call.cfscript -string -comment'
# scopes in which to trigger tag operator arguments
CFSCRIPT_TAGOPERATOR_ATTRIBUTE_SCOPE = 'meta.operator -string -comment'
# scopes in which to trigger variable completions
CFSCRIPT_VARIABLES_SCOPE = 'variable.other.dot.cfscript'
# scopes that trigger auto complete on spacebar key press // meta.tag.inline.cf.other excludes cfset/cfreturn
AC_ON_SPACE_SCOPE = 'meta.function-call.cfscript -meta.tag.inline.cf.other, meta.tag -meta.tag.inline.cf.other, meta.operator'
# scopes that trigger on dot auto completions
AC_ON_DOT_SCOPE = 'source.cfscript'

def get_tag_name(view, pos):
    return _get_tag_info(view, pos).pop(0)

def get_tag_attribs(view, pos):
    return _get_tag_info(view, pos)[:-1]

def get_tagoperator_name(view, pos):
    return _get_tag_operator_info(view, pos).pop(0)

def get_function_completions_from_file(cfc_file, hint_text):
    completions = []
    methods = []

    with open(cfc_file, 'r') as f:
        read_data = f.read()

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
        if params[0]:
            for p in params:
                snippet = snippet.replace(p, '${' + str(num) + ':' + p + '}')
                num = num + 1
        # removes parens
        c = re.sub("\(.*\)","",c)
        completions.append((c + "\tfn. " + hint_text, snippet))
    return completions


# *****************************************************************************************
# HELPERS
# *****************************************************************************************
def _get_tag_info(view, pos):
    taginfo = view.substr(sublime.Region(0, pos)).split("<").pop()
    return re.split('\s|\t|\n',taginfo)

def _get_tag_operator_info(view, pos):
    return list(filter(None, re.split('\t|\s',view.substr(view.line(pos)))))

