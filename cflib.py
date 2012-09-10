import sublime, sublime_plugin, json
from urllib import urlopen

CFLIBCATS = r"http://www.cflib.org/api/api.cfc?method=getlibraries&returnformat=json"
CFLIBUDFS = r"http://www.cflib.org/api/api.cfc?method=getudfs&returnformat=json&libraryid="
CFLIBUDF = r"http://www.cflib.org/api/api.cfc?method=getudf&returnFormat=json&udfid="

class ShowCflibCommand(sublime_plugin.WindowCommand):
    categories = []
    udfs = []
    def __init__(self, *args, **kwargs):
        super(ShowCflibCommand, self).__init__(*args, **kwargs)
        categories = []
        udfs = []
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
