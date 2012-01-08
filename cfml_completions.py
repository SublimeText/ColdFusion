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
            ("cfabort\tCfml", "cfabort ${1:${2:showerror=\"$3\"}} />"),
            ("cfapplet\tCfml", "cfapplet ${1:${2:appletsource=\"$3\" }${4:name=\"$5\" }${6:height=\"$7\" }${8:width=\"$9\" }${10:vspace=\"$11\" }${12:hspace=\"$13\" }${14:align=\"$15\" }${16:notsupported=\"$17\"}} />"),
            ("cfapplication\tCfml", "cfapplication ${1:${2:name=\"$3\" }${4:loginstorage=\"$5\" }${6:clientmanagement=\"$7\" }${8:clientstorage=\"$9\" }${10:setclientcookies=\"$11\" }${12:sessionmanagement=\"$13\" }${14:sessiontimeout=\"$15\" }${16:applicationtimeout=\"$17\" }${18:setdomaincookies=\"$19\" }${20:scriptprotect=\"$21\"}} />"),
            ("cfargument\tCfml", "cfargument ${1:${2:name=\"$3\" }${4:type=\"$5\" }${6:required=\"$7\" }${8:default=\"$9\" }${10:displayname=\"$11\" }${12:hint=\"$13\"}} />"),
            ("cfassociate\tCfml", "cfassociate ${1:${2:basetag=\"$3\" }${4:datacollection=\"$5\"}} />"),
            ("cfbreak\tCfml", "cfbreak ${1:} />"),
            ("cfcache\tCfml", "cfcache ${1:${2:action=\"$3\" }${4:directory=\"$5\" }${6:timespan=\"$7\" }${8:expireurl=\"$9\" }${10:username=\"$11\" }${12:password=\"$13\" }${14:port=\"$15\" }${16:protocol=\"$17\"}} />"),
            ("cfcalendar\tCfml", "cfcalendar ${1:${2:name=\"$3\" }${4:height=\"$5\" }${6:width=\"$7\" }${8:selecteddate=\"$9\" }${10:startrange=\"$11\" }${12:endrange=\"$13\" }${14:disabled=\"$15\" }${16:mask=\"$17\" }${18:firstdayofweek=\"$19\" }${20:daynames=\"$21\" }${22:monthnames=\"$23\" }${24:style=\"$25\" }${26:onchange=\"$27\"}} />"),
            ("cfcase\tCfml", "cfcase ${1:${2:value=\"$3\" }${4:delimiters=\"$5\"}}>\n\t$0\n</cfcase>"),
            ("cfcatch\tCfml", "cfcatch ${1:${2:type=\"$3\"}}>\n\t$0\n</cfcatch>"),
            ("cfchart\tCfml", "cfchart ${1:${2:format=\"$3\" }${4:chartheight=\"$5\" }${6:chartwidth=\"$7\" }${8:scalefrom=\"$9\" }${10:scaleto=\"$11\" }${12:showxgridlines=\"$13\" }${14:showygridlines=\"$15\" }${16:gridlines=\"$17\" }${18:seriesplacement=\"$19\" }${20:foregroundcolor=\"$21\" }${22:backgroundcolor=\"$23\" }${24:databackgroundcolor=\"$25\" }${26:showborder=\"$27\" }${28:font=\"$29\" }${30:fontsize=\"$31\" }${32:fontitalic=\"$33\" }${34:fontbold=\"$35\" }${36:labelformat=\"$37\" }${38:xaxistitle=\"$39\" }${40:yaxistitle=\"$41\" }${42:xaxistype=\"$43\" }${44:yaxistype=\"$45\" }${46:sortxaxis=\"$47\" }${48:show3d=\"$49\" }${50:xoffset=\"$51\" }${52:yoffset=\"$53\" }${54:rotated=\"$55\" }${56:showlegend=\"$57\" }${58:tipstyle=\"$59\" }${60:tipbgcolor=\"$61\" }${62:showmarkers=\"$63\" }${64:markersize=\"$65\" }${66:pieslicestyle=\"$67\" }${68:url=\"$69\" }${70:name=\"$71\" }${72:style=\"$73\" }${74:title=\"$75\"}}>\n\t$0\n</cfchart>"),
            ("cfchartdata\tCfml", "cfchartdata ${1:${2:item=\"$3\" }${4:value=\"$5\"}} />"),
            ("cfchartseries\tCfml", "cfchartseries ${1:${2:type=\"$3\" }${4:query=\"$5\" }${6:itemcolumn=\"$7\" }${8:valuecolumn=\"$9\" }${10:serieslabel=\"$11\" }${12:seriescolor=\"$13\" }${14:paintstyle=\"$15\" }${16:markerstyle=\"$17\" }${18:colorlist=\"$19\" }${20:datalabelstyle=\"$21\"}}>\n\t\$0\n</cfchartseries>"),
            ("cfcol\tCfml", "cfcol ${1:${2:header=\"$3\" }${4:width=\"$5\" }${6:align=\"$7\" }${8:text=\"$9\"}} />"),




            ("cfset\tCfml", "cfset $1 />"),
            ("cfdump\tCfml", "cfdump var=\"#${1:selection}#\" >"),

        ], sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)
