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
            ("cfcollection\tCfml", "cfcollection ${1:${2:action=\"$3\" }${4:collection=\"$5\" }${6:path=\"$7\" }${8:language=\"$9\" }${10:name=\"$11\" }${12:categories=\"$13\"}} />"),
            ("cfcomponent\tCfml", "cfcomponent ${1:${2:extends=\"$3\" }${4:output=\"$5\" }${6:displayname=\"$7\" }${8:hint=\"$9\" }${10:name=\"$11\" }${12:style=\"$13\" }${14:namespace=\"$15\" }${16:serviceportname=\"$17\" }${18:porttypename=\"$19\" }${20:bindingname=\"$21\" }${22:wsdlfile=\"$23\"}}>\n\t$0\n</cfcomponent>"),
            ("cfcontent\tCfml", "cfcontent ${1:${2:type=\"$3\" }${4:deletefile=\"$5\" }${6:file=\"$7\" }${8:reset=\"$9\"}} />"),
            ("cfcookie\tCfml", "cfcookie ${1:${2:name=\"$3\" }${4:value=\"$5\" }${6:expires=\"$7\" }${8:secure=\"$9\" }${10:path=\"$11\" }${12:domain=\"$13\"}} />"),
            ("cfdefaultcase\tCfml", "cfdefaultcase>\n\t$0\n</cfdefaultcase>"),
            ("cfdirectory\tCfml", "cfdirectory ${1:${2:action=\"$3\" }${4:directory=\"$5\" }${6:name=\"$7\" }${8:filter=\"$9\" }${10:mode=\"$11\" }${12:sort=\"$13\" }${14:newdirectory=\"$15\" }${16:recurse=\"$17\"}} />"),
            ("cfdocument\tCfml", "cfdocument ${1:${2:format=\"$3\" }${4:filename=\"$5\" }${6:overwrite=\"$7\" }${8:name=\"$9\" }${10:pagetype=\"$11\" }${12:pageheight=\"$13\" }${14:pagewidth=\"$15\" }${16:orientation=\"$17\" }${18:margintop=\"$19\" }${20:marginbottom=\"$21\" }${22:marginleft=\"$23\" }${24:marginright=\"$25\" }${26:unit=\"$27\" }${28:encryption=\"$29\" }${30:ownerpassword=\"$31\" }${32:userpassword=\"$33\" }${34:permissions=\"$35\" }${36:fontembed=\"$37\" }${38:backgroundvisible=\"$39\" }${40:scale=\"$41\"}}>\n\t$0\n</cfdocument>"),
            ("cfdocumentitem\tCfml", "cfdocumentitem ${1:${2:type=\"$3\"}}>\n\t$0\n</cfdocumentitem>"),
            ("cfdocumentsection\tCfml", "cfdocumentsection ${1:${2:margintop=\"$3\" }${4:marginbottom=\"$5\" }${6:marginleft=\"$7\" }${8:marginright=\"$9\"}}>\n\t$0\n<cfdocumentsection>"),
            ("cfdump\tCfml", "cfdump ${1:${2:var=\"$3\" }${4:expand=\"$5\" }${6:label=\"$7\"}} />"),
            ("cfelse\tCfml", "cfelse>"),
            ("cfelseif\tCfml", "cfelseif ${1:} />"),
            ("cferror\tCfml", "cferror ${1:${2:type=\"$3\" }${4:template=\"$5\" }${6:mailto=\"$7\" }${8:exception=\"$9\"}} />"),
            ("cfexecute\tCfml", "cfexecute ${1:${2:name=\"$3\" }${4:arguments=\"$5\" }${6:outputfile=\"$7\" }${8:variable=\"$9\" }${10:timeout=\"$11\"}}>\n\t$0\n</cfexecute>"),
            ("cfexit\tCfml", "cfexit ${1:${2:method=\"$3\"}} />"),
            ("cfexit\tCfml", "cfexit ${1:${2:method=\"$3\"}} />"),
            ("cffile\tCfml", "cffile ${1:${2:action=\"$3\" }${4:file=\"$5\" }${6:mode=\"$7\" }${8:output=\"$9\" }${10:addnewline=\"$11\" }${12:attributes=\"$13\" }${14:charset=\"$15\" }${16:source=\"$17\" }${18:destination=\"$19\" }${20:variable=\"$21\" }${22:filefield=\"$23\" }${24:nameconflict=\"$25\" }${26:accept=\"$27\" }${28:result=\"$29\"}} />"),
            ("cfflush\tCfml", "cfflush ${1:${2:interval=\"$3\"}} />"),
            ("cfform\tCfml", "cfform ${1:${2:name=\"$3\" }${4:action=\"$5\" }${6:method=\"$7\" }${8:format=\"$9\" }${10:skin=\"$11\" }${12:style=\"$13\" }${14:preservedata=\"$15\" }${16:onload=\"$17\" }${18:onreset=\"$19\" }${20:onsubmit=\"$21\" }${22:codebase=\"$23\" }${24:archive=\"$25\" }${26:height=\"$27\" }${28:width=\"$29\" }${30:onerror=\"$31\" }${32:wmode=\"$33\" }${34:accessible=\"$35\" }${36:preloader=\"$37\" }${38:timeout=\"$39\" }${40:enctype=\"$41\" }${42:id=\"$43\" }${44:scriptsrc=\"$45\" }${46:target=\"$47\" }${48:class=\"$49\" }${50:passthrough=\"$51\"}}>\n\t$0\n</cfform>"),
            ("cfformgroup\tCfml", "cfformgroup ${1:${2:type=\"$3\" }${4:query=\"$5\" }${6:startrow=\"$7\" }${8:maxrows=\"$9\" }${10:label=\"$11\" }${12:style=\"$13\" }${14:selectedindex=\"$15\" }${16:width=\"$17\" }${18:height=\"$19\" }${20:enabled=\"$21\" }${22:visible=\"$23\" }${24:onchange=\"$25\" }${26:tooltip=\"$27\"}}>\n\t$0\n</cfformgroup>"),
            ("cfformitem\tCfml", "cfformitem ${1:${2:type=\"$3\" }${4:style=\"$5\" }${6:width=\"$7\" }${8:height=\"$9\" }${10:enabled=\"$11\" }${12:visible=\"$13\" }${14:tooltip=\"$15\" }${16:bind=\"$17\"}}>\n\t$0\n</cfformitem>"),









            ("cfset\tCfml", "cfset $1 />"),

        ], sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)
