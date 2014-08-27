VARIABLES = {
'application':[],
'arguments':[],
'attributes':[],
'caller':[],
'cookie':[],
'flash':[],
'form':[],
'local':[],
'request':[],
'this':[],
'thistag':[],
'thread':[],
'url':[],
'variables':[],
'super':[],
'self':[],
'argumentcollection':[],
'client': 
[
('CFID'),
('CFToken'),
('HitCount'),
('LastVisit'),
('TimeCreated'),
('URLToken')
],
'server': 
[
('ColdFusion.ProductName'),
('ColdFusion.ProductVersion'),
('ColdFusion.ProductLevel'),
('ColdFusion.SerialNumber'),
('ColdFusion.SupportedLocales'),
('ColdFusion.AppServer'),
('ColdFusion.Expiration'),
('ColdFusion.RootDir'),
('OS.Name'),
('OS.AdditionalInformation'),
('OS.Version'),
('OS.BuildNumber')
],
'session': 
[
('CFID'),
('CFToken'),
('URLToken')
],
'cgi': 
[
('AUTH_PASSWORD'),
('AUTH_TYPE'),
('AUTH_USER'),
('CERT_COOKIE'),
('CERT_FLAGS'),
('CERT_ISSUER'),
('CERT_KEYSIZE'),
('CERT_SECRETKEYSIZE'),
('CERT_SERIALNUMBER'),
('CERT_SERVER_ISSUER'),
('CERT_SERVER_SUBJECT'),
('CERT_SUBJECT'),
('CF_TEMPLATE_PATH'),
('CONTENT_LENGTH'),
('CONTENT_TYPE'),
('CONTEXT_PATH'),
('GATEWAY_INTERFACE'),
('HTTPS'),
('HTTPS_KEYSIZE'),
('HTTPS_SECRETKEYSIZE'),
('HTTPS_SERVER_ISSUER'),
('HTTPS_SERVER_SUBJECT'),
('HTTP_ACCEPT'),
('HTTP_ACCEPT_ENCODING'),
('HTTP_ACCEPT_LANGUAGE'),
('HTTP_CONNECTION'),
('HTTP_COOKIE'),
('HTTP_HOST'),
('HTTP_REFERER'),
('HTTP_USER_AGENT'),
('HTTP_IF_MODIFIED_SINCE'),
('PATH_INFO'),
('PATH_TRANSLATED'),
('QUERY_STRING'),
('REMOTE_ADDR'),
('REMOTE_HOST'),
('REMOTE_USER'),
('REMOTE_IDENT'),
('REQUEST_METHOD'),
('SCRIPT_NAME'),
('SERVER_NAME'),
('SERVER_PORT'),
('SERVER_PORT_SECURE'),
('SERVER_PROTOCOL'),
('SERVER_SOFTWARE'),
('WEB_SERVER_AP')
]
}

TAGS = {
'cfabort':
[
('showerror\t@showerror','showerror="$1"')
],
'cfapplet':
[
('appletsource\t@appletsource','appletsource="$1"'),
('name\t@name','name="$1"'),
('height\t@height','height="$1"'),
('width\t@width','width="$1"'),
('vspace\t@vspace','vspace="$1"'),
('hspace\t@hspace','hspace="$1"'),
('align\t@align','align="$1"'),
('align="top"\talign', 'align="top"'),
('align="left"\talign', 'align="left"'),
('align="bottom"\talign', 'align="bottom"'),
('align="baseline"\talign', 'align="baseline"'),
('align="texttop"\talign', 'align="texttop"'),
('align="absbottom"\talign', 'align="absbottom"'),
('align="middle"\talign', 'align="middle"'),
('align="absmiddle"\talign', 'align="absmiddle"'),
('align="right"\talign', 'align="right"'),
('notsupported\t@notsupported','notsupported="$1"')
],
'cfapplication':
[
('name\t@name','name="$1"'),
('loginstorage\t@loginstorage','loginstorage="$1"'),
('loginstorage="cookie"\tloginstorage', 'loginstorage="cookie"'),
('loginstorage="session"\tloginstorage', 'loginstorage="session"'),
('clientmanagement\t@clientmanagement','clientmanagement="$1"'),
('clientmanagement="true"\tclientmanagement', 'clientmanagement="true"'),
('clientmanagement="false"\tclientmanagement', 'clientmanagement="false"'),
('clientstorage\t@clientstorage','clientstorage="$1"'),
('clientstorage="cookie"\tclientstorage', 'clientstorage="cookie"'),
('clientstorage="registry"\tclientstorage', 'clientstorage="registry"'),
('clientstorage="datasource_name"\tclientstorage', 'clientstorage="datasource_name"'),
('setclientcookies\t@setclientcookies','setclientcookies="$1"'),
('setclientcookies="true"\tsetclientcookies', 'setclientcookies="true"'),
('setclientcookies="false"\tsetclientcookies', 'setclientcookies="false"'),
('sessionmanagement\t@sessionmanagement','sessionmanagement="$1"'),
('sessionmanagement="true"\tsessionmanagement', 'sessionmanagement="true"'),
('sessionmanagement="false"\tsessionmanagement', 'sessionmanagement="false"'),
('sessiontimeout\t@sessiontimeout','sessiontimeout="$1"'),
('applicationtimeout\t@applicationtimeout','applicationtimeout="$1"'),
('setdomaincookies\t@setdomaincookies','setdomaincookies="$1"'),
('setdomaincookies="true"\tsetdomaincookies', 'setdomaincookies="true"'),
('setdomaincookies="false"\tsetdomaincookies', 'setdomaincookies="false"'),
('scriptprotect\t@scriptprotect','scriptprotect="$1"'),
('scriptprotect="none"\tscriptprotect', 'scriptprotect="none"'),
('scriptprotect="all"\tscriptprotect', 'scriptprotect="all"'),
('scriptprotect="form"\tscriptprotect', 'scriptprotect="form"'),
('scriptprotect="url"\tscriptprotect', 'scriptprotect="url"'),
('scriptprotect="cookie"\tscriptprotect', 'scriptprotect="cookie"'),
('scriptprotect="cgi"\tscriptprotect', 'scriptprotect="cgi"'),
('scriptprotect="form,url"\tscriptprotect', 'scriptprotect="form,url"'),
('scriptprotect="form,url,cookie"\tscriptprotect', 'scriptprotect="form,url,cookie"'),
('scriptprotect="form,url,cookie,cgi"\tscriptprotect', 'scriptprotect="form,url,cookie,cgi"'),
('securejsonprefix\t@securejsonprefix','securejsonprefix="$1"'),
('securejsonprefix="true"\tsecurejsonprefix', 'securejsonprefix="true"'),
('securejsonprefix="false"\tsecurejsonprefix', 'securejsonprefix="false"'),
('securejson\t@securejson','securejson="$1"'),
('securejson="true"\tsecurejson', 'securejson="true"'),
('securejson="false"\tsecurejson', 'securejson="false"'),
('serverSideFormValidation\t@serverSideFormValidation','serverSideFormValidation="$1"'),
('serverSideFormValidation="true"\tserverSideFormValidation', 'serverSideFormValidation="true"'),
('serverSideFormValidation="false"\tserverSideFormValidation', 'serverSideFormValidation="false"'),
('datasource\t@datasource','datasource="$1"'),
('exchangeserverversion\t@exchangeserverversion','exchangeserverversion="$1"'),
('exchangeserverversion="2003"\texchangeserverversion', 'exchangeserverversion="2003"'),
('exchangeserverversion="2007"\texchangeserverversion', 'exchangeserverversion="2007"'),
('exchangeserverversion="2010"\texchangeserverversion', 'exchangeserverversion="2010"'),
('authcookie\t@authcookie','authcookie="$1"'),
('sessioncookie\t@sessioncookie','sessioncookie="$1"'),
('wsversion\t@wsversion','wsversion="$1"')
],
'cfargument':
[
('name\t@name','name="$1"'),
('type\t@type','type="$1"'),
('type="any"\ttype', 'type="any"'),
('type="array"\ttype', 'type="array"'),
('type="binary"\ttype', 'type="binary"'),
('type="boolean"\ttype', 'type="boolean"'),
('type="date"\ttype', 'type="date"'),
('type="guid"\ttype', 'type="guid"'),
('type="numeric"\ttype', 'type="numeric"'),
('type="query"\ttype', 'type="query"'),
('type="string"\ttype', 'type="string"'),
('type="struct"\ttype', 'type="struct"'),
('type="uuid"\ttype', 'type="uuid"'),
('type="xml"\ttype', 'type="xml"'),
('type="variablename"\ttype', 'type="variablename"'),
('type="(component name)"\ttype', 'type="${1:component name}"'),
('required\t@required','required="$1"'),
('required="true"\trequired', 'required="true"'),
('required="false"\trequired', 'required="false"'),
('default\t@default','default="$1"'),
('displayname\t@displayname','displayname="$1"'),
('hint\t@hint','hint="$1"'),
('restargsource\t@restargsource','restargsource="$1"'),
('restargsource="path"\trestargsource', 'restargsource="path"'),
('restargsource="query "\trestargsource', 'restargsource="query "'),
('restargsource="matrix"\trestargsource', 'restargsource="matrix"'),
('restargsource="header"\trestargsource', 'restargsource="header"'),
('restargsource="cookie"\trestargsource', 'restargsource="cookie"'),
('restargsource="form"\trestargsource', 'restargsource="form"'),
('restargname\t@restargname','restargname="$1"')
],
'cfassociate':
[
('basetag\t@basetag','basetag="$1"'),
('datacollection\t@datacollection','datacollection="$1"')
],
'cfbreak':
[

],
'cfcache':
[
('action\t@action','action="$1"'),
('action="cache"\taction', 'action="cache"'),
('action="flush"\taction', 'action="flush"'),
('action="clientcache"\taction', 'action="clientcache"'),
('action="servercache"\taction', 'action="servercache"'),
('action="optimal"\taction', 'action="optimal"'),
('action="get"\taction', 'action="get"'),
('action="put"\taction', 'action="put"'),
('directory\t@directory','directory="$1"'),
('timespan\t@timespan','timespan="$1"'),
('expireurl\t@expireurl','expireurl="$1"'),
('username\t@username','username="$1"'),
('password\t@password','password="$1"'),
('port\t@port','port="$1"'),
('protocol\t@protocol','protocol="$1"'),
('protocol="http://"\tprotocol', 'protocol="http://"'),
('protocol="https://"\tprotocol', 'protocol="https://"'),
('value\t@value','value="$1"'),
('metadata\t@metadata','metadata="$1"'),
('stripwhitespace\t@stripwhitespace','stripwhitespace="$1"'),
('stripwhitespace="true"\tstripwhitespace', 'stripwhitespace="true"'),
('stripwhitespace="false"\tstripwhitespace', 'stripwhitespace="false"'),
('throwonerror\t@throwonerror','throwonerror="$1"'),
('id\t@id','id="$1"'),
('region\t@region','region="$1"'),
('usecache\t@usecache','usecache="$1"'),
('usecache="true"\tusecache', 'usecache="true"'),
('usecache="false"\tusecache', 'usecache="false"'),
('dependson\t@dependson','dependson="$1"'),
('idletime\t@idletime','idletime="$1"'),
('name\t@name','name="$1"'),
('useQueryString\t@useQueryString','useQueryString="$1"'),
('useQueryString="true"\tuseQueryString', 'useQueryString="true"'),
('useQueryString="false"\tuseQueryString', 'useQueryString="false"'),
('timeout\t@timeout','timeout="$1"'),
('cachedirectory\t@cachedirectory','cachedirectory="$1"'),
('key\t@key','key="$1"')
],
'cfcalendar':
[
('name\t@name','name="$1"'),
('height\t@height','height="$1"'),
('width\t@width','width="$1"'),
('selecteddate\t@selecteddate','selecteddate="$1"'),
('startrange\t@startrange','startrange="$1"'),
('endrange\t@endrange','endrange="$1"'),
('disabled\t@disabled','disabled="$1"'),
('disabled="true"\tdisabled', 'disabled="true"'),
('disabled="false"\tdisabled', 'disabled="false"'),
('mask\t@mask','mask="$1"'),
('mask="mm/dd/yyyy"\tmask', 'mask="mm/dd/yyyy"'),
('mask="dd/mm/yyyy"\tmask', 'mask="dd/mm/yyyy"'),
('mask="mm/yyyy"\tmask', 'mask="mm/yyyy"'),
('mask="mm/yy"\tmask', 'mask="mm/yy"'),
('mask="yyyy-mm-dd"\tmask', 'mask="yyyy-mm-dd"'),
('mask="eee dd. mmm yyyy"\tmask', 'mask="eee dd. mmm yyyy"'),
('firstdayofweek\t@firstdayofweek','firstdayofweek="$1"'),
('firstdayofweek="0"\tfirstdayofweek', 'firstdayofweek="0"'),
('firstdayofweek="1"\tfirstdayofweek', 'firstdayofweek="1"'),
('firstdayofweek="2"\tfirstdayofweek', 'firstdayofweek="2"'),
('firstdayofweek="3"\tfirstdayofweek', 'firstdayofweek="3"'),
('firstdayofweek="4"\tfirstdayofweek', 'firstdayofweek="4"'),
('firstdayofweek="5"\tfirstdayofweek', 'firstdayofweek="5"'),
('firstdayofweek="6"\tfirstdayofweek', 'firstdayofweek="6"'),
('daynames\t@daynames','daynames="$1"'),
('daynames="s,m,t,w,th,f,s"\tdaynames', 'daynames="s,m,t,w,th,f,s"'),
('daynames="sunday,monday,tuesday,wednesday,thursday,friday,saturday"\tdaynames', 'daynames="sunday,monday,tuesday,wednesday,thursday,friday,saturday"'),
('daynames="sun,mon,tue,wed,thu,fri,sat"\tdaynames', 'daynames="sun,mon,tue,wed,thu,fri,sat"'),
('monthnames\t@monthnames','monthnames="$1"'),
('monthnames="january,february,march,april,may,june,july,august,september,october,november,december"\tmonthnames', 'monthnames="january,february,march,april,may,june,july,august,september,october,november,december"'),
('monthnames="jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec"\tmonthnames', 'monthnames="jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec"'),
('enabled\t@enabled','enabled="$1"'),
('enabled="true"\tenabled', 'enabled="true"'),
('enabled="false"\tenabled', 'enabled="false"'),
('visible\t@visible','visible="$1"'),
('visible="true"\tvisible', 'visible="true"'),
('visible="false"\tvisible', 'visible="false"'),
('tooltip\t@tooltip','tooltip="$1"'),
('style\t@style','style="$1"'),
('style="haloblue"\tstyle', 'style="haloblue"'),
('style="halogreen"\tstyle', 'style="halogreen"'),
('style="haloorange"\tstyle', 'style="haloorange"'),
('style="halosilver"\tstyle', 'style="halosilver"'),
('onchange\t@onchange','onchange="$1"'),
('onblur\t@onblur','onblur="$1"'),
('onfocus\t@onfocus','onfocus="$1"')
],
'cfcase':
[
('value\t@value','value="$1"'),
('delimiters\t@delimiters','delimiters="$1"'),
('delimiters=","\tdelimiters', 'delimiters=","'),
('delimiters=";"\tdelimiters', 'delimiters=";"'),
('delimiters="|"\tdelimiters', 'delimiters="|"'),
('delimiters=":"\tdelimiters', 'delimiters=":"')
],
'cfcatch':
[
('type\t@type','type="$1"'),
('type="application"\ttype', 'type="application"'),
('type="database"\ttype', 'type="database"'),
('type="template"\ttype', 'type="template"'),
('type="security"\ttype', 'type="security"'),
('type="object"\ttype', 'type="object"'),
('type="missinginclude"\ttype', 'type="missinginclude"'),
('type="expression"\ttype', 'type="expression"'),
('type="lock"\ttype', 'type="lock"'),
('type="custom_type"\ttype', 'type="custom_type"'),
('type="searchengine"\ttype', 'type="searchengine"'),
('type="any"\ttype', 'type="any"'),
('name\t@name','name="$1"')
],
'cfchart':
[
('chartheight\t@chartheight','chartheight="$1"'),
('chartwidth\t@chartwidth','chartwidth="$1"'),
('scalefrom\t@scalefrom','scalefrom="$1"'),
('scaleto\t@scaleto','scaleto="$1"'),
('showxgridlines\t@showxgridlines','showxgridlines="$1"'),
('showxgridlines="true"\tshowxgridlines', 'showxgridlines="true"'),
('showxgridlines="false"\tshowxgridlines', 'showxgridlines="false"'),
('showygridlines\t@showygridlines','showygridlines="$1"'),
('showygridlines="true"\tshowygridlines', 'showygridlines="true"'),
('showygridlines="false"\tshowygridlines', 'showygridlines="false"'),
('gridlines\t@gridlines','gridlines="$1"'),
('seriesplacement\t@seriesplacement','seriesplacement="$1"'),
('seriesplacement="default"\tseriesplacement', 'seriesplacement="default"'),
('seriesplacement="cluster"\tseriesplacement', 'seriesplacement="cluster"'),
('seriesplacement="stacked"\tseriesplacement', 'seriesplacement="stacked"'),
('seriesplacement="percent"\tseriesplacement', 'seriesplacement="percent"'),
('foregroundcolor\t@foregroundcolor','foregroundcolor="$1"'),
('foregroundcolor="aqua"\tforegroundcolor', 'foregroundcolor="aqua"'),
('foregroundcolor="black"\tforegroundcolor', 'foregroundcolor="black"'),
('foregroundcolor="blue"\tforegroundcolor', 'foregroundcolor="blue"'),
('foregroundcolor="fuchsia"\tforegroundcolor', 'foregroundcolor="fuchsia"'),
('foregroundcolor="grey"\tforegroundcolor', 'foregroundcolor="grey"'),
('foregroundcolor="green"\tforegroundcolor', 'foregroundcolor="green"'),
('foregroundcolor="lime"\tforegroundcolor', 'foregroundcolor="lime"'),
('foregroundcolor="maroon"\tforegroundcolor', 'foregroundcolor="maroon"'),
('foregroundcolor="navy"\tforegroundcolor', 'foregroundcolor="navy"'),
('foregroundcolor="olive"\tforegroundcolor', 'foregroundcolor="olive"'),
('foregroundcolor="purple"\tforegroundcolor', 'foregroundcolor="purple"'),
('foregroundcolor="red"\tforegroundcolor', 'foregroundcolor="red"'),
('foregroundcolor="silver"\tforegroundcolor', 'foregroundcolor="silver"'),
('foregroundcolor="teal"\tforegroundcolor', 'foregroundcolor="teal"'),
('foregroundcolor="white"\tforegroundcolor', 'foregroundcolor="white"'),
('foregroundcolor="yellow"\tforegroundcolor', 'foregroundcolor="yellow"'),
('backgroundcolor\t@backgroundcolor','backgroundcolor="$1"'),
('backgroundcolor="aqua"\tbackgroundcolor', 'backgroundcolor="aqua"'),
('backgroundcolor="black"\tbackgroundcolor', 'backgroundcolor="black"'),
('backgroundcolor="blue"\tbackgroundcolor', 'backgroundcolor="blue"'),
('backgroundcolor="fuchsia"\tbackgroundcolor', 'backgroundcolor="fuchsia"'),
('backgroundcolor="grey"\tbackgroundcolor', 'backgroundcolor="grey"'),
('backgroundcolor="green"\tbackgroundcolor', 'backgroundcolor="green"'),
('backgroundcolor="lime"\tbackgroundcolor', 'backgroundcolor="lime"'),
('backgroundcolor="maroon"\tbackgroundcolor', 'backgroundcolor="maroon"'),
('backgroundcolor="navy"\tbackgroundcolor', 'backgroundcolor="navy"'),
('backgroundcolor="olive"\tbackgroundcolor', 'backgroundcolor="olive"'),
('backgroundcolor="purple"\tbackgroundcolor', 'backgroundcolor="purple"'),
('backgroundcolor="red"\tbackgroundcolor', 'backgroundcolor="red"'),
('backgroundcolor="silver"\tbackgroundcolor', 'backgroundcolor="silver"'),
('backgroundcolor="teal"\tbackgroundcolor', 'backgroundcolor="teal"'),
('backgroundcolor="white"\tbackgroundcolor', 'backgroundcolor="white"'),
('backgroundcolor="yellow"\tbackgroundcolor', 'backgroundcolor="yellow"'),
('showborder\t@showborder','showborder="$1"'),
('showborder="true"\tshowborder', 'showborder="true"'),
('showborder="false"\tshowborder', 'showborder="false"'),
('databackgroundcolor\t@databackgroundcolor','databackgroundcolor="$1"'),
('databackgroundcolor="aqua"\tdatabackgroundcolor', 'databackgroundcolor="aqua"'),
('databackgroundcolor="black"\tdatabackgroundcolor', 'databackgroundcolor="black"'),
('databackgroundcolor="blue"\tdatabackgroundcolor', 'databackgroundcolor="blue"'),
('databackgroundcolor="fuchsia"\tdatabackgroundcolor', 'databackgroundcolor="fuchsia"'),
('databackgroundcolor="grey"\tdatabackgroundcolor', 'databackgroundcolor="grey"'),
('databackgroundcolor="green"\tdatabackgroundcolor', 'databackgroundcolor="green"'),
('databackgroundcolor="lime"\tdatabackgroundcolor', 'databackgroundcolor="lime"'),
('databackgroundcolor="maroon"\tdatabackgroundcolor', 'databackgroundcolor="maroon"'),
('databackgroundcolor="navy"\tdatabackgroundcolor', 'databackgroundcolor="navy"'),
('databackgroundcolor="olive"\tdatabackgroundcolor', 'databackgroundcolor="olive"'),
('databackgroundcolor="purple"\tdatabackgroundcolor', 'databackgroundcolor="purple"'),
('databackgroundcolor="red"\tdatabackgroundcolor', 'databackgroundcolor="red"'),
('databackgroundcolor="silver"\tdatabackgroundcolor', 'databackgroundcolor="silver"'),
('databackgroundcolor="teal"\tdatabackgroundcolor', 'databackgroundcolor="teal"'),
('databackgroundcolor="white"\tdatabackgroundcolor', 'databackgroundcolor="white"'),
('databackgroundcolor="yellow"\tdatabackgroundcolor', 'databackgroundcolor="yellow"'),
('font\t@font','font="$1"'),
('font="arial"\tfont', 'font="arial"'),
('font="times"\tfont', 'font="times"'),
('font="courier"\tfont', 'font="courier"'),
('font="arialunicodems"\tfont', 'font="arialunicodems"'),
('fontsize\t@fontsize','fontsize="$1"'),
('fontitalic\t@fontitalic','fontitalic="$1"'),
('fontitalic="true"\tfontitalic', 'fontitalic="true"'),
('fontitalic="false"\tfontitalic', 'fontitalic="false"'),
('fontbold\t@fontbold','fontbold="$1"'),
('fontbold="true"\tfontbold', 'fontbold="true"'),
('fontbold="false"\tfontbold', 'fontbold="false"'),
('labelformat\t@labelformat','labelformat="$1"'),
('labelformat="number"\tlabelformat', 'labelformat="number"'),
('labelformat="currency"\tlabelformat', 'labelformat="currency"'),
('labelformat="percent"\tlabelformat', 'labelformat="percent"'),
('labelformat="date"\tlabelformat', 'labelformat="date"'),
('xaxistitle\t@xaxistitle','xaxistitle="$1"'),
('yaxistitle\t@yaxistitle','yaxistitle="$1"'),
('xaxistype\t@xaxistype','xaxistype="$1"'),
('xaxistype="category"\txaxistype', 'xaxistype="category"'),
('xaxistype="scale"\txaxistype', 'xaxistype="scale"'),
('yaxistype\t@yaxistype','yaxistype="$1"'),
('yaxistype="category"\tyaxistype', 'yaxistype="category"'),
('yaxistype="scale"\tyaxistype', 'yaxistype="scale"'),
('sortxaxis\t@sortxaxis','sortxaxis="$1"'),
('sortxaxis="true"\tsortxaxis', 'sortxaxis="true"'),
('sortxaxis="false"\tsortxaxis', 'sortxaxis="false"'),
('show3d\t@show3d','show3d="$1"'),
('show3d="true"\tshow3d', 'show3d="true"'),
('show3d="false"\tshow3d', 'show3d="false"'),
('xoffset\t@xoffset','xoffset="$1"'),
('yoffset\t@yoffset','yoffset="$1"'),
('showlegend\t@showlegend','showlegend="$1"'),
('showlegend="true"\tshowlegend', 'showlegend="true"'),
('showlegend="false"\tshowlegend', 'showlegend="false"'),
('tipstyle\t@tipstyle','tipstyle="$1"'),
('tipstyle="mousedown"\ttipstyle', 'tipstyle="mousedown"'),
('tipstyle="mouseover"\ttipstyle', 'tipstyle="mouseover"'),
('tipstyle="none"\ttipstyle', 'tipstyle="none"'),
('tipbgcolor\t@tipbgcolor','tipbgcolor="$1"'),
('tipbgcolor="aqua"\ttipbgcolor', 'tipbgcolor="aqua"'),
('tipbgcolor="black"\ttipbgcolor', 'tipbgcolor="black"'),
('tipbgcolor="blue"\ttipbgcolor', 'tipbgcolor="blue"'),
('tipbgcolor="fuchsia"\ttipbgcolor', 'tipbgcolor="fuchsia"'),
('tipbgcolor="grey"\ttipbgcolor', 'tipbgcolor="grey"'),
('tipbgcolor="green"\ttipbgcolor', 'tipbgcolor="green"'),
('tipbgcolor="lime"\ttipbgcolor', 'tipbgcolor="lime"'),
('tipbgcolor="maroon"\ttipbgcolor', 'tipbgcolor="maroon"'),
('tipbgcolor="navy"\ttipbgcolor', 'tipbgcolor="navy"'),
('tipbgcolor="olive"\ttipbgcolor', 'tipbgcolor="olive"'),
('tipbgcolor="purple"\ttipbgcolor', 'tipbgcolor="purple"'),
('tipbgcolor="red"\ttipbgcolor', 'tipbgcolor="red"'),
('tipbgcolor="silver"\ttipbgcolor', 'tipbgcolor="silver"'),
('tipbgcolor="teal"\ttipbgcolor', 'tipbgcolor="teal"'),
('tipbgcolor="white"\ttipbgcolor', 'tipbgcolor="white"'),
('tipbgcolor="yellow"\ttipbgcolor', 'tipbgcolor="yellow"'),
('showmarkers\t@showmarkers','showmarkers="$1"'),
('showmarkers="true"\tshowmarkers', 'showmarkers="true"'),
('showmarkers="false"\tshowmarkers', 'showmarkers="false"'),
('markersize\t@markersize','markersize="$1"'),
('pieslicestyle\t@pieslicestyle','pieslicestyle="$1"'),
('pieslicestyle="solid"\tpieslicestyle', 'pieslicestyle="solid"'),
('pieslicestyle="sliced"\tpieslicestyle', 'pieslicestyle="sliced"'),
('URL\t@URL','URL="$1"'),
('URL="$value$"\tURL', 'URL="$value$"'),
('URL="$itemlabel$"\tURL', 'URL="$itemlabel$"'),
('URL="$serieslabel$"\tURL', 'URL="$serieslabel$"'),
('name\t@name','name="$1"'),
('style\t@style','style="$1"'),
('style="beige"\tstyle', 'style="beige"'),
('style="blue"\tstyle', 'style="blue"'),
('style="default"\tstyle', 'style="default"'),
('style="red"\tstyle', 'style="red"'),
('style="silver"\tstyle', 'style="silver"'),
('style="yellow"\tstyle', 'style="yellow"'),
('title\t@title','title="$1"'),
('arrows\t@arrows','arrows="$1"'),
('aspect3d\t@aspect3d','aspect3d="$1"'),
('height\t@height','height="$1"'),
('labels\t@labels','labels="$1"'),
('legend\t@legend','legend="$1"'),
('zoom\t@zoom','zoom="$1"'),
('plot\t@plot','plot="$1"'),
('preview\t@preview','preview="$1"'),
('renderer\t@renderer','renderer="$1"'),
('renderer="canvas"\trenderer', 'renderer="canvas"'),
('renderer="svg"\trenderer', 'renderer="svg"'),
('renderer="flash"\trenderer', 'renderer="flash"'),
('renderer="vml"\trenderer', 'renderer="vml"'),
('scales\t@scales','scales="$1"'),
('tooltip\t@tooltip','tooltip="$1"'),
('type\t@type','type="$1"'),
('type="area"\ttype', 'type="area"'),
('type="bar"\ttype', 'type="bar"'),
('type="bubble"\ttype', 'type="bubble"'),
('type="gauge"\ttype', 'type="gauge"'),
('type="hbar"\ttype', 'type="hbar"'),
('type="hbullet"\ttype', 'type="hbullet"'),
('type="line"\ttype', 'type="line"'),
('type="nestedpie"\ttype', 'type="nestedpie"'),
('type="pie"\ttype', 'type="pie"'),
('type="radar"\ttype', 'type="radar"'),
('type="scatter"\ttype', 'type="scatter"'),
('type="bullet"\ttype', 'type="bullet"'),
('type="hfunnel"\ttype', 'type="hfunnel"'),
('type="funnel"\ttype', 'type="funnel"'),
('type="piano"\ttype', 'type="piano"'),
('type="curve"\ttype', 'type="curve"'),
('type="step"\ttype', 'type="step"'),
('xaxis\t@xaxis','xaxis="$1"'),
('yaxis\t@yaxis','yaxis="$1"'),
('xaxis2\t@xaxis2','xaxis2="$1"'),
('yaxis2\t@yaxis2','yaxis2="$1"'),
('xaxisvalues\t@xaxisvalues','xaxisvalues="$1"'),
('yaxisvalues\t@yaxisvalues','yaxisvalues="$1"'),
('width\t@width','width="$1"'),
('alpha\t@alpha','alpha="$1"'),
('background\t@background','background="$1"'),
('bevel\t@bevel','bevel="$1"'),
('border\t@border','border="$1"'),
('crosshair\t@crosshair','crosshair="$1"'),
('fill\t@fill','fill="$1"'),
('plotarea\t@plotarea','plotarea="$1"'),
('format\t@format','format="$1"'),
('format="html"\tformat', 'format="html"'),
('format="flash"\tformat', 'format="flash"'),
('format="jpg"\tformat', 'format="jpg"'),
('format="png"\tformat', 'format="png"'),
('plotarea\t@plotarea','plotarea="$1"'),
('refresh\t@refresh','refresh="$1"'),
('query\t@query','query="$1"')
],
'cfchartdata':
[
('item\t@item','item="$1"'),
('value\t@value','value="$1"')
],
'cfchartseries':
[
('type\t@type','type="$1"'),
('type="area"\ttype', 'type="area"'),
('type="bar"\ttype', 'type="bar"'),
('type="bubble"\ttype', 'type="bubble"'),
('type="gauge"\ttype', 'type="gauge"'),
('type="hbar"\ttype', 'type="hbar"'),
('type="hbullet"\ttype', 'type="hbullet"'),
('type="line"\ttype', 'type="line"'),
('type="nestedpie"\ttype', 'type="nestedpie"'),
('type="pie"\ttype', 'type="pie"'),
('type="radar"\ttype', 'type="radar"'),
('type="scatter"\ttype', 'type="scatter"'),
('type="bullet"\ttype', 'type="bullet"'),
('type="hfunnel"\ttype', 'type="hfunnel"'),
('type="funnel"\ttype', 'type="funnel"'),
('type="piano"\ttype', 'type="piano"'),
('type="curve"\ttype', 'type="curve"'),
('type="step"\ttype', 'type="step"'),
('query\t@query','query="$1"'),
('itemcolumn\t@itemcolumn','itemcolumn="$1"'),
('valuecolumn\t@valuecolumn','valuecolumn="$1"'),
('paintstyle\t@paintstyle','paintstyle="$1"'),
('paintstyle="plain"\tpaintstyle', 'paintstyle="plain"'),
('paintstyle="raise"\tpaintstyle', 'paintstyle="raise"'),
('paintstyle="shade"\tpaintstyle', 'paintstyle="shade"'),
('paintstyle="light"\tpaintstyle', 'paintstyle="light"'),
('markerstyle\t@markerstyle','markerstyle="$1"'),
('markerstyle="rectangle"\tmarkerstyle', 'markerstyle="rectangle"'),
('markerstyle="triangle"\tmarkerstyle', 'markerstyle="triangle"'),
('markerstyle="diamond"\tmarkerstyle', 'markerstyle="diamond"'),
('markerstyle="circle"\tmarkerstyle', 'markerstyle="circle"'),
('markerstyle="letter"\tmarkerstyle', 'markerstyle="letter"'),
('markerstyle="mcross"\tmarkerstyle', 'markerstyle="mcross"'),
('markerstyle="snow"\tmarkerstyle', 'markerstyle="snow"'),
('markerstyle="rcross"\tmarkerstyle', 'markerstyle="rcross"'),
('colorlist\t@colorlist','colorlist="$1"'),
('datalabelstyle\t@datalabelstyle','datalabelstyle="$1"'),
('datalabelstyle="none"\tdatalabelstyle', 'datalabelstyle="none"'),
('datalabelstyle="value"\tdatalabelstyle', 'datalabelstyle="value"'),
('datalabelstyle="rowlabel"\tdatalabelstyle', 'datalabelstyle="rowlabel"'),
('datalabelstyle="columnlabel"\tdatalabelstyle', 'datalabelstyle="columnlabel"'),
('datalabelstyle="pattern"\tdatalabelstyle', 'datalabelstyle="pattern"'),
('alpha\t@alpha','alpha="$1"'),
('background\t@background','background="$1"'),
('bevel\t@bevel','bevel="$1"'),
('border\t@border','border="$1"'),
('aspect\t@aspect','aspect="$1"'),
('animate\t@animate','animate="$1"'),
('data\t@data','data="$1"'),
('hovermarker\t@hovermarker','hovermarker="$1"'),
('marker\t@marker','marker="$1"'),
('scales\t@scales','scales="$1"'),
('shadow\t@shadow','shadow="$1"'),
('zcolumn\t@zcolumn','zcolumn="$1"'),
('tooltip\t@tooltip','tooltip="$1"'),
('label\t@label','label="$1"'),
('seriescolor\t@seriescolor','seriescolor="$1"')
],
'cfcol':
[
('header\t@header','header="$1"'),
('width\t@width','width="$1"'),
('align\t@align','align="$1"'),
('align="left"\talign', 'align="left"'),
('align="center"\talign', 'align="center"'),
('align="right"\talign', 'align="right"'),
('text\t@text','text="$1"')
],
'cfcollection':
[
('action\t@action','action="$1"'),
('action="categorylist"\taction', 'action="categorylist"'),
('action="create"\taction', 'action="create"'),
('action="delete"\taction', 'action="delete"'),
('action="optimize"\taction', 'action="optimize"'),
('action="list"\taction', 'action="list"'),
('action="map"\taction', 'action="map"'),
('action="repair"\taction', 'action="repair"'),
('collection\t@collection','collection="$1"'),
('path\t@path','path="$1"'),
('language\t@language','language="$1"'),
('name\t@name','name="$1"'),
('categories\t@categories','categories="$1"'),
('categories="true"\tcategories', 'categories="true"'),
('categories="false"\tcategories', 'categories="false"')
],
'cfcomponent':
[
('extends\t@extends','extends="$1"'),
('initmethod\t@initmethod','initmethod="$1"'),
('implements\t@implements','implements="$1"'),
('output\t@output','output="$1"'),
('output="true"\toutput', 'output="true"'),
('output="false"\toutput', 'output="false"'),
('displayname\t@displayname','displayname="$1"'),
('hint\t@hint','hint="$1"'),
('style\t@style','style="$1"'),
('style="rpc"\tstyle', 'style="rpc"'),
('style="document"\tstyle', 'style="document"'),
('style="wrapped"\tstyle', 'style="wrapped"'),
('namespace\t@namespace','namespace="$1"'),
('serviceportname\t@serviceportname','serviceportname="$1"'),
('porttypename\t@porttypename','porttypename="$1"'),
('bindingname\t@bindingname','bindingname="$1"'),
('wsdlfile\t@wsdlfile','wsdlfile="$1"'),
('serviceaddress\t@serviceaddress','serviceaddress="$1"'),
('persistent\t@persistent','persistent="$1"'),
('persistent="true"\tpersistent', 'persistent="true"'),
('persistent="false"\tpersistent', 'persistent="false"'),
('entityName\t@entityName','entityName="$1"'),
('table\t@table','table="$1"'),
('schema\t@schema','schema="$1"'),
('catalog\t@catalog','catalog="$1"'),
('dynamicinsert\t@dynamicinsert','dynamicinsert="$1"'),
('dynamicinsert="true"\tdynamicinsert', 'dynamicinsert="true"'),
('dynamicinsert="false"\tdynamicinsert', 'dynamicinsert="false"'),
('dynamicupdate\t@dynamicupdate','dynamicupdate="$1"'),
('dynamicupdate="true"\tdynamicupdate', 'dynamicupdate="true"'),
('dynamicupdate="false"\tdynamicupdate', 'dynamicupdate="false"'),
('readonly\t@readonly','readonly="$1"'),
('readonly="true"\treadonly', 'readonly="true"'),
('readonly="false"\treadonly', 'readonly="false"'),
('selectbeforeupdate\t@selectbeforeupdate','selectbeforeupdate="$1"'),
('selectbeforeupdate="true"\tselectbeforeupdate', 'selectbeforeupdate="true"'),
('selectbeforeupdate="false"\tselectbeforeupdate', 'selectbeforeupdate="false"'),
('batchsize\t@batchsize','batchsize="$1"'),
('optimisticlock\t@optimisticlock','optimisticlock="$1"'),
('optimisticlock="none"\toptimisticlock', 'optimisticlock="none"'),
('optimisticlock="dirty"\toptimisticlock', 'optimisticlock="dirty"'),
('optimisticlock="all"\toptimisticlock', 'optimisticlock="all"'),
('optimisticlock="version"\toptimisticlock', 'optimisticlock="version"'),
('lazy\t@lazy','lazy="$1"'),
('lazy="true"\tlazy', 'lazy="true"'),
('lazy="false"\tlazy', 'lazy="false"'),
('rowid\t@rowid','rowid="$1"'),
('discriminatorColumn\t@discriminatorColumn','discriminatorColumn="$1"'),
('discriminatorValue\t@discriminatorValue','discriminatorValue="$1"'),
('joinColumn\t@joinColumn','joinColumn="$1"'),
('embedded\t@embedded','embedded="$1"'),
('embedded="true"\tembedded', 'embedded="true"'),
('embedded="false"\tembedded', 'embedded="false"'),
('cacheUse\t@cacheUse','cacheUse="$1"'),
('cacheUse="read-only"\tcacheUse', 'cacheUse="read-only"'),
('cacheUse="nonstrict-read-write"\tcacheUse', 'cacheUse="nonstrict-read-write"'),
('cacheUse="read-write"\tcacheUse', 'cacheUse="read-write"'),
('cacheUse="transactional"\tcacheUse', 'cacheUse="transactional"'),
('cacheName\t@cacheName','cacheName="$1"'),
('saveMapping\t@saveMapping','saveMapping="$1"'),
('saveMapping="true"\tsaveMapping', 'saveMapping="true"'),
('saveMapping="false"\tsaveMapping', 'saveMapping="false"'),
('accessors\t@accessors','accessors="$1"'),
('accessors="true"\taccessors', 'accessors="true"'),
('accessors="false"\taccessors', 'accessors="false"'),
('serializable\t@serializable','serializable="$1"'),
('serializable="true"\tserializable', 'serializable="true"'),
('serializable="false"\tserializable', 'serializable="false"'),
('alias\t@alias','alias="$1"'),
('datasource\t@datasource','datasource="$1"'),
('mappedSuperClass\t@mappedSuperClass','mappedSuperClass="$1"'),
('mappedSuperClass="false"\tmappedSuperClass', 'mappedSuperClass="false"'),
('mappedSuperClass="true"\tmappedSuperClass', 'mappedSuperClass="true"'),
('rest\t@rest','rest="$1"'),
('rest="false"\trest', 'rest="false"'),
('rest="true"\trest', 'rest="true"'),
('restPath\t@restPath','restPath="$1"'),
('httpMethod\t@httpMethod','httpMethod="$1"'),
('httpMethod="get"\thttpMethod', 'httpMethod="get"'),
('httpMethod="delete"\thttpMethod', 'httpMethod="delete"'),
('httpMethod="post"\thttpMethod', 'httpMethod="post"'),
('httpMethod="put"\thttpMethod', 'httpMethod="put"'),
('httpMethod="head"\thttpMethod', 'httpMethod="head"'),
('httpMethod="options"\thttpMethod', 'httpMethod="options"'),
('produces\t@produces','produces="$1"'),
('consumes\t@consumes','consumes="$1"'),
('indexable\t@indexable','indexable="$1"'),
('indexable="false"\tindexable', 'indexable="false"'),
('indexable="true"\tindexable', 'indexable="true"'),
('indexLanguage\t@indexLanguage','indexLanguage="$1"'),
('autoindex\t@autoindex','autoindex="$1"'),
('autoindex="false"\tautoindex', 'autoindex="false"'),
('autoindex="true"\tautoindex', 'autoindex="true"'),
('wsversion\t@wsversion','wsversion="$1"'),
('wsversion="1"\twsversion', 'wsversion="1"'),
('wsversion="2"\twsversion', 'wsversion="2"')
],
'cfcontent':
[
('type\t@type','type="$1"'),
('type="text/html"\ttype', 'type="text/html"'),
('type="text/plain"\ttype', 'type="text/plain"'),
('type="application/msword"\ttype', 'type="application/msword"'),
('type="application/msexcel"\ttype', 'type="application/msexcel"'),
('type="application/poscript"\ttype', 'type="application/poscript"'),
('type="application/x-zip-compressed"\ttype', 'type="application/x-zip-compressed"'),
('type="application/pdf"\ttype', 'type="application/pdf"'),
('type="application/rtf"\ttype', 'type="application/rtf"'),
('type="video/x-msvideo"\ttype', 'type="video/x-msvideo"'),
('type="video/quicktime"\ttype', 'type="video/quicktime"'),
('type="video/x-mpeg2"\ttype', 'type="video/x-mpeg2"'),
('type="audio/x-pn/realaudio"\ttype', 'type="audio/x-pn/realaudio"'),
('type="audio/x-mpeg"\ttype', 'type="audio/x-mpeg"'),
('type="audio/x-waw"\ttype', 'type="audio/x-waw"'),
('type="audio/x-aiff"\ttype', 'type="audio/x-aiff"'),
('type="audio/basic"\ttype', 'type="audio/basic"'),
('type="image/tiff"\ttype', 'type="image/tiff"'),
('type="image/jpeg"\ttype', 'type="image/jpeg"'),
('type="image/gif"\ttype', 'type="image/gif"'),
('type="image/x-png"\ttype', 'type="image/x-png"'),
('type="image/x-photo-cd"\ttype', 'type="image/x-photo-cd"'),
('type="image/x-ms-bmp"\ttype', 'type="image/x-ms-bmp"'),
('type="image/x-rgb"\ttype', 'type="image/x-rgb"'),
('type="image/x-portable-pixmap"\ttype', 'type="image/x-portable-pixmap"'),
('type="image/x-portable-greymap"\ttype', 'type="image/x-portable-greymap"'),
('type="image/x-portablebitmap"\ttype', 'type="image/x-portablebitmap"'),
('deletefile\t@deletefile','deletefile="$1"'),
('deletefile="true"\tdeletefile', 'deletefile="true"'),
('deletefile="false"\tdeletefile', 'deletefile="false"'),
('file\t@file','file="$1"'),
('variable\t@variable','variable="$1"'),
('reset\t@reset','reset="$1"'),
('reset="true"\treset', 'reset="true"'),
('reset="false"\treset', 'reset="false"')
],
'cfcookie':
[
('name\t@name','name="$1"'),
('value\t@value','value="$1"'),
('expires\t@expires','expires="$1"'),
('secure\t@secure','secure="$1"'),
('secure="true"\tsecure', 'secure="true"'),
('secure="false"\tsecure', 'secure="false"'),
('path\t@path','path="$1"'),
('domain\t@domain','domain="$1"'),
('httpOnly\t@httpOnly','httpOnly="$1"'),
('httpOnly="true"\thttpOnly', 'httpOnly="true"'),
('httpOnly="false"\thttpOnly', 'httpOnly="false"'),
('casesensitive\t@casesensitive','casesensitive="$1"'),
('casesensitive="true"\tcasesensitive', 'casesensitive="true"'),
('casesensitive="false"\tcasesensitive', 'casesensitive="false"'),
('encodevalue\t@encodevalue','encodevalue="$1"'),
('encodevalue="true"\tencodevalue', 'encodevalue="true"'),
('encodevalue="false"\tencodevalue', 'encodevalue="false"'),
('preservecase\t@preservecase','preservecase="$1"'),
('preservecase="true"\tpreservecase', 'preservecase="true"'),
('preservecase="false"\tpreservecase', 'preservecase="false"')
],
'cfdbinfo':
[
('type\t@type','type="$1"'),
('type="clientinfo"\ttype', 'type="clientinfo"'),
('type="columns"\ttype', 'type="columns"'),
('type="dbnames"\ttype', 'type="dbnames"'),
('type="tables"\ttype', 'type="tables"'),
('type="foreignkeys"\ttype', 'type="foreignkeys"'),
('type="index"\ttype', 'type="index"'),
('type="procedures"\ttype', 'type="procedures"'),
('type="version"\ttype', 'type="version"'),
('datasource\t@datasource','datasource="$1"'),
('name\t@name','name="$1"'),
('dbname\t@dbname','dbname="$1"'),
('username\t@username','username="$1"'),
('password\t@password','password="$1"'),
('pattern\t@pattern','pattern="$1"'),
('table\t@table','table="$1"')
],
'cfdefaultcase':
[

],
'cfdirectory':
[
('action\t@action','action="$1"'),
('action="list"\taction', 'action="list"'),
('action="create"\taction', 'action="create"'),
('action="delete"\taction', 'action="delete"'),
('action="rename"\taction', 'action="rename"'),
('action="copy"\taction', 'action="copy"'),
('directory\t@directory','directory="$1"'),
('name\t@name','name="$1"'),
('filter\t@filter','filter="$1"'),
('mode\t@mode','mode="$1"'),
('sort\t@sort','sort="$1"'),
('sort="asc"\tsort', 'sort="asc"'),
('sort="desc"\tsort', 'sort="desc"'),
('newdirectory\t@newdirectory','newdirectory="$1"'),
('recurse\t@recurse','recurse="$1"'),
('recurse="true"\trecurse', 'recurse="true"'),
('recurse="false"\trecurse', 'recurse="false"'),
('type\t@type','type="$1"'),
('type="dir"\ttype', 'type="dir"'),
('type="file"\ttype', 'type="file"'),
('type="all"\ttype', 'type="all"'),
('listinfo\t@listinfo','listinfo="$1"'),
('listinfo="name"\tlistinfo', 'listinfo="name"'),
('listinfo="all"\tlistinfo', 'listinfo="all"'),
('storeLocation\t@storeLocation','storeLocation="$1"'),
('storeLocation="eu"\tstoreLocation', 'storeLocation="eu"'),
('storeLocation="us"\tstoreLocation', 'storeLocation="us"'),
('storeACL\t@storeACL','storeACL="$1"'),
('destination\t@destination','destination="$1"')
],
'cfdiv':
[
('id\t@id','id="$1"'),
('onBindError\t@onBindError','onBindError="$1"'),
('bind\t@bind','bind="$1"'),
('tagName\t@tagName','tagName="$1"'),
('tagName="div"\ttagName', 'tagName="div"'),
('tagName="span"\ttagName', 'tagName="span"'),
('bindonload\t@bindonload','bindonload="$1"'),
('bindonload="false"\tbindonload', 'bindonload="false"'),
('bindonload="true"\tbindonload', 'bindonload="true"')
],
'cfdocument':
[
('format\t@format','format="$1"'),
('format="pdf"\tformat', 'format="pdf"'),
('format="flashpaper"\tformat', 'format="flashpaper"'),
('filename\t@filename','filename="$1"'),
('overwrite\t@overwrite','overwrite="$1"'),
('overwrite="true"\toverwrite', 'overwrite="true"'),
('overwrite="false"\toverwrite', 'overwrite="false"'),
('name\t@name','name="$1"'),
('pagetype\t@pagetype','pagetype="$1"'),
('pagetype="legal"\tpagetype', 'pagetype="legal"'),
('pagetype="letter"\tpagetype', 'pagetype="letter"'),
('pagetype="a4"\tpagetype', 'pagetype="a4"'),
('pagetype="a5"\tpagetype', 'pagetype="a5"'),
('pagetype="b5"\tpagetype', 'pagetype="b5"'),
('pagetype="custom"\tpagetype', 'pagetype="custom"'),
('pageheight\t@pageheight','pageheight="$1"'),
('pagewidth\t@pagewidth','pagewidth="$1"'),
('orientation\t@orientation','orientation="$1"'),
('orientation="portrait"\torientation', 'orientation="portrait"'),
('orientation="landscape"\torientation', 'orientation="landscape"'),
('margintop\t@margintop','margintop="$1"'),
('marginbottom\t@marginbottom','marginbottom="$1"'),
('marginleft\t@marginleft','marginleft="$1"'),
('marginright\t@marginright','marginright="$1"'),
('unit\t@unit','unit="$1"'),
('unit="in"\tunit', 'unit="in"'),
('unit="cm"\tunit', 'unit="cm"'),
('encryption\t@encryption','encryption="$1"'),
('encryption="128-bit"\tencryption', 'encryption="128-bit"'),
('encryption="40-bit"\tencryption', 'encryption="40-bit"'),
('encryption="none"\tencryption', 'encryption="none"'),
('ownerpassword\t@ownerpassword','ownerpassword="$1"'),
('userpassword\t@userpassword','userpassword="$1"'),
('permissions\t@permissions','permissions="$1"'),
('permissions="allowprinting,allowcopy,allowscreenreaders"\tpermissions', 'permissions="allowprinting,allowcopy,allowscreenreaders"'),
('permissions="allowprinting"\tpermissions', 'permissions="allowprinting"'),
('permissions="allowmodifycontents"\tpermissions', 'permissions="allowmodifycontents"'),
('permissions="allowcopy"\tpermissions', 'permissions="allowcopy"'),
('permissions="allowmodifyannotations"\tpermissions', 'permissions="allowmodifyannotations"'),
('permissions="allowfillin"\tpermissions', 'permissions="allowfillin"'),
('permissions="allowscreenreaders"\tpermissions', 'permissions="allowscreenreaders"'),
('permissions="allowassembly"\tpermissions', 'permissions="allowassembly"'),
('permissions="allowdegradedprinting"\tpermissions', 'permissions="allowdegradedprinting"'),
('permissions="allowprinting,allowmodifycontents,allowcopy,allowmodifyannotations,allowfillin,allowscreenreaders,allowassembly,allowdegradedprinting"\tpermissions', 'permissions="allowprinting,allowmodifycontents,allowcopy,allowmodifyannotations,allowfillin,allowscreenreaders,allowassembly,allowdegradedprinting"'),
('fontembed\t@fontembed','fontembed="$1"'),
('fontembed="true"\tfontembed', 'fontembed="true"'),
('fontembed="false"\tfontembed', 'fontembed="false"'),
('backgroundvisible\t@backgroundvisible','backgroundvisible="$1"'),
('backgroundvisible="true"\tbackgroundvisible', 'backgroundvisible="true"'),
('backgroundvisible="false"\tbackgroundvisible', 'backgroundvisible="false"'),
('scale\t@scale','scale="$1"'),
('scale="100"\tscale', 'scale="100"'),
('scale="90"\tscale', 'scale="90"'),
('scale="80"\tscale', 'scale="80"'),
('scale="70"\tscale', 'scale="70"'),
('scale="60"\tscale', 'scale="60"'),
('scale="50"\tscale', 'scale="50"'),
('scale="40"\tscale', 'scale="40"'),
('scale="30"\tscale', 'scale="30"'),
('scale="20"\tscale', 'scale="20"'),
('scale="10"\tscale', 'scale="10"'),
('authpassword\t@authpassword','authpassword="$1"'),
('authuser\t@authuser','authuser="$1"'),
('bookmark\t@bookmark','bookmark="$1"'),
('bookmark="true"\tbookmark', 'bookmark="true"'),
('bookmark="false"\tbookmark', 'bookmark="false"'),
('localurl\t@localurl','localurl="$1"'),
('localurl="true"\tlocalurl', 'localurl="true"'),
('localurl="false"\tlocalurl', 'localurl="false"'),
('mimetype\t@mimetype','mimetype="$1"'),
('mimetype="text/html"\tmimetype', 'mimetype="text/html"'),
('mimetype="text/plain"\tmimetype', 'mimetype="text/plain"'),
('mimetype="application/xml"\tmimetype', 'mimetype="application/xml"'),
('mimetype="image/bmp"\tmimetype', 'mimetype="image/bmp"'),
('mimetype="image/jpeg"\tmimetype', 'mimetype="image/jpeg"'),
('mimetype="image/png"\tmimetype', 'mimetype="image/png"'),
('mimetype="image/gif"\tmimetype', 'mimetype="image/gif"'),
('proxypassword\t@proxypassword','proxypassword="$1"'),
('proxyuser\t@proxyuser','proxyuser="$1"'),
('saveasname\t@saveasname','saveasname="$1"'),
('src\t@src','src="$1"'),
('srcfile\t@srcfile','srcfile="$1"'),
('useragent\t@useragent','useragent="$1"'),
('proxyhost\t@proxyhost','proxyhost="$1"'),
('proxyport\t@proxyport','proxyport="$1"'),
('tagged\t@tagged','tagged="$1"'),
('tagged="true"\ttagged', 'tagged="true"'),
('tagged="false"\ttagged', 'tagged="false"'),
('pdfa\t@pdfa','pdfa="$1"'),
('pdfa="true"\tpdfa', 'pdfa="true"'),
('pdfa="false"\tpdfa', 'pdfa="false"'),
('formFields\t@formFields','formFields="$1"'),
('formFields="true"\tformFields', 'formFields="true"'),
('formFields="false"\tformFields', 'formFields="false"'),
('formsType\t@formsType','formsType="$1"'),
('formsType="fdf"\tformsType', 'formsType="fdf"'),
('formsType="pdf"\tformsType', 'formsType="pdf"'),
('formsType="html"\tformsType', 'formsType="html"'),
('formsType="xml"\tformsType', 'formsType="xml"'),
('permissionsPassword\t@permissionsPassword','permissionsPassword="$1"'),
('openPassword\t@openPassword','openPassword="$1"')
],
'cfdocumentitem':
[
('type\t@type','type="$1"'),
('type="pagebreak"\ttype', 'type="pagebreak"'),
('type="header"\ttype', 'type="header"'),
('type="footer"\ttype', 'type="footer"'),
('evalAtPrint\t@evalAtPrint','evalAtPrint="$1"'),
('evalAtPrint="true"\tevalAtPrint', 'evalAtPrint="true"'),
('evalAtPrint="false"\tevalAtPrint', 'evalAtPrint="false"')
],
'cfdocumentsection':
[
('margintop\t@margintop','margintop="$1"'),
('marginbottom\t@marginbottom','marginbottom="$1"'),
('marginleft\t@marginleft','marginleft="$1"'),
('marginright\t@marginright','marginright="$1"'),
('authpassword\t@authpassword','authpassword="$1"'),
('authuser\t@authuser','authuser="$1"'),
('mimetype\t@mimetype','mimetype="$1"'),
('mimetype="text/html"\tmimetype', 'mimetype="text/html"'),
('mimetype="text/plain"\tmimetype', 'mimetype="text/plain"'),
('mimetype="application/xml"\tmimetype', 'mimetype="application/xml"'),
('mimetype="image/bmp"\tmimetype', 'mimetype="image/bmp"'),
('mimetype="image/jpeg"\tmimetype', 'mimetype="image/jpeg"'),
('mimetype="image/png"\tmimetype', 'mimetype="image/png"'),
('mimetype="image/gif"\tmimetype', 'mimetype="image/gif"'),
('name\t@name','name="$1"'),
('src\t@src','src="$1"'),
('srcfile\t@srcfile','srcfile="$1"'),
('useragent\t@useragent','useragent="$1"')
],
'cfdump':
[
('var\t@var','var="$1"'),
('expand\t@expand','expand="$1"'),
('expand="true"\texpand', 'expand="true"'),
('expand="false"\texpand', 'expand="false"'),
('format\t@format','format="$1"'),
('format="html"\tformat', 'format="html"'),
('format="text"\tformat', 'format="text"'),
('hide\t@hide','hide="$1"'),
('keys\t@keys','keys="$1"'),
('label\t@label','label="$1"'),
('metainfo\t@metainfo','metainfo="$1"'),
('metainfo="true"\tmetainfo', 'metainfo="true"'),
('metainfo="false"\tmetainfo', 'metainfo="false"'),
('output\t@output','output="$1"'),
('output="browser"\toutput', 'output="browser"'),
('output="console"\toutput', 'output="console"'),
('output="filename"\toutput', 'output="filename"'),
('show\t@show','show="$1"'),
('showUDfs\t@showUDfs','showUDfs="$1"'),
('showUDfs="true"\tshowUDfs', 'showUDfs="true"'),
('showUDfs="false"\tshowUDfs', 'showUDfs="false"'),
('top\t@top','top="$1"'),
('abort\t@abort','abort="$1"'),
('abort="true"\tabort', 'abort="true"'),
('abort="false"\tabort', 'abort="false"')
],
'cfelse':
[

],
'cfelseif':
[

],
'cferror':
[
('type\t@type','type="$1"'),
('type="exception"\ttype', 'type="exception"'),
('type="validation"\ttype', 'type="validation"'),
('type="request"\ttype', 'type="request"'),
('type="monitor"\ttype', 'type="monitor"'),
('template\t@template','template="$1"'),
('mailto\t@mailto','mailto="$1"'),
('exception\t@exception','exception="$1"'),
('exception="any"\texception', 'exception="any"'),
('exception="application"\texception', 'exception="application"'),
('exception="database"\texception', 'exception="database"'),
('exception="template"\texception', 'exception="template"'),
('exception="security"\texception', 'exception="security"'),
('exception="object"\texception', 'exception="object"'),
('exception="missinginclude"\texception', 'exception="missinginclude"'),
('exception="expression"\texception', 'exception="expression"'),
('exception="lock"\texception', 'exception="lock"'),
('exception="custom_type"\texception', 'exception="custom_type"')
],
'cfexecute':
[
('name\t@name','name="$1"'),
('arguments\t@arguments','arguments="$1"'),
('outputfile\t@outputfile','outputfile="$1"'),
('variable\t@variable','variable="$1"'),
('timeout\t@timeout','timeout="$1"'),
('errorVariable\t@errorVariable','errorVariable="$1"'),
('errorFile\t@errorFile','errorFile="$1"')
],
'cfexit':
[
('method\t@method','method="$1"'),
('method="exittag"\tmethod', 'method="exittag"'),
('method="exittemplate"\tmethod', 'method="exittemplate"'),
('method="loop"\tmethod', 'method="loop"')
],
'cffile':
[
('action\t@action','action="$1"'),
('action="append"\taction', 'action="append"'),
('action="copy"\taction', 'action="copy"'),
('action="delete"\taction', 'action="delete"'),
('action="move"\taction', 'action="move"'),
('action="read"\taction', 'action="read"'),
('action="readbinary"\taction', 'action="readbinary"'),
('action="rename"\taction', 'action="rename"'),
('action="upload"\taction', 'action="upload"'),
('action="uploadall"\taction', 'action="uploadall"'),
('action="write"\taction', 'action="write"'),
('file\t@file','file="$1"'),
('mode\t@mode','mode="$1"'),
('output\t@output','output="$1"'),
('addnewline\t@addnewline','addnewline="$1"'),
('addnewline="true"\taddnewline', 'addnewline="true"'),
('addnewline="false"\taddnewline', 'addnewline="false"'),
('attributes\t@attributes','attributes="$1"'),
('attributes="readonly"\tattributes', 'attributes="readonly"'),
('attributes="hidden"\tattributes', 'attributes="hidden"'),
('attributes="normal"\tattributes', 'attributes="normal"'),
('attributes="system"\tattributes', 'attributes="system"'),
('attributes="temporary"\tattributes', 'attributes="temporary"'),
('charset\t@charset','charset="$1"'),
('charset="utf-8"\tcharset', 'charset="utf-8"'),
('charset="iso-8859-1"\tcharset', 'charset="iso-8859-1"'),
('charset="windows-1252"\tcharset', 'charset="windows-1252"'),
('charset="us-ascii"\tcharset', 'charset="us-ascii"'),
('charset="shift_jis"\tcharset', 'charset="shift_jis"'),
('charset="iso-2022-jp"\tcharset', 'charset="iso-2022-jp"'),
('charset="euc-jp"\tcharset', 'charset="euc-jp"'),
('charset="euc-kr"\tcharset', 'charset="euc-kr"'),
('charset="big5"\tcharset', 'charset="big5"'),
('charset="euc-cn"\tcharset', 'charset="euc-cn"'),
('charset="utf-16"\tcharset', 'charset="utf-16"'),
('source\t@source','source="$1"'),
('destination\t@destination','destination="$1"'),
('variable\t@variable','variable="$1"'),
('filefield\t@filefield','filefield="$1"'),
('nameconflict\t@nameconflict','nameconflict="$1"'),
('nameconflict="error"\tnameconflict', 'nameconflict="error"'),
('nameconflict="skip"\tnameconflict', 'nameconflict="skip"'),
('nameconflict="overwrite"\tnameconflict', 'nameconflict="overwrite"'),
('nameconflict="makeunique"\tnameconflict', 'nameconflict="makeunique"'),
('accept\t@accept','accept="$1"'),
('result\t@result','result="$1"'),
('fixnewline\t@fixnewline','fixnewline="$1"'),
('fixnewline="true"\tfixnewline', 'fixnewline="true"'),
('fixnewline="false"\tfixnewline', 'fixnewline="false"'),
('strict\t@strict','strict="$1"'),
('strict="true"\tstrict', 'strict="true"'),
('strict="false"\tstrict', 'strict="false"')
],
'cfflush':
[
('interval\t@interval','interval="$1"')
],
'cfform':
[
('name\t@name','name="$1"'),
('action\t@action','action="$1"'),
('method\t@method','method="$1"'),
('method="post"\tmethod', 'method="post"'),
('method="get"\tmethod', 'method="get"'),
('format\t@format','format="$1"'),
('format="html"\tformat', 'format="html"'),
('format="flash"\tformat', 'format="flash"'),
('format="xml"\tformat', 'format="xml"'),
('skin\t@skin','skin="$1"'),
('skin="halosilver"\tskin', 'skin="halosilver"'),
('skin="haloblue"\tskin', 'skin="haloblue"'),
('skin="halogreen"\tskin', 'skin="halogreen"'),
('skin="haloorange"\tskin', 'skin="haloorange"'),
('skin="beige"\tskin', 'skin="beige"'),
('skin="blue"\tskin', 'skin="blue"'),
('skin="bluegray"\tskin', 'skin="bluegray"'),
('skin="lightgray"\tskin', 'skin="lightgray"'),
('skin="red"\tskin', 'skin="red"'),
('skin="silver"\tskin', 'skin="silver"'),
('skin="none"\tskin', 'skin="none"'),
('skin="default"\tskin', 'skin="default"'),
('skin="basic"\tskin', 'skin="basic"'),
('skin="basiccss"\tskin', 'skin="basiccss"'),
('preservedata\t@preservedata','preservedata="$1"'),
('preservedata="true"\tpreservedata', 'preservedata="true"'),
('preservedata="false"\tpreservedata', 'preservedata="false"'),
('onload\t@onload','onload="$1"'),
('onsubmit\t@onsubmit','onsubmit="$1"'),
('codebase\t@codebase','codebase="$1"'),
('archive\t@archive','archive="$1"'),
('height\t@height','height="$1"'),
('width\t@width','width="$1"'),
('onerror\t@onerror','onerror="$1"'),
('wmode\t@wmode','wmode="$1"'),
('wmode="window"\twmode', 'wmode="window"'),
('wmode="transparent"\twmode', 'wmode="transparent"'),
('wmode="opaque"\twmode', 'wmode="opaque"'),
('accessible\t@accessible','accessible="$1"'),
('accessible="true"\taccessible', 'accessible="true"'),
('accessible="false"\taccessible', 'accessible="false"'),
('preloader\t@preloader','preloader="$1"'),
('preloader="true"\tpreloader', 'preloader="true"'),
('preloader="false"\tpreloader', 'preloader="false"'),
('timeout\t@timeout','timeout="$1"'),
('scriptsrc\t@scriptsrc','scriptsrc="$1"'),
('style\t@style','style="$1"'),
('onreset\t@onreset','onreset="$1"'),
('id\t@id','id="$1"'),
('target\t@target','target="$1"'),
('passthrough\t@passthrough','passthrough="$1"'),
('onsuccess\t@onsuccess','onsuccess="$1"'),
('enctype\t@enctype','enctype="$1"')
],
'cfformgroup':
[
('type\t@type','type="$1"'),
('type="horizontal"\ttype', 'type="horizontal"'),
('type="vertical"\ttype', 'type="vertical"'),
('type="fieldset"\ttype', 'type="fieldset"'),
('type="repeater"\ttype', 'type="repeater"'),
('type="hbox"\ttype', 'type="hbox"'),
('type="vbox"\ttype', 'type="vbox"'),
('type="hdividedbox"\ttype', 'type="hdividedbox"'),
('type="vdividedbox"\ttype', 'type="vdividedbox"'),
('type="panel"\ttype', 'type="panel"'),
('type="tile"\ttype', 'type="tile"'),
('type="accordion"\ttype', 'type="accordion"'),
('type="tabnavigator"\ttype', 'type="tabnavigator"'),
('type="page"\ttype', 'type="page"'),
('query\t@query','query="$1"'),
('startrow\t@startrow','startrow="$1"'),
('maxrows\t@maxrows','maxrows="$1"'),
('label\t@label','label="$1"'),
('id\t@id','id="$1"'),
('style\t@style','style="$1"'),
('selectedindex\t@selectedindex','selectedindex="$1"'),
('width\t@width','width="$1"'),
('height\t@height','height="$1"'),
('enabled\t@enabled','enabled="$1"'),
('enabled="true"\tenabled', 'enabled="true"'),
('enabled="false"\tenabled', 'enabled="false"'),
('visible\t@visible','visible="$1"'),
('visible="true"\tvisible', 'visible="true"'),
('visible="false"\tvisible', 'visible="false"'),
('onchange\t@onchange','onchange="$1"'),
('tooltip\t@tooltip','tooltip="$1"')
],
'cfformitem':
[
('type\t@type','type="$1"'),
('type="html"\ttype', 'type="html"'),
('type="text"\ttype', 'type="text"'),
('type="script"\ttype', 'type="script"'),
('type="spacer"\ttype', 'type="spacer"'),
('type="hrule"\ttype', 'type="hrule"'),
('type="vrule"\ttype', 'type="vrule"'),
('style\t@style','style="$1"'),
('width\t@width','width="$1"'),
('height\t@height','height="$1"'),
('enabled\t@enabled','enabled="$1"'),
('enabled="true"\tenabled', 'enabled="true"'),
('enabled="false"\tenabled', 'enabled="false"'),
('visible\t@visible','visible="$1"'),
('visible="true"\tvisible', 'visible="true"'),
('visible="false"\tvisible', 'visible="false"'),
('tooltip\t@tooltip','tooltip="$1"'),
('bind\t@bind','bind="$1"')
],
'cfftp':
[
('action\t@action','action="$1"'),
('action="open"\taction', 'action="open"'),
('action="close"\taction', 'action="close"'),
('action="changedir"\taction', 'action="changedir"'),
('action="createdir"\taction', 'action="createdir"'),
('action="listdir"\taction', 'action="listdir"'),
('action="removedir"\taction', 'action="removedir"'),
('action="getfile"\taction', 'action="getfile"'),
('action="putfile"\taction', 'action="putfile"'),
('action="rename"\taction', 'action="rename"'),
('action="remove"\taction', 'action="remove"'),
('action="getcurrentdir"\taction', 'action="getcurrentdir"'),
('action="getcurrenturl"\taction', 'action="getcurrenturl"'),
('action="existsdir"\taction', 'action="existsdir"'),
('action="existsfile"\taction', 'action="existsfile"'),
('action="exists"\taction', 'action="exists"'),
('action="quote"\taction', 'action="quote"'),
('action="site"\taction', 'action="site"'),
('action="allo"\taction', 'action="allo"'),
('action="acct"\taction', 'action="acct"'),
('username\t@username','username="$1"'),
('password\t@password','password="$1"'),
('server\t@server','server="$1"'),
('timeout\t@timeout','timeout="$1"'),
('port\t@port','port="$1"'),
('connection\t@connection','connection="$1"'),
('proxyserver\t@proxyserver','proxyserver="$1"'),
('retrycount\t@retrycount','retrycount="$1"'),
('stoponerror\t@stoponerror','stoponerror="$1"'),
('stoponerror="true"\tstoponerror', 'stoponerror="true"'),
('stoponerror="false"\tstoponerror', 'stoponerror="false"'),
('passive\t@passive','passive="$1"'),
('passive="true"\tpassive', 'passive="true"'),
('passive="false"\tpassive', 'passive="false"'),
('transfermode\t@transfermode','transfermode="$1"'),
('transfermode="auto"\ttransfermode', 'transfermode="auto"'),
('transfermode="ascii"\ttransfermode', 'transfermode="ascii"'),
('transfermode="binary"\ttransfermode', 'transfermode="binary"'),
('failifexists\t@failifexists','failifexists="$1"'),
('failifexists="true"\tfailifexists', 'failifexists="true"'),
('failifexists="false"\tfailifexists', 'failifexists="false"'),
('directory\t@directory','directory="$1"'),
('localfile\t@localfile','localfile="$1"'),
('remotefile\t@remotefile','remotefile="$1"'),
('item\t@item','item="$1"'),
('existing\t@existing','existing="$1"'),
('new\t@new','new="$1"'),
('name\t@name','name="$1"'),
('result\t@result','result="$1"'),
('attributes\t@attributes','attributes="$1"'),
('passphrase\t@passphrase','passphrase="$1"'),
('buffersize\t@buffersize','buffersize="$1"'),
('secure\t@secure','secure="$1"'),
('secure="true"\tsecure', 'secure="true"'),
('secure="false"\tsecure', 'secure="false"'),
('asciiextensionlist\t@asciiextensionlist','asciiextensionlist="$1"'),
('key\t@key','key="$1"'),
('actionparam\t@actionparam','actionparam="$1"'),
('fingerprint\t@fingerprint','fingerprint="$1"')
],
'cffunction':
[
('name\t@name','name="$1"'),
('returntype\t@returntype','returntype="$1"'),
('returntype="any"\treturntype', 'returntype="any"'),
('returntype="array"\treturntype', 'returntype="array"'),
('returntype="binary"\treturntype', 'returntype="binary"'),
('returntype="boolean"\treturntype', 'returntype="boolean"'),
('returntype="date"\treturntype', 'returntype="date"'),
('returntype="guid"\treturntype', 'returntype="guid"'),
('returntype="numeric"\treturntype', 'returntype="numeric"'),
('returntype="query"\treturntype', 'returntype="query"'),
('returntype="string"\treturntype', 'returntype="string"'),
('returntype="struct"\treturntype', 'returntype="struct"'),
('returntype="uuid"\treturntype', 'returntype="uuid"'),
('returntype="variablename"\treturntype', 'returntype="variablename"'),
('returntype="void"\treturntype', 'returntype="void"'),
('returntype="xml"\treturntype', 'returntype="xml"'),
('returntype="(component name)"\treturntype', 'returntype="${1:component name}"'),
('roles\t@roles','roles="$1"'),
('access\t@access','access="$1"'),
('access="private"\taccess', 'access="private"'),
('access="package"\taccess', 'access="package"'),
('access="public"\taccess', 'access="public"'),
('access="remote"\taccess', 'access="remote"'),
('output\t@output','output="$1"'),
('output="true"\toutput', 'output="true"'),
('output="false"\toutput', 'output="false"'),
('displayname\t@displayname','displayname="$1"'),
('hint\t@hint','hint="$1"'),
('description\t@description','description="$1"'),
('returnformat\t@returnformat','returnformat="$1"'),
('returnformat="json"\treturnformat', 'returnformat="json"'),
('returnformat="plain"\treturnformat', 'returnformat="plain"'),
('returnformat="wddx"\treturnformat', 'returnformat="wddx"'),
('securejson\t@securejson','securejson="$1"'),
('securejson="true"\tsecurejson', 'securejson="true"'),
('securejson="false"\tsecurejson', 'securejson="false"'),
('verifyclient\t@verifyclient','verifyclient="$1"'),
('verifyclient="true"\tverifyclient', 'verifyclient="true"'),
('verifyclient="false"\tverifyclient', 'verifyclient="false"'),
('restPath\t@restPath','restPath="$1"'),
('httpMethod\t@httpMethod','httpMethod="$1"'),
('httpMethod="get"\thttpMethod', 'httpMethod="get"'),
('httpMethod="post"\thttpMethod', 'httpMethod="post"'),
('httpMethod="put"\thttpMethod', 'httpMethod="put"'),
('httpMethod="delete"\thttpMethod', 'httpMethod="delete"'),
('httpMethod="head"\thttpMethod', 'httpMethod="head"'),
('httpMethod="options"\thttpMethod', 'httpMethod="options"'),
('produces\t@produces','produces="$1"'),
('consumes\t@consumes','consumes="$1"')
],
'cfgrid':
[
('name\t@name','name="$1"'),
('bind\t@bind','bind="$1"'),
('pagesize\t@pagesize','pagesize="$1"'),
('striperowcolor\t@striperowcolor','striperowcolor="$1"'),
('preservepageonsort\t@preservepageonsort','preservepageonsort="$1"'),
('preservepageonsort="true"\tpreservepageonsort', 'preservepageonsort="true"'),
('preservepageonsort="false"\tpreservepageonsort', 'preservepageonsort="false"'),
('striperows\t@striperows','striperows="$1"'),
('striperows="true"\tstriperows', 'striperows="true"'),
('striperows="false"\tstriperows', 'striperows="false"'),
('format\t@format','format="$1"'),
('format="applet"\tformat', 'format="applet"'),
('format="flash"\tformat', 'format="flash"'),
('format="xml"\tformat', 'format="xml"'),
('format="html"\tformat', 'format="html"'),
('height\t@height','height="$1"'),
('width\t@width','width="$1"'),
('autowidth\t@autowidth','autowidth="$1"'),
('autowidth="true"\tautowidth', 'autowidth="true"'),
('autowidth="false"\tautowidth', 'autowidth="false"'),
('vspace\t@vspace','vspace="$1"'),
('hspace\t@hspace','hspace="$1"'),
('align\t@align','align="$1"'),
('align="top"\talign', 'align="top"'),
('align="left"\talign', 'align="left"'),
('align="bottom"\talign', 'align="bottom"'),
('align="baseline"\talign', 'align="baseline"'),
('align="texttop"\talign', 'align="texttop"'),
('align="absbottom"\talign', 'align="absbottom"'),
('align="middle"\talign', 'align="middle"'),
('align="absmiddle"\talign', 'align="absmiddle"'),
('align="right"\talign', 'align="right"'),
('query\t@query','query="$1"'),
('insert\t@insert','insert="$1"'),
('insert="true"\tinsert', 'insert="true"'),
('insert="false"\tinsert', 'insert="false"'),
('delete\t@delete','delete="$1"'),
('delete="true"\tdelete', 'delete="true"'),
('delete="false"\tdelete', 'delete="false"'),
('sort\t@sort','sort="$1"'),
('sort="true"\tsort', 'sort="true"'),
('sort="false"\tsort', 'sort="false"'),
('font\t@font','font="$1"'),
('font="arial"\tfont', 'font="arial"'),
('font="times"\tfont', 'font="times"'),
('font="courier"\tfont', 'font="courier"'),
('font="arialunicodems"\tfont', 'font="arialunicodems"'),
('fontsize\t@fontsize','fontsize="$1"'),
('italic\t@italic','italic="$1"'),
('italic="true"\titalic', 'italic="true"'),
('italic="false"\titalic', 'italic="false"'),
('bold\t@bold','bold="$1"'),
('bold="true"\tbold', 'bold="true"'),
('bold="false"\tbold', 'bold="false"'),
('textcolor\t@textcolor','textcolor="$1"'),
('textcolor="black"\ttextcolor', 'textcolor="black"'),
('textcolor="red"\ttextcolor', 'textcolor="red"'),
('textcolor="blue"\ttextcolor', 'textcolor="blue"'),
('textcolor="magenta"\ttextcolor', 'textcolor="magenta"'),
('textcolor="cyan"\ttextcolor', 'textcolor="cyan"'),
('textcolor="orange"\ttextcolor', 'textcolor="orange"'),
('textcolor="darkgray"\ttextcolor', 'textcolor="darkgray"'),
('textcolor="pink"\ttextcolor', 'textcolor="pink"'),
('textcolor="white"\ttextcolor', 'textcolor="white"'),
('textcolor="lightgray"\ttextcolor', 'textcolor="lightgray"'),
('textcolor="yellow"\ttextcolor', 'textcolor="yellow"'),
('href\t@href','href="$1"'),
('hrefkey\t@hrefkey','hrefkey="$1"'),
('target\t@target','target="$1"'),
('appendkey\t@appendkey','appendkey="$1"'),
('appendkey="true"\tappendkey', 'appendkey="true"'),
('appendkey="false"\tappendkey', 'appendkey="false"'),
('highlighthref\t@highlighthref','highlighthref="$1"'),
('highlighthref="true"\thighlighthref', 'highlighthref="true"'),
('highlighthref="false"\thighlighthref', 'highlighthref="false"'),
('onvalidate\t@onvalidate','onvalidate="$1"'),
('onerror\t@onerror','onerror="$1"'),
('griddataalign\t@griddataalign','griddataalign="$1"'),
('griddataalign="left"\tgriddataalign', 'griddataalign="left"'),
('griddataalign="center"\tgriddataalign', 'griddataalign="center"'),
('griddataalign="right"\tgriddataalign', 'griddataalign="right"'),
('gridlines\t@gridlines','gridlines="$1"'),
('gridlines="true"\tgridlines', 'gridlines="true"'),
('gridlines="false"\tgridlines', 'gridlines="false"'),
('rowheight\t@rowheight','rowheight="$1"'),
('rowheaders\t@rowheaders','rowheaders="$1"'),
('rowheaders="true"\trowheaders', 'rowheaders="true"'),
('rowheaders="false"\trowheaders', 'rowheaders="false"'),
('rowheaderalign\t@rowheaderalign','rowheaderalign="$1"'),
('rowheaderalign="left"\trowheaderalign', 'rowheaderalign="left"'),
('rowheaderalign="center"\trowheaderalign', 'rowheaderalign="center"'),
('rowheaderalign="right"\trowheaderalign', 'rowheaderalign="right"'),
('rowheaderfont\t@rowheaderfont','rowheaderfont="$1"'),
('rowheaderfontsize\t@rowheaderfontsize','rowheaderfontsize="$1"'),
('rowheaderitalic\t@rowheaderitalic','rowheaderitalic="$1"'),
('rowheaderitalic="true"\trowheaderitalic', 'rowheaderitalic="true"'),
('rowheaderitalic="false"\trowheaderitalic', 'rowheaderitalic="false"'),
('rowheaderbold\t@rowheaderbold','rowheaderbold="$1"'),
('rowheaderbold="true"\trowheaderbold', 'rowheaderbold="true"'),
('rowheaderbold="false"\trowheaderbold', 'rowheaderbold="false"'),
('rowheadertextcolor\t@rowheadertextcolor','rowheadertextcolor="$1"'),
('rowheadertextcolor="black"\trowheadertextcolor', 'rowheadertextcolor="black"'),
('rowheadertextcolor="red"\trowheadertextcolor', 'rowheadertextcolor="red"'),
('rowheadertextcolor="blue"\trowheadertextcolor', 'rowheadertextcolor="blue"'),
('rowheadertextcolor="magenta"\trowheadertextcolor', 'rowheadertextcolor="magenta"'),
('rowheadertextcolor="cyan"\trowheadertextcolor', 'rowheadertextcolor="cyan"'),
('rowheadertextcolor="orange"\trowheadertextcolor', 'rowheadertextcolor="orange"'),
('rowheadertextcolor="darkgray"\trowheadertextcolor', 'rowheadertextcolor="darkgray"'),
('rowheadertextcolor="pink"\trowheadertextcolor', 'rowheadertextcolor="pink"'),
('rowheadertextcolor="white"\trowheadertextcolor', 'rowheadertextcolor="white"'),
('rowheadertextcolor="lightgray"\trowheadertextcolor', 'rowheadertextcolor="lightgray"'),
('rowheadertextcolor="yellow"\trowheadertextcolor', 'rowheadertextcolor="yellow"'),
('colheaders\t@colheaders','colheaders="$1"'),
('colheaders="true"\tcolheaders', 'colheaders="true"'),
('colheaders="false"\tcolheaders', 'colheaders="false"'),
('colheaderalign\t@colheaderalign','colheaderalign="$1"'),
('colheaderalign="left"\tcolheaderalign', 'colheaderalign="left"'),
('colheaderalign="center"\tcolheaderalign', 'colheaderalign="center"'),
('colheaderalign="right"\tcolheaderalign', 'colheaderalign="right"'),
('colheaderfont\t@colheaderfont','colheaderfont="$1"'),
('colheaderfontsize\t@colheaderfontsize','colheaderfontsize="$1"'),
('colheaderitalic\t@colheaderitalic','colheaderitalic="$1"'),
('colheaderitalic="true"\tcolheaderitalic', 'colheaderitalic="true"'),
('colheaderitalic="false"\tcolheaderitalic', 'colheaderitalic="false"'),
('colheaderbold\t@colheaderbold','colheaderbold="$1"'),
('colheaderbold="true"\tcolheaderbold', 'colheaderbold="true"'),
('colheaderbold="false"\tcolheaderbold', 'colheaderbold="false"'),
('colheadertextcolor\t@colheadertextcolor','colheadertextcolor="$1"'),
('colheadertextcolor="black"\tcolheadertextcolor', 'colheadertextcolor="black"'),
('colheadertextcolor="red"\tcolheadertextcolor', 'colheadertextcolor="red"'),
('colheadertextcolor="blue"\tcolheadertextcolor', 'colheadertextcolor="blue"'),
('colheadertextcolor="magenta"\tcolheadertextcolor', 'colheadertextcolor="magenta"'),
('colheadertextcolor="cyan"\tcolheadertextcolor', 'colheadertextcolor="cyan"'),
('colheadertextcolor="orange"\tcolheadertextcolor', 'colheadertextcolor="orange"'),
('colheadertextcolor="darkgray"\tcolheadertextcolor', 'colheadertextcolor="darkgray"'),
('colheadertextcolor="pink"\tcolheadertextcolor', 'colheadertextcolor="pink"'),
('colheadertextcolor="white"\tcolheadertextcolor', 'colheadertextcolor="white"'),
('colheadertextcolor="lightgray"\tcolheadertextcolor', 'colheadertextcolor="lightgray"'),
('colheadertextcolor="yellow"\tcolheadertextcolor', 'colheadertextcolor="yellow"'),
('bgcolor\t@bgcolor','bgcolor="$1"'),
('bgcolor="black"\tbgcolor', 'bgcolor="black"'),
('bgcolor="red"\tbgcolor', 'bgcolor="red"'),
('bgcolor="blue"\tbgcolor', 'bgcolor="blue"'),
('bgcolor="magenta"\tbgcolor', 'bgcolor="magenta"'),
('bgcolor="cyan"\tbgcolor', 'bgcolor="cyan"'),
('bgcolor="orange"\tbgcolor', 'bgcolor="orange"'),
('bgcolor="darkgray"\tbgcolor', 'bgcolor="darkgray"'),
('bgcolor="pink"\tbgcolor', 'bgcolor="pink"'),
('bgcolor="white"\tbgcolor', 'bgcolor="white"'),
('bgcolor="lightgray"\tbgcolor', 'bgcolor="lightgray"'),
('bgcolor="yellow"\tbgcolor', 'bgcolor="yellow"'),
('selectcolor\t@selectcolor','selectcolor="$1"'),
('selectcolor="black"\tselectcolor', 'selectcolor="black"'),
('selectcolor="red"\tselectcolor', 'selectcolor="red"'),
('selectcolor="blue"\tselectcolor', 'selectcolor="blue"'),
('selectcolor="magenta"\tselectcolor', 'selectcolor="magenta"'),
('selectcolor="cyan"\tselectcolor', 'selectcolor="cyan"'),
('selectcolor="orange"\tselectcolor', 'selectcolor="orange"'),
('selectcolor="darkgray"\tselectcolor', 'selectcolor="darkgray"'),
('selectcolor="pink"\tselectcolor', 'selectcolor="pink"'),
('selectcolor="white"\tselectcolor', 'selectcolor="white"'),
('selectcolor="lightgray"\tselectcolor', 'selectcolor="lightgray"'),
('selectcolor="yellow"\tselectcolor', 'selectcolor="yellow"'),
('selectmode\t@selectmode','selectmode="$1"'),
('selectmode="edit"\tselectmode', 'selectmode="edit"'),
('selectmode="single"\tselectmode', 'selectmode="single"'),
('selectmode="row"\tselectmode', 'selectmode="row"'),
('selectmode="column"\tselectmode', 'selectmode="column"'),
('selectmode="browse"\tselectmode', 'selectmode="browse"'),
('maxrows\t@maxrows','maxrows="$1"'),
('notsupported\t@notsupported','notsupported="$1"'),
('picturebar\t@picturebar','picturebar="$1"'),
('picturebar="true"\tpicturebar', 'picturebar="true"'),
('picturebar="false"\tpicturebar', 'picturebar="false"'),
('insertbutton\t@insertbutton','insertbutton="$1"'),
('deletebutton\t@deletebutton','deletebutton="$1"'),
('sortascendingbutton\t@sortascendingbutton','sortascendingbutton="$1"'),
('sortdescendingbutton\t@sortdescendingbutton','sortdescendingbutton="$1"'),
('style\t@style','style="$1"'),
('enabled\t@enabled','enabled="$1"'),
('enabled="true"\tenabled', 'enabled="true"'),
('enabled="false"\tenabled', 'enabled="false"'),
('visible\t@visible','visible="$1"'),
('visible="true"\tvisible', 'visible="true"'),
('visible="false"\tvisible', 'visible="false"'),
('tooltip\t@tooltip','tooltip="$1"'),
('onchange\t@onchange','onchange="$1"'),
('bindonload\t@bindonload','bindonload="$1"'),
('bindonload="true"\tbindonload', 'bindonload="true"'),
('bindonload="false"\tbindonload', 'bindonload="false"'),
('selectonload\t@selectonload','selectonload="$1"'),
('selectonload="true"\tselectonload', 'selectonload="true"'),
('selectonload="false"\tselectonload', 'selectonload="false"'),
('onblur\t@onblur','onblur="$1"'),
('onfocus\t@onfocus','onfocus="$1"'),
('collapsible\t@collapsible','collapsible="$1"'),
('groupfield\t@groupfield','groupfield="$1"'),
('onLoad\t@onLoad','onLoad="$1"'),
('multiRowSelect\t@multiRowSelect','multiRowSelect="$1"'),
('multiRowSelect="true"\tmultiRowSelect', 'multiRowSelect="true"'),
('multiRowSelect="false"\tmultiRowSelect', 'multiRowSelect="false"')
],
'cfgridcolumn':
[
('name\t@name','name="$1"'),
('header\t@header','header="$1"'),
('width\t@width','width="$1"'),
('font\t@font','font="$1"'),
('font="arial"\tfont', 'font="arial"'),
('font="times"\tfont', 'font="times"'),
('font="courier"\tfont', 'font="courier"'),
('font="arialunicodems"\tfont', 'font="arialunicodems"'),
('fontsize\t@fontsize','fontsize="$1"'),
('italic\t@italic','italic="$1"'),
('italic="true"\titalic', 'italic="true"'),
('italic="false"\titalic', 'italic="false"'),
('bold\t@bold','bold="$1"'),
('bold="true"\tbold', 'bold="true"'),
('bold="false"\tbold', 'bold="false"'),
('bgcolor\t@bgcolor','bgcolor="$1"'),
('bgcolor="black"\tbgcolor', 'bgcolor="black"'),
('bgcolor="red"\tbgcolor', 'bgcolor="red"'),
('bgcolor="blue"\tbgcolor', 'bgcolor="blue"'),
('bgcolor="magenta"\tbgcolor', 'bgcolor="magenta"'),
('bgcolor="cyan"\tbgcolor', 'bgcolor="cyan"'),
('bgcolor="orange"\tbgcolor', 'bgcolor="orange"'),
('bgcolor="darkgray"\tbgcolor', 'bgcolor="darkgray"'),
('bgcolor="pink"\tbgcolor', 'bgcolor="pink"'),
('bgcolor="white"\tbgcolor', 'bgcolor="white"'),
('bgcolor="lightgray"\tbgcolor', 'bgcolor="lightgray"'),
('bgcolor="yellow"\tbgcolor', 'bgcolor="yellow"'),
('textcolor\t@textcolor','textcolor="$1"'),
('textcolor="black"\ttextcolor', 'textcolor="black"'),
('textcolor="red"\ttextcolor', 'textcolor="red"'),
('textcolor="blue"\ttextcolor', 'textcolor="blue"'),
('textcolor="magenta"\ttextcolor', 'textcolor="magenta"'),
('textcolor="cyan"\ttextcolor', 'textcolor="cyan"'),
('textcolor="orange"\ttextcolor', 'textcolor="orange"'),
('textcolor="darkgray"\ttextcolor', 'textcolor="darkgray"'),
('textcolor="pink"\ttextcolor', 'textcolor="pink"'),
('textcolor="white"\ttextcolor', 'textcolor="white"'),
('textcolor="lightgray"\ttextcolor', 'textcolor="lightgray"'),
('textcolor="yellow"\ttextcolor', 'textcolor="yellow"'),
('href\t@href','href="$1"'),
('hrefkey\t@hrefkey','hrefkey="$1"'),
('target\t@target','target="$1"'),
('select\t@select','select="$1"'),
('select="true"\tselect', 'select="true"'),
('select="false"\tselect', 'select="false"'),
('display\t@display','display="$1"'),
('display="true"\tdisplay', 'display="true"'),
('display="false"\tdisplay', 'display="false"'),
('type\t@type','type="$1"'),
('type="string_nocase"\ttype', 'type="string_nocase"'),
('type="boolean"\ttype', 'type="boolean"'),
('type="numeric"\ttype', 'type="numeric"'),
('type="date"\ttype', 'type="date"'),
('type="combobox"\ttype', 'type="combobox"'),
('type="image"\ttype', 'type="image"'),
('headerfont\t@headerfont','headerfont="$1"'),
('headerfontsize\t@headerfontsize','headerfontsize="$1"'),
('headeritalic\t@headeritalic','headeritalic="$1"'),
('headeritalic="true"\theaderitalic', 'headeritalic="true"'),
('headeritalic="false"\theaderitalic', 'headeritalic="false"'),
('headerbold\t@headerbold','headerbold="$1"'),
('headerbold="true"\theaderbold', 'headerbold="true"'),
('headerbold="false"\theaderbold', 'headerbold="false"'),
('headertextcolor\t@headertextcolor','headertextcolor="$1"'),
('headertextcolor="black"\theadertextcolor', 'headertextcolor="black"'),
('headertextcolor="red"\theadertextcolor', 'headertextcolor="red"'),
('headertextcolor="blue"\theadertextcolor', 'headertextcolor="blue"'),
('headertextcolor="magenta"\theadertextcolor', 'headertextcolor="magenta"'),
('headertextcolor="cyan"\theadertextcolor', 'headertextcolor="cyan"'),
('headertextcolor="orange"\theadertextcolor', 'headertextcolor="orange"'),
('headertextcolor="darkgray"\theadertextcolor', 'headertextcolor="darkgray"'),
('headertextcolor="pink"\theadertextcolor', 'headertextcolor="pink"'),
('headertextcolor="white"\theadertextcolor', 'headertextcolor="white"'),
('headertextcolor="lightgray"\theadertextcolor', 'headertextcolor="lightgray"'),
('headertextcolor="yellow"\theadertextcolor', 'headertextcolor="yellow"'),
('dataalign\t@dataalign','dataalign="$1"'),
('dataalign="left"\tdataalign', 'dataalign="left"'),
('dataalign="right"\tdataalign', 'dataalign="right"'),
('dataalign="center"\tdataalign', 'dataalign="center"'),
('headeralign\t@headeralign','headeralign="$1"'),
('headeralign="left"\theaderalign', 'headeralign="left"'),
('headeralign="right"\theaderalign', 'headeralign="right"'),
('headeralign="center"\theaderalign', 'headeralign="center"'),
('numberformat\t@numberformat','numberformat="$1"'),
('values\t@values','values="$1"'),
('valuesdisplay\t@valuesdisplay','valuesdisplay="$1"'),
('valuesdelimiter\t@valuesdelimiter','valuesdelimiter="$1"'),
('valuesdelimiter=","\tvaluesdelimiter', 'valuesdelimiter=","'),
('valuesdelimiter=";"\tvaluesdelimiter', 'valuesdelimiter=";"'),
('valuesdelimiter="|"\tvaluesdelimiter', 'valuesdelimiter="|"'),
('valuesdelimiter=":"\tvaluesdelimiter', 'valuesdelimiter=":"'),
('mask\t@mask','mask="$1"'),
('headerIcon\t@headerIcon','headerIcon="$1"'),
('autoExpand\t@autoExpand','autoExpand="$1"'),
('autoExpand="true"\tautoExpand', 'autoExpand="true"'),
('autoExpand="false"\tautoExpand', 'autoExpand="false"'),
('headerMenu\t@headerMenu','headerMenu="$1"'),
('headerMenu="true"\theaderMenu', 'headerMenu="true"'),
('headerMenu="false"\theaderMenu', 'headerMenu="false"')
],
'cfgridrow':
[
('data\t@data','data="$1"'),
('delimiter\t@delimiter','delimiter="$1"')
],
'cfgridupdate':
[
('grid\t@grid','grid="$1"'),
('datasource\t@datasource','datasource="$1"'),
('tablename\t@tablename','tablename="$1"'),
('username\t@username','username="$1"'),
('password\t@password','password="$1"'),
('tableowner\t@tableowner','tableowner="$1"'),
('tablequalifier\t@tablequalifier','tablequalifier="$1"'),
('keyonly\t@keyonly','keyonly="$1"'),
('keyonly="true"\tkeyonly', 'keyonly="true"'),
('keyonly="false"\tkeyonly', 'keyonly="false"'),
('clientinfo\t@clientinfo','clientinfo="$1"')
],
'cfheader':
[
('name\t@name','name="$1"'),
('value\t@value','value="$1"'),
('charset\t@charset','charset="$1"'),
('charset="utf-8"\tcharset', 'charset="utf-8"'),
('charset="iso-8859-1"\tcharset', 'charset="iso-8859-1"'),
('charset="windows-1252"\tcharset', 'charset="windows-1252"'),
('charset="us-ascii"\tcharset', 'charset="us-ascii"'),
('charset="shift_jis"\tcharset', 'charset="shift_jis"'),
('charset="iso-2022-jp"\tcharset', 'charset="iso-2022-jp"'),
('charset="euc-jp"\tcharset', 'charset="euc-jp"'),
('charset="euc-kr"\tcharset', 'charset="euc-kr"'),
('charset="big5"\tcharset', 'charset="big5"'),
('charset="euc-cn"\tcharset', 'charset="euc-cn"'),
('charset="utf-16"\tcharset', 'charset="utf-16"'),
('statuscode\t@statuscode','statuscode="$1"'),
('statustext\t@statustext','statustext="$1"')
],
'cfhtmlhead':
[
('text\t@text','text="$1"')
],
'cfhttp':
[
('url\t@url','url="$1"'),
('port\t@port','port="$1"'),
('method\t@method','method="$1"'),
('method="get"\tmethod', 'method="get"'),
('method="post"\tmethod', 'method="post"'),
('method="put"\tmethod', 'method="put"'),
('method="delete"\tmethod', 'method="delete"'),
('method="head"\tmethod', 'method="head"'),
('method="trace"\tmethod', 'method="trace"'),
('method="options"\tmethod', 'method="options"'),
('proxyserver\t@proxyserver','proxyserver="$1"'),
('proxyport\t@proxyport','proxyport="$1"'),
('proxyuser\t@proxyuser','proxyuser="$1"'),
('proxypassword\t@proxypassword','proxypassword="$1"'),
('username\t@username','username="$1"'),
('password\t@password','password="$1"'),
('useragent\t@useragent','useragent="$1"'),
('charset\t@charset','charset="$1"'),
('charset="utf-8"\tcharset', 'charset="utf-8"'),
('charset="iso-8859-1"\tcharset', 'charset="iso-8859-1"'),
('charset="windows-1252"\tcharset', 'charset="windows-1252"'),
('charset="us-ascii"\tcharset', 'charset="us-ascii"'),
('charset="shift_jis"\tcharset', 'charset="shift_jis"'),
('charset="iso-2022-jp"\tcharset', 'charset="iso-2022-jp"'),
('charset="euc-jp"\tcharset', 'charset="euc-jp"'),
('charset="euc-kr"\tcharset', 'charset="euc-kr"'),
('charset="big5"\tcharset', 'charset="big5"'),
('charset="euc-cn"\tcharset', 'charset="euc-cn"'),
('charset="utf-16"\tcharset', 'charset="utf-16"'),
('resolveurl\t@resolveurl','resolveurl="$1"'),
('resolveurl="true"\tresolveurl', 'resolveurl="true"'),
('resolveurl="false"\tresolveurl', 'resolveurl="false"'),
('throwonerror\t@throwonerror','throwonerror="$1"'),
('throwonerror="true"\tthrowonerror', 'throwonerror="true"'),
('throwonerror="false"\tthrowonerror', 'throwonerror="false"'),
('redirect\t@redirect','redirect="$1"'),
('redirect="true"\tredirect', 'redirect="true"'),
('redirect="false"\tredirect', 'redirect="false"'),
('timeout\t@timeout','timeout="$1"'),
('getasbinary\t@getasbinary','getasbinary="$1"'),
('getasbinary="auto"\tgetasbinary', 'getasbinary="auto"'),
('getasbinary="yes"\tgetasbinary', 'getasbinary="yes"'),
('getasbinary="no"\tgetasbinary', 'getasbinary="no"'),
('getasbinary="never"\tgetasbinary', 'getasbinary="never"'),
('result\t@result','result="$1"'),
('delimiter\t@delimiter','delimiter="$1"'),
('delimiter=","\tdelimiter', 'delimiter=","'),
('delimiter=";"\tdelimiter', 'delimiter=";"'),
('delimiter="|"\tdelimiter', 'delimiter="|"'),
('delimiter=":"\tdelimiter', 'delimiter=":"'),
('name\t@name','name="$1"'),
('columns\t@columns','columns="$1"'),
('firstrowasheaders\t@firstrowasheaders','firstrowasheaders="$1"'),
('firstrowasheaders="true"\tfirstrowasheaders', 'firstrowasheaders="true"'),
('firstrowasheaders="false"\tfirstrowasheaders', 'firstrowasheaders="false"'),
('textqualifier\t@textqualifier','textqualifier="$1"'),
('textqualifier="""\ttextqualifier', 'textqualifier="""'),
('textqualifier="\'"\ttextqualifier', 'textqualifier="\'"'),
('file\t@file','file="$1"'),
('multipart\t@multipart','multipart="$1"'),
('multipart="false"\tmultipart', 'multipart="false"'),
('multipart="true"\tmultipart', 'multipart="true"'),
('clientcertpassword\t@clientcertpassword','clientcertpassword="$1"'),
('path\t@path','path="$1"'),
('clientcert\t@clientcert','clientcert="$1"'),
('compression\t@compression','compression="$1"'),
('multiparttype\t@multiparttype','multiparttype="$1"')
],
'cfhttpparam':
[
('type\t@type','type="$1"'),
('type="header"\ttype', 'type="header"'),
('type="body"\ttype', 'type="body"'),
('type="xml"\ttype', 'type="xml"'),
('type="cgi"\ttype', 'type="cgi"'),
('type="file"\ttype', 'type="file"'),
('type="url"\ttype', 'type="url"'),
('type="formfield"\ttype', 'type="formfield"'),
('type="cookie"\ttype', 'type="cookie"'),
('name\t@name','name="$1"'),
('value\t@value','value="$1"'),
('file\t@file','file="$1"'),
('encoded\t@encoded','encoded="$1"'),
('encoded="true"\tencoded', 'encoded="true"'),
('encoded="false"\tencoded', 'encoded="false"'),
('mimetype\t@mimetype','mimetype="$1"'),
('mimetype="text/plain"\tmimetype', 'mimetype="text/plain"'),
('mimetype="text/html"\tmimetype', 'mimetype="text/html"')
],
'cfif':
[

],
'cffinally':
[

],
'cfcontinue':
[

],
'cfimap':
[
('password\t@password','password="$1"'),
('secure\t@secure','secure="$1"'),
('secure="true"\tsecure', 'secure="true"'),
('secure="false"\tsecure', 'secure="false"'),
('action\t@action','action="$1"'),
('action="createfolder"\taction', 'action="createfolder"'),
('action="open"\taction', 'action="open"'),
('action="close"\taction', 'action="close"'),
('action="getall"\taction', 'action="getall"'),
('action="markread"\taction', 'action="markread"'),
('action="listallfolders"\taction', 'action="listallfolders"'),
('action="getheaderonly"\taction', 'action="getheaderonly"'),
('action="deletefolder"\taction', 'action="deletefolder"'),
('action="delete"\taction', 'action="delete"'),
('action="renamefolder"\taction', 'action="renamefolder"'),
('action="movemail"\taction', 'action="movemail"'),
('timeout\t@timeout','timeout="$1"'),
('messageNumber\t@messageNumber','messageNumber="$1"'),
('connection\t@connection','connection="$1"'),
('newFolder\t@newFolder','newFolder="$1"'),
('uid\t@uid','uid="$1"'),
('folder\t@folder','folder="$1"'),
('port\t@port','port="$1"'),
('stoponerror\t@stoponerror','stoponerror="$1"'),
('stoponerror="true"\tstoponerror', 'stoponerror="true"'),
('stoponerror="false"\tstoponerror', 'stoponerror="false"'),
('generateUniqueFileNames\t@generateUniqueFileNames','generateUniqueFileNames="$1"'),
('generateUniqueFileNames="true"\tgenerateUniqueFileNames', 'generateUniqueFileNames="true"'),
('generateUniqueFileNames="false"\tgenerateUniqueFileNames', 'generateUniqueFileNames="false"'),
('maxrows\t@maxrows','maxrows="$1"'),
('username\t@username','username="$1"'),
('startRow\t@startRow','startRow="$1"'),
('attachmentpath\t@attachmentpath','attachmentpath="$1"'),
('server\t@server','server="$1"'),
('name\t@name','name="$1"'),
('recurse\t@recurse','recurse="$1"'),
('recurse="true"\trecurse', 'recurse="true"'),
('recurse="false"\trecurse', 'recurse="false"')
],
'cfimport':
[
('taglib\t@taglib','taglib="$1"'),
('prefix\t@prefix','prefix="$1"'),
('path\t@path','path="$1"')
],
'cfinclude':
[
('template\t@template','template="$1"'),
('runonce\t@runonce','runonce="$1"'),
('runonce="true"\trunonce', 'runonce="true"'),
('runonce="false"\trunonce', 'runonce="false"')
],
'cfindex':
[
('collection\t@collection','collection="$1"'),
('action\t@action','action="$1"'),
('action="abort"\taction', 'action="abort"'),
('action="commit"\taction', 'action="commit"'),
('action="delete"\taction', 'action="delete"'),
('action="deltaimport"\taction', 'action="deltaimport"'),
('action="fullimport"\taction', 'action="fullimport"'),
('action="purge"\taction', 'action="purge"'),
('action="refresh"\taction', 'action="refresh"'),
('action="status"\taction', 'action="status"'),
('action="update"\taction', 'action="update"'),
('type\t@type','type="$1"'),
('type="file"\ttype', 'type="file"'),
('type="path"\ttype', 'type="path"'),
('type="custom"\ttype', 'type="custom"'),
('type="dih"\ttype', 'type="dih"'),
('title\t@title','title="$1"'),
('key\t@key','key="$1"'),
('body\t@body','body="$1"'),
('custom1\t@custom1','custom1="$1"'),
('custom2\t@custom2','custom2="$1"'),
('custom3\t@custom3','custom3="$1"'),
('custom4\t@custom4','custom4="$1"'),
('category\t@category','category="$1"'),
('categoryTree\t@categoryTree','categoryTree="$1"'),
('urlpath\t@urlpath','urlpath="$1"'),
('extensions\t@extensions','extensions="$1"'),
('query\t@query','query="$1"'),
('recurse\t@recurse','recurse="$1"'),
('recurse="true"\trecurse', 'recurse="true"'),
('recurse="false"\trecurse', 'recurse="false"'),
('language\t@language','language="$1"'),
('status\t@status','status="$1"'),
('prefix\t@prefix','prefix="$1"'),
('docboost\t@docboost','docboost="$1"'),
('fieldboost\t@fieldboost','fieldboost="$1"'),
('autocommit\t@autocommit','autocommit="$1"'),
('autocommit="true"\tautocommit', 'autocommit="true"'),
('autocommit="false"\tautocommit', 'autocommit="false"')
],
'cfinput':
[
('name\t@name','name="$1"'),
('autosuggest\t@autosuggest','autosuggest="$1"'),
('autoSuggestBindDelay\t@autoSuggestBindDelay','autoSuggestBindDelay="$1"'),
('autoSuggestMinLength\t@autoSuggestMinLength','autoSuggestMinLength="$1"'),
('bindAttribute\t@bindAttribute','bindAttribute="$1"'),
('bindonload\t@bindonload','bindonload="$1"'),
('bindonload="true"\tbindonload', 'bindonload="true"'),
('bindonload="false"\tbindonload', 'bindonload="false"'),
('id\t@id','id="$1"'),
('type\t@type','type="$1"'),
('type="button"\ttype', 'type="button"'),
('type="checkbox"\ttype', 'type="checkbox"'),
('type="file"\ttype', 'type="file"'),
('type="hidden"\ttype', 'type="hidden"'),
('type="image"\ttype', 'type="image"'),
('type="password"\ttype', 'type="password"'),
('type="radio"\ttype', 'type="radio"'),
('type="reset"\ttype', 'type="reset"'),
('type="submit"\ttype', 'type="submit"'),
('type="text"\ttype', 'type="text"'),
('type="datefield"\ttype', 'type="datefield"'),
('type="autosuggest"\ttype', 'type="autosuggest"'),
('label\t@label','label="$1"'),
('style\t@style','style="$1"'),
('class\t@class','class="$1"'),
('required\t@required','required="$1"'),
('required="true"\trequired', 'required="true"'),
('required="false"\trequired', 'required="false"'),
('mask\t@mask','mask="$1"'),
('validate\t@validate','validate="$1"'),
('validate="date"\tvalidate', 'validate="date"'),
('validate="eurodate"\tvalidate', 'validate="eurodate"'),
('validate="time"\tvalidate', 'validate="time"'),
('validate="float"\tvalidate', 'validate="float"'),
('validate="integer"\tvalidate', 'validate="integer"'),
('validate="telephone"\tvalidate', 'validate="telephone"'),
('validate="zipcode"\tvalidate', 'validate="zipcode"'),
('validate="creditcard"\tvalidate', 'validate="creditcard"'),
('validate="social_security_number"\tvalidate', 'validate="social_security_number"'),
('validate="regular_expression"\tvalidate', 'validate="regular_expression"'),
('validateat\t@validateat','validateat="$1"'),
('validateat="onsubmit"\tvalidateat', 'validateat="onsubmit"'),
('validateat="onserver"\tvalidateat', 'validateat="onserver"'),
('validateat="onblur"\tvalidateat', 'validateat="onblur"'),
('message\t@message','message="$1"'),
('range\t@range','range="$1"'),
('maxlength\t@maxlength','maxlength="$1"'),
('pattern\t@pattern','pattern="$1"'),
('onvalidate\t@onvalidate','onvalidate="$1"'),
('onerror\t@onerror','onerror="$1"'),
('size\t@size','size="$1"'),
('value\t@value','value="$1"'),
('bind\t@bind','bind="$1"'),
('checked\t@checked','checked="$1"'),
('checked="true"\tchecked', 'checked="true"'),
('checked="false"\tchecked', 'checked="false"'),
('disabled\t@disabled','disabled="$1"'),
('disabled="true"\tdisabled', 'disabled="true"'),
('disabled="false"\tdisabled', 'disabled="false"'),
('src\t@src','src="$1"'),
('onkeyup\t@onkeyup','onkeyup="$1"'),
('onkeydown\t@onkeydown','onkeydown="$1"'),
('onmouseup\t@onmouseup','onmouseup="$1"'),
('onmousedown\t@onmousedown','onmousedown="$1"'),
('onchange\t@onchange','onchange="$1"'),
('onclick\t@onclick','onclick="$1"'),
('daynames\t@daynames','daynames="$1"'),
('daynames="s"\tdaynames', 'daynames="s"'),
('daynames="m"\tdaynames', 'daynames="m"'),
('daynames="t"\tdaynames', 'daynames="t"'),
('daynames="w"\tdaynames', 'daynames="w"'),
('daynames="th"\tdaynames', 'daynames="th"'),
('daynames="f"\tdaynames', 'daynames="f"'),
('daynames="sa"\tdaynames', 'daynames="sa"'),
('daynames="sunday"\tdaynames', 'daynames="sunday"'),
('daynames="monday"\tdaynames', 'daynames="monday"'),
('daynames="tuesday"\tdaynames', 'daynames="tuesday"'),
('daynames="wednesday"\tdaynames', 'daynames="wednesday"'),
('daynames="thursday"\tdaynames', 'daynames="thursday"'),
('daynames="friday"\tdaynames', 'daynames="friday"'),
('daynames="saturday"\tdaynames', 'daynames="saturday"'),
('daynames="sun"\tdaynames', 'daynames="sun"'),
('daynames="mon"\tdaynames', 'daynames="mon"'),
('daynames="tue"\tdaynames', 'daynames="tue"'),
('daynames="wed"\tdaynames', 'daynames="wed"'),
('daynames="thu"\tdaynames', 'daynames="thu"'),
('daynames="fri"\tdaynames', 'daynames="fri"'),
('daynames="sat"\tdaynames', 'daynames="sat"'),
('firstdayofweek\t@firstdayofweek','firstdayofweek="$1"'),
('firstdayofweek="0"\tfirstdayofweek', 'firstdayofweek="0"'),
('firstdayofweek="1"\tfirstdayofweek', 'firstdayofweek="1"'),
('firstdayofweek="2"\tfirstdayofweek', 'firstdayofweek="2"'),
('firstdayofweek="3"\tfirstdayofweek', 'firstdayofweek="3"'),
('firstdayofweek="4"\tfirstdayofweek', 'firstdayofweek="4"'),
('firstdayofweek="5"\tfirstdayofweek', 'firstdayofweek="5"'),
('firstdayofweek="6"\tfirstdayofweek', 'firstdayofweek="6"'),
('monthnames\t@monthnames','monthnames="$1"'),
('monthnames="january"\tmonthnames', 'monthnames="january"'),
('monthnames="february"\tmonthnames', 'monthnames="february"'),
('monthnames="march"\tmonthnames', 'monthnames="march"'),
('monthnames="april"\tmonthnames', 'monthnames="april"'),
('monthnames="may"\tmonthnames', 'monthnames="may"'),
('monthnames="june"\tmonthnames', 'monthnames="june"'),
('monthnames="july"\tmonthnames', 'monthnames="july"'),
('monthnames="august"\tmonthnames', 'monthnames="august"'),
('monthnames="september"\tmonthnames', 'monthnames="september"'),
('monthnames="october"\tmonthnames', 'monthnames="october"'),
('monthnames="november"\tmonthnames', 'monthnames="november"'),
('monthnames="december"\tmonthnames', 'monthnames="december"'),
('monthnames="jan"\tmonthnames', 'monthnames="jan"'),
('monthnames="feb"\tmonthnames', 'monthnames="feb"'),
('monthnames="mar"\tmonthnames', 'monthnames="mar"'),
('monthnames="apr"\tmonthnames', 'monthnames="apr"'),
('monthnames="may"\tmonthnames', 'monthnames="may"'),
('monthnames="jun"\tmonthnames', 'monthnames="jun"'),
('monthnames="jul"\tmonthnames', 'monthnames="jul"'),
('monthnames="aug"\tmonthnames', 'monthnames="aug"'),
('monthnames="sep"\tmonthnames', 'monthnames="sep"'),
('monthnames="oct"\tmonthnames', 'monthnames="oct"'),
('monthnames="nov"\tmonthnames', 'monthnames="nov"'),
('monthnames="dec"\tmonthnames', 'monthnames="dec"'),
('enabled\t@enabled','enabled="$1"'),
('enabled="true"\tenabled', 'enabled="true"'),
('enabled="false"\tenabled', 'enabled="false"'),
('visible\t@visible','visible="$1"'),
('visible="true"\tvisible', 'visible="true"'),
('visible="false"\tvisible', 'visible="false"'),
('tooltip\t@tooltip','tooltip="$1"'),
('width\t@width','width="$1"'),
('height\t@height','height="$1"'),
('passthrough\t@passthrough','passthrough="$1"'),
('delimiter\t@delimiter','delimiter="$1"'),
('maxresultsdisplayed\t@maxresultsdisplayed','maxresultsdisplayed="$1"'),
('onbinderror\t@onbinderror','onbinderror="$1"'),
('showautosuggestloadingicon\t@showautosuggestloadingicon','showautosuggestloadingicon="$1"'),
('showautosuggestloadingicon="true"\tshowautosuggestloadingicon', 'showautosuggestloadingicon="true"'),
('showautosuggestloadingicon="false"\tshowautosuggestloadingicon', 'showautosuggestloadingicon="false"'),
('sourcefortooltip\t@sourcefortooltip','sourcefortooltip="$1"'),
('typeahead\t@typeahead','typeahead="$1"'),
('typeahead="true"\ttypeahead', 'typeahead="true"'),
('typeahead="false"\ttypeahead', 'typeahead="false"'),
('matchContains\t@matchContains','matchContains="$1"'),
('matchContains="true"\tmatchContains', 'matchContains="true"'),
('matchContains="false"\tmatchContains', 'matchContains="false"')
],
'cfinsert':
[
('datasource\t@datasource','datasource="$1"'),
('tablename\t@tablename','tablename="$1"'),
('tableowner\t@tableowner','tableowner="$1"'),
('tablequalifier\t@tablequalifier','tablequalifier="$1"'),
('username\t@username','username="$1"'),
('password\t@password','password="$1"'),
('formfields\t@formfields','formfields="$1"'),
('providerdsn\t@providerdsn','providerdsn="$1"'),
('dbtype\t@dbtype','dbtype="$1"'),
('dbname\t@dbname','dbname="$1"'),
('dbserver\t@dbserver','dbserver="$1"'),
('provider\t@provider','provider="$1"'),
('fetchclientinfo\t@fetchclientinfo','fetchclientinfo="$1"'),
('clientinfo\t@clientinfo','clientinfo="$1"')
],
'cfinvoke':
[
('component\t@component','component="$1"'),
('method\t@method','method="$1"'),
('returnvariable\t@returnvariable','returnvariable="$1"'),
('argumentcollection\t@argumentcollection','argumentcollection="$1"'),
('username\t@username','username="$1"'),
('password\t@password','password="$1"'),
('webservice\t@webservice','webservice="$1"'),
('timeout\t@timeout','timeout="$1"'),
('proxyserver\t@proxyserver','proxyserver="$1"'),
('proxyport\t@proxyport','proxyport="$1"'),
('proxyuser\t@proxyuser','proxyuser="$1"'),
('proxypassword\t@proxypassword','proxypassword="$1"'),
('serviceport\t@serviceport','serviceport="$1"'),
('refreshwsdl\t@refreshwsdl','refreshwsdl="$1"'),
('refreshwsdl="true"\trefreshwsdl', 'refreshwsdl="true"'),
('refreshwsdl="false"\trefreshwsdl', 'refreshwsdl="false"'),
('wsdl2javaargs\t@wsdl2javaargs','wsdl2javaargs="$1"'),
('wsversion\t@wsversion','wsversion="$1"'),
('wsversion="1"\twsversion', 'wsversion="1"'),
('wsversion="2"\twsversion', 'wsversion="2"')
],
'cfinvokeargument':
[
('name\t@name','name="$1"'),
('value\t@value','value="$1"'),
('omit\t@omit','omit="$1"'),
('omit="true"\tomit', 'omit="true"'),
('omit="false"\tomit', 'omit="false"')
],
'cflayout':
[
('type\t@type','type="$1"'),
('type="accordion"\ttype', 'type="accordion"'),
('type="border"\ttype', 'type="border"'),
('type="hbox"\ttype', 'type="hbox"'),
('type="tab"\ttype', 'type="tab"'),
('type="vbox"\ttype', 'type="vbox"'),
('align\t@align','align="$1"'),
('align="center"\talign', 'align="center"'),
('align="justify"\talign', 'align="justify"'),
('align="left"\talign', 'align="left"'),
('align="right"\talign', 'align="right"'),
('name\t@name','name="$1"'),
('padding\t@padding','padding="$1"'),
('style\t@style','style="$1"'),
('tabheight\t@tabheight','tabheight="$1"'),
('tabposition\t@tabposition','tabposition="$1"'),
('tabposition="top"\ttabposition', 'tabposition="top"'),
('tabposition="bottom"\ttabposition', 'tabposition="bottom"'),
('titlecollapse\t@titlecollapse','titlecollapse="$1"'),
('titlecollapse="true"\ttitlecollapse', 'titlecollapse="true"'),
('titlecollapse="false"\ttitlecollapse', 'titlecollapse="false"'),
('activeontop\t@activeontop','activeontop="$1"'),
('activeontop="true"\tactiveontop', 'activeontop="true"'),
('activeontop="false"\tactiveontop', 'activeontop="false"'),
('fillheight\t@fillheight','fillheight="$1"'),
('fillheight="true"\tfillheight', 'fillheight="true"'),
('fillheight="false"\tfillheight', 'fillheight="false"'),
('fitToWindow\t@fitToWindow','fitToWindow="$1"'),
('fitToWindow="true"\tfitToWindow', 'fitToWindow="true"'),
('fitToWindow="false"\tfitToWindow', 'fitToWindow="false"'),
('height\t@height','height="$1"'),
('width\t@width','width="$1"'),
('buttonStyle\t@buttonStyle','buttonStyle="$1"'),
('tabstrip\t@tabstrip','tabstrip="$1"')
],
'cflayoutarea':
[
('position\t@position','position="$1"'),
('position="bottom"\tposition', 'position="bottom"'),
('position="center"\tposition', 'position="center"'),
('position="left"\tposition', 'position="left"'),
('position="right"\tposition', 'position="right"'),
('position="top"\tposition', 'position="top"'),
('align\t@align','align="$1"'),
('align="center"\talign', 'align="center"'),
('align="justify"\talign', 'align="justify"'),
('align="left"\talign', 'align="left"'),
('align="right"\talign', 'align="right"'),
('closable\t@closable','closable="$1"'),
('closable="true"\tclosable', 'closable="true"'),
('closable="false"\tclosable', 'closable="false"'),
('collapsible\t@collapsible','collapsible="$1"'),
('collapsible="true"\tcollapsible', 'collapsible="true"'),
('collapsible="false"\tcollapsible', 'collapsible="false"'),
('disabled\t@disabled','disabled="$1"'),
('disabled="true"\tdisabled', 'disabled="true"'),
('disabled="false"\tdisabled', 'disabled="false"'),
('initCollapsed\t@initCollapsed','initCollapsed="$1"'),
('initCollapsed="true"\tinitCollapsed', 'initCollapsed="true"'),
('initCollapsed="false"\tinitCollapsed', 'initCollapsed="false"'),
('initHide\t@initHide','initHide="$1"'),
('initHide="true"\tinitHide', 'initHide="true"'),
('initHide="false"\tinitHide', 'initHide="false"'),
('maxSize\t@maxSize','maxSize="$1"'),
('minSize\t@minSize','minSize="$1"'),
('name\t@name','name="$1"'),
('onBindError\t@onBindError','onBindError="$1"'),
('overflow\t@overflow','overflow="$1"'),
('overflow="auto"\toverflow', 'overflow="auto"'),
('overflow="hidden"\toverflow', 'overflow="hidden"'),
('overflow="scroll"\toverflow', 'overflow="scroll"'),
('overflow="visible"\toverflow', 'overflow="visible"'),
('selected\t@selected','selected="$1"'),
('selected="true"\tselected', 'selected="true"'),
('selected="false"\tselected', 'selected="false"'),
('size\t@size','size="$1"'),
('source\t@source','source="$1"'),
('splitter\t@splitter','splitter="$1"'),
('splitter="true"\tsplitter', 'splitter="true"'),
('splitter="false"\tsplitter', 'splitter="false"'),
('style\t@style','style="$1"'),
('title\t@title','title="$1"'),
('refreshonactivate\t@refreshonactivate','refreshonactivate="$1"'),
('refreshonactivate="true"\trefreshonactivate', 'refreshonactivate="true"'),
('refreshonactivate="false"\trefreshonactivate', 'refreshonactivate="false"'),
('titleIcon\t@titleIcon','titleIcon="$1"'),
('bindOnLoad\t@bindOnLoad','bindOnLoad="$1"'),
('bindOnLoad="true"\tbindOnLoad', 'bindOnLoad="true"'),
('bindOnLoad="false"\tbindOnLoad', 'bindOnLoad="false"'),
('tabtip\t@tabtip','tabtip="$1"')
],
'cfldap':
[
('server\t@server','server="$1"'),
('port\t@port','port="$1"'),
('username\t@username','username="$1"'),
('password\t@password','password="$1"'),
('action\t@action','action="$1"'),
('action="query"\taction', 'action="query"'),
('action="add"\taction', 'action="add"'),
('action="modify"\taction', 'action="modify"'),
('action="modifydn"\taction', 'action="modifydn"'),
('action="delete"\taction', 'action="delete"'),
('name\t@name','name="$1"'),
('timeout\t@timeout','timeout="$1"'),
('maxrows\t@maxrows','maxrows="$1"'),
('start\t@start','start="$1"'),
('scope\t@scope','scope="$1"'),
('scope="onelevel"\tscope', 'scope="onelevel"'),
('scope="base"\tscope', 'scope="base"'),
('scope="subtree"\tscope', 'scope="subtree"'),
('attributes\t@attributes','attributes="$1"'),
('returnasbinary\t@returnasbinary','returnasbinary="$1"'),
('filter\t@filter','filter="$1"'),
('sort\t@sort','sort="$1"'),
('sortcontrol\t@sortcontrol','sortcontrol="$1"'),
('sortcontrol="nocase"\tsortcontrol', 'sortcontrol="nocase"'),
('sortcontrol="asc"\tsortcontrol', 'sortcontrol="asc"'),
('sortcontrol="desc"\tsortcontrol', 'sortcontrol="desc"'),
('sortcontrol="nocase, desc"\tsortcontrol', 'sortcontrol="nocase, desc"'),
('sortcontrol="nocase, asc"\tsortcontrol', 'sortcontrol="nocase, asc"'),
('dn\t@dn','dn="$1"'),
('startrow\t@startrow','startrow="$1"'),
('modifytype\t@modifytype','modifytype="$1"'),
('modifytype="add"\tmodifytype', 'modifytype="add"'),
('modifytype="delete"\tmodifytype', 'modifytype="delete"'),
('modifytype="replace"\tmodifytype', 'modifytype="replace"'),
('rebind\t@rebind','rebind="$1"'),
('rebind="true"\trebind', 'rebind="true"'),
('rebind="false"\trebind', 'rebind="false"'),
('referral\t@referral','referral="$1"'),
('secure\t@secure','secure="$1"'),
('secure="cfssl_basic"\tsecure', 'secure="cfssl_basic"'),
('separator\t@separator','separator="$1"'),
('separator=","\tseparator', 'separator=","'),
('separator=";"\tseparator', 'separator=";"'),
('separator="|"\tseparator', 'separator="|"'),
('separator=":"\tseparator', 'separator=":"'),
('delimiter\t@delimiter','delimiter="$1"'),
('delimiter=","\tdelimiter', 'delimiter=","'),
('delimiter=";"\tdelimiter', 'delimiter=";"'),
('delimiter="|"\tdelimiter', 'delimiter="|"'),
('delimiter=":"\tdelimiter', 'delimiter=":"')
],
'cflocation':
[
('url\t@url','url="$1"'),
('addtoken\t@addtoken','addtoken="$1"'),
('addtoken="true"\taddtoken', 'addtoken="true"'),
('addtoken="false"\taddtoken', 'addtoken="false"'),
('statuscode\t@statuscode','statuscode="$1"')
],
'cflock':
[
('timeout\t@timeout','timeout="$1"'),
('scope\t@scope','scope="$1"'),
('scope="application"\tscope', 'scope="application"'),
('scope="request"\tscope', 'scope="request"'),
('scope="server"\tscope', 'scope="server"'),
('scope="session"\tscope', 'scope="session"'),
('name\t@name','name="$1"'),
('throwontimeout\t@throwontimeout','throwontimeout="$1"'),
('throwontimeout="true"\tthrowontimeout', 'throwontimeout="true"'),
('throwontimeout="false"\tthrowontimeout', 'throwontimeout="false"'),
('type\t@type','type="$1"'),
('type="readonly"\ttype', 'type="readonly"'),
('type="exclusive"\ttype', 'type="exclusive"')
],
'cflog':
[
('text\t@text','text="$1"'),
('log\t@log','log="$1"'),
('log="application"\tlog', 'log="application"'),
('log="scheduler"\tlog', 'log="scheduler"'),
('file\t@file','file="$1"'),
('type\t@type','type="$1"'),
('type="information"\ttype', 'type="information"'),
('type="warning"\ttype', 'type="warning"'),
('type="error"\ttype', 'type="error"'),
('type="fatal"\ttype', 'type="fatal"'),
('application\t@application','application="$1"'),
('application="true"\tapplication', 'application="true"'),
('application="false"\tapplication', 'application="false"')
],
'cflogin':
[
('idletimeout\t@idletimeout','idletimeout="$1"'),
('applicationtoken\t@applicationtoken','applicationtoken="$1"'),
('cookiedomain\t@cookiedomain','cookiedomain="$1"')
],
'cfloginuser':
[
('name\t@name','name="$1"'),
('password\t@password','password="$1"'),
('roles\t@roles','roles="$1"')
],
'cflogout':
[

],
'cfloop':
[
('index\t@index','index="$1"'),
('to\t@to','to="$1"'),
('from\t@from','from="$1"'),
('step\t@step','step="$1"'),
('condition\t@condition','condition="$1"'),
('query\t@query','query="$1"'),
('startrow\t@startrow','startrow="$1"'),
('endrow\t@endrow','endrow="$1"'),
('list\t@list','list="$1"'),
('delimiters\t@delimiters','delimiters="$1"'),
('delimiters=","\tdelimiters', 'delimiters=","'),
('delimiters=";"\tdelimiters', 'delimiters=";"'),
('delimiters="|"\tdelimiters', 'delimiters="|"'),
('delimiters=":"\tdelimiters', 'delimiters=":"'),
('collection\t@collection','collection="$1"'),
('item\t@item','item="$1"'),
('array\t@array','array="$1"'),
('characters\t@characters','characters="$1"'),
('file\t@file','file="$1"'),
('group\t@group','group="$1"'),
('groupcasesensitive\t@groupcasesensitive','groupcasesensitive="$1"'),
('groupcasesensitive="true"\tgroupcasesensitive', 'groupcasesensitive="true"'),
('groupcasesensitive="false"\tgroupcasesensitive', 'groupcasesensitive="false"')
],
'cfmail':
[
('to\t@to','to="$1"'),
('from\t@from','from="$1"'),
('cc\t@cc','cc="$1"'),
('bcc\t@bcc','bcc="$1"'),
('subject\t@subject','subject="$1"'),
('replyto\t@replyto','replyto="$1"'),
('failto\t@failto','failto="$1"'),
('username\t@username','username="$1"'),
('password\t@password','password="$1"'),
('wraptext\t@wraptext','wraptext="$1"'),
('charset\t@charset','charset="$1"'),
('charset="utf-8"\tcharset', 'charset="utf-8"'),
('charset="iso-8859-1"\tcharset', 'charset="iso-8859-1"'),
('charset="windows-1252"\tcharset', 'charset="windows-1252"'),
('charset="us-ascii"\tcharset', 'charset="us-ascii"'),
('charset="shift_jis"\tcharset', 'charset="shift_jis"'),
('charset="iso-2022-jp"\tcharset', 'charset="iso-2022-jp"'),
('charset="euc-jp"\tcharset', 'charset="euc-jp"'),
('charset="euc-kr"\tcharset', 'charset="euc-kr"'),
('charset="big5"\tcharset', 'charset="big5"'),
('charset="euc-cn"\tcharset', 'charset="euc-cn"'),
('charset="utf-16"\tcharset', 'charset="utf-16"'),
('type\t@type','type="$1"'),
('type="plain"\ttype', 'type="plain"'),
('type="html"\ttype', 'type="html"'),
('type="text"\ttype', 'type="text"'),
('type="text/html"\ttype', 'type="text/html"'),
('type="text/plain"\ttype', 'type="text/plain"'),
('mimeattach\t@mimeattach','mimeattach="$1"'),
('query\t@query','query="$1"'),
('group\t@group','group="$1"'),
('groupcasesensitive\t@groupcasesensitive','groupcasesensitive="$1"'),
('groupcasesensitive="true"\tgroupcasesensitive', 'groupcasesensitive="true"'),
('groupcasesensitive="false"\tgroupcasesensitive', 'groupcasesensitive="false"'),
('startrow\t@startrow','startrow="$1"'),
('maxrows\t@maxrows','maxrows="$1"'),
('server\t@server','server="$1"'),
('port\t@port','port="$1"'),
('mailerid\t@mailerid','mailerid="$1"'),
('timeout\t@timeout','timeout="$1"'),
('spoolenable\t@spoolenable','spoolenable="$1"'),
('spoolenable="true"\tspoolenable', 'spoolenable="true"'),
('spoolenable="false"\tspoolenable', 'spoolenable="false"'),
('debug\t@debug','debug="$1"'),
('debug="true"\tdebug', 'debug="true"'),
('debug="false"\tdebug', 'debug="false"'),
('priority\t@priority','priority="$1"'),
('priority="highest"\tpriority', 'priority="highest"'),
('priority="urgent"\tpriority', 'priority="urgent"'),
('priority="normal"\tpriority', 'priority="normal"'),
('priority="low"\tpriority', 'priority="low"'),
('priority="lowest"\tpriority', 'priority="lowest"'),
('usessl\t@usessl','usessl="$1"'),
('usessl="true"\tusessl', 'usessl="true"'),
('usessl="false"\tusessl', 'usessl="false"'),
('usetls\t@usetls','usetls="$1"'),
('usetls="true"\tusetls', 'usetls="true"'),
('usetls="false"\tusetls', 'usetls="false"'),
('remove\t@remove','remove="$1"'),
('keystore\t@keystore','keystore="$1"'),
('keypassword\t@keypassword','keypassword="$1"'),
('sign\t@sign','sign="$1"'),
('keyalias\t@keyalias','keyalias="$1"'),
('keystorepassword\t@keystorepassword','keystorepassword="$1"')
],
'cfmailparam':
[
('file\t@file','file="$1"'),
('type\t@type','type="$1"'),
('type="text/plain"\ttype', 'type="text/plain"'),
('type="text/html"\ttype', 'type="text/html"'),
('type="html"\ttype', 'type="html"'),
('type="plain"\ttype', 'type="plain"'),
('type="text"\ttype', 'type="text"'),
('name\t@name','name="$1"'),
('name="message-context"\tname', 'name="message-context"'),
('name="apparently-to"\tname', 'name="apparently-to"'),
('name="approved-by"\tname', 'name="approved-by"'),
('name="fax"\tname', 'name="fax"'),
('name="telefax"\tname', 'name="telefax"'),
('name="for-approval"\tname', 'name="for-approval"'),
('name="for-comment"\tname', 'name="for-comment"'),
('name="for-handling"\tname', 'name="for-handling"'),
('name="mail-system-version"\tname', 'name="mail-system-version"'),
('name="mailer"\tname', 'name="mailer"'),
('name="originating-client"\tname', 'name="originating-client"'),
('name="x-mailer "\tname', 'name="x-mailer "'),
('name="x-newsreader"\tname', 'name="x-newsreader"'),
('name="x-mimeole"\tname', 'name="x-mimeole"'),
('name="user-agent"\tname', 'name="user-agent"'),
('name="originator-info"\tname', 'name="originator-info"'),
('name="phone"\tname', 'name="phone"'),
('name="x-envelope-from"\tname', 'name="x-envelope-from"'),
('name="envelope-to"\tname', 'name="envelope-to"'),
('name="x-envelope-to"\tname', 'name="x-envelope-to"'),
('name="x-face"\tname', 'name="x-face"'),
('name="x-rcpt-to"\tname', 'name="x-rcpt-to"'),
('name="x-sender"\tname', 'name="x-sender"'),
('name="x-x-sender"\tname', 'name="x-x-sender"'),
('name="posted-to"\tname', 'name="posted-to"'),
('name="x-admin"\tname', 'name="x-admin"'),
('name="errors-to"\tname', 'name="errors-to"'),
('name="return-receipt-to"\tname', 'name="return-receipt-to"'),
('name="read-receipt-to"\tname', 'name="read-receipt-to"'),
('name="x-confirm-reading-to"\tname', 'name="x-confirm-reading-to"'),
('name="return-receipt-requested"\tname', 'name="return-receipt-requested"'),
('name="register-mail-reply-requested-by"\tname', 'name="register-mail-reply-requested-by"'),
('name="abuse-reports-to"\tname', 'name="abuse-reports-to"'),
('name="x-complaints-to"\tname', 'name="x-complaints-to"'),
('name="x-report-abuse-to"\tname', 'name="x-report-abuse-to"'),
('name="content-alias"\tname', 'name="content-alias"'),
('name="delivered-to"\tname', 'name="delivered-to"'),
('name="x-loop"\tname', 'name="x-loop"'),
('name="translated-by"\tname', 'name="translated-by"'),
('name="translation-of"\tname', 'name="translation-of"'),
('name="x-uidl"\tname', 'name="x-uidl"'),
('name="x-uri"\tname', 'name="x-uri"'),
('name="x-url"\tname', 'name="x-url"'),
('name="x-imap"\tname', 'name="x-imap"'),
('name="x-originalarrivaltime"\tname', 'name="x-originalarrivaltime"'),
('name="precedence"\tname', 'name="precedence"'),
('name="x-msmail-priority"\tname', 'name="x-msmail-priority"'),
('name="x-priority"\tname', 'name="x-priority"'),
('name="content-length"\tname', 'name="content-length"'),
('name="content-conversion"\tname', 'name="content-conversion"'),
('name="content-class"\tname', 'name="content-class"'),
('name="content-sgml-entity"\tname', 'name="content-sgml-entity"'),
('name="x-mime-autoconverted"\tname', 'name="x-mime-autoconverted"'),
('name="list-digest"\tname', 'name="list-digest"'),
('name="mailing-list"\tname', 'name="mailing-list"'),
('name="x-mailing-list"\tname', 'name="x-mailing-list"'),
('name="list-software"\tname', 'name="list-software"'),
('name="list-url"\tname', 'name="list-url"'),
('name="x-listserver"\tname', 'name="x-listserver"'),
('name="x-list-host"\tname', 'name="x-list-host"'),
('name="fcc"\tname', 'name="fcc"'),
('name="speech-act"\tname', 'name="speech-act"'),
('name="status"\tname', 'name="status"'),
('name="x-no-archive"\tname', 'name="x-no-archive"'),
('value\t@value','value="$1"'),
('contentID\t@contentID','contentID="$1"'),
('disposition\t@disposition','disposition="$1"'),
('disposition="attachment"\tdisposition', 'disposition="attachment"'),
('disposition="inline"\tdisposition', 'disposition="inline"'),
('content\t@content','content="$1"'),
('remove\t@remove','remove="$1"')
],
'cfmailpart':
[
('type\t@type','type="$1"'),
('type="text/plain"\ttype', 'type="text/plain"'),
('type="text/html"\ttype', 'type="text/html"'),
('wraptext\t@wraptext','wraptext="$1"'),
('charset\t@charset','charset="$1"'),
('charset="utf-8"\tcharset', 'charset="utf-8"'),
('charset="iso-8859-1"\tcharset', 'charset="iso-8859-1"'),
('charset="windows-1252"\tcharset', 'charset="windows-1252"'),
('charset="us-ascii"\tcharset', 'charset="us-ascii"'),
('charset="shift_jis"\tcharset', 'charset="shift_jis"'),
('charset="iso-2022-jp"\tcharset', 'charset="iso-2022-jp"'),
('charset="euc-jp"\tcharset', 'charset="euc-jp"'),
('charset="euc-kr"\tcharset', 'charset="euc-kr"'),
('charset="big5"\tcharset', 'charset="big5"'),
('charset="euc-cn"\tcharset', 'charset="euc-cn"'),
('charset="utf-16"\tcharset', 'charset="utf-16"')
],
'cfmodule':
[
('template\t@template','template="$1"'),
('name\t@name','name="$1"'),
('attributecollection\t@attributecollection','attributecollection="$1"')
],
'cfntauthenticate':
[
('username\t@username','username="$1"'),
('password\t@password','password="$1"'),
('domain\t@domain','domain="$1"'),
('result\t@result','result="$1"'),
('listgroups\t@listgroups','listgroups="$1"'),
('listgroups="true"\tlistgroups', 'listgroups="true"'),
('listgroups="false"\tlistgroups', 'listgroups="false"'),
('throwonerror\t@throwonerror','throwonerror="$1"'),
('throwonerror="true"\tthrowonerror', 'throwonerror="true"'),
('throwonerror="false"\tthrowonerror', 'throwonerror="false"')
],
'cfobject':
[
('type\t@type','type="$1"'),
('type="com"\ttype', 'type="com"'),
('type="component"\ttype', 'type="component"'),
('type="corba"\ttype', 'type="corba"'),
('type="java"\ttype', 'type="java"'),
('type="dotnet"\ttype', 'type="dotnet"'),
('type="webservice"\ttype', 'type="webservice"'),
('action\t@action','action="$1"'),
('action="create"\taction', 'action="create"'),
('action="connect"\taction', 'action="connect"'),
('class\t@class','class="$1"'),
('name\t@name','name="$1"'),
('context\t@context','context="$1"'),
('context="inproc"\tcontext', 'context="inproc"'),
('context="local"\tcontext', 'context="local"'),
('context="remote"\tcontext', 'context="remote"'),
('context="ior"\tcontext', 'context="ior"'),
('context="nameservice"\tcontext', 'context="nameservice"'),
('server\t@server','server="$1"'),
('component\t@component','component="$1"'),
('locale\t@locale','locale="$1"'),
('webservice\t@webservice','webservice="$1"'),
('password\t@password','password="$1"'),
('secure\t@secure','secure="$1"'),
('secure="true"\tsecure', 'secure="true"'),
('secure="false"\tsecure', 'secure="false"'),
('protocol\t@protocol','protocol="$1"'),
('protocol="tcp"\tprotocol', 'protocol="tcp"'),
('protocol="http"\tprotocol', 'protocol="http"'),
('proxyserver\t@proxyserver','proxyserver="$1"'),
('refreshwsdl\t@refreshwsdl','refreshwsdl="$1"'),
('refreshwsdl="true"\trefreshwsdl', 'refreshwsdl="true"'),
('refreshwsdl="false"\trefreshwsdl', 'refreshwsdl="false"'),
('wsportname\t@wsportname','wsportname="$1"'),
('wsdl2javaargs\t@wsdl2javaargs','wsdl2javaargs="$1"'),
('proxyport\t@proxyport','proxyport="$1"'),
('port\t@port','port="$1"'),
('proxypassword\t@proxypassword','proxypassword="$1"'),
('assembly\t@assembly','assembly="$1"'),
('username\t@username','username="$1"'),
('proxyuser\t@proxyuser','proxyuser="$1"'),
('wsversion\t@wsversion','wsversion="$1"'),
('wsversion="1"\twsversion', 'wsversion="1"'),
('wsversion="2"\twsversion', 'wsversion="2"')
],
'cfobjectcache':
[
('action\t@action','action="$1"'),
('action="clear"\taction', 'action="clear"')
],
'cfoutput':
[
('query\t@query','query="$1"'),
('group\t@group','group="$1"'),
('groupcasesensitive\t@groupcasesensitive','groupcasesensitive="$1"'),
('groupcasesensitive="true"\tgroupcasesensitive', 'groupcasesensitive="true"'),
('groupcasesensitive="false"\tgroupcasesensitive', 'groupcasesensitive="false"'),
('startrow\t@startrow','startrow="$1"'),
('maxrows\t@maxrows','maxrows="$1"')
],
'cfparam':
[
('name\t@name','name="$1"'),
('type\t@type','type="$1"'),
('type="any"\ttype', 'type="any"'),
('type="array"\ttype', 'type="array"'),
('type="binary"\ttype', 'type="binary"'),
('type="boolean"\ttype', 'type="boolean"'),
('type="creditcard"\ttype', 'type="creditcard"'),
('type="date"\ttype', 'type="date"'),
('type="time"\ttype', 'type="time"'),
('type="email"\ttype', 'type="email"'),
('type="eurodate"\ttype', 'type="eurodate"'),
('type="float"\ttype', 'type="float"'),
('type="numeric"\ttype', 'type="numeric"'),
('type="guid"\ttype', 'type="guid"'),
('type="integer"\ttype', 'type="integer"'),
('type="query"\ttype', 'type="query"'),
('type="range"\ttype', 'type="range"'),
('type="regex"\ttype', 'type="regex"'),
('type="regular_expression"\ttype', 'type="regular_expression"'),
('type="ssn"\ttype', 'type="ssn"'),
('type="social_security_number"\ttype', 'type="social_security_number"'),
('type="string"\ttype', 'type="string"'),
('type="struct"\ttype', 'type="struct"'),
('type="telephone"\ttype', 'type="telephone"'),
('type="url"\ttype', 'type="url"'),
('type="uuid"\ttype', 'type="uuid"'),
('type="usdate"\ttype', 'type="usdate"'),
('type="variablename"\ttype', 'type="variablename"'),
('type="xml"\ttype', 'type="xml"'),
('type="zipcode"\ttype', 'type="zipcode"'),
('default\t@default','default="$1"'),
('max\t@max','max="$1"'),
('min\t@min','min="$1"'),
('pattern\t@pattern','pattern="$1"'),
('maxlength\t@maxlength','maxlength="$1"')
],
'cfpod':
[
('bodyStyle\t@bodyStyle','bodyStyle="$1"'),
('headerStyle\t@headerStyle','headerStyle="$1"'),
('height\t@height','height="$1"'),
('name\t@name','name="$1"'),
('onBindError\t@onBindError','onBindError="$1"'),
('overflow\t@overflow','overflow="$1"'),
('overflow="auto"\toverflow', 'overflow="auto"'),
('overflow="hidden"\toverflow', 'overflow="hidden"'),
('overflow="scroll"\toverflow', 'overflow="scroll"'),
('overflow="visible"\toverflow', 'overflow="visible"'),
('source\t@source','source="$1"'),
('title\t@title','title="$1"'),
('width\t@width','width="$1"')
],
'cfpop':
[
('server\t@server','server="$1"'),
('port\t@port','port="$1"'),
('username\t@username','username="$1"'),
('password\t@password','password="$1"'),
('action\t@action','action="$1"'),
('action="getheaderonly"\taction', 'action="getheaderonly"'),
('action="getall"\taction', 'action="getall"'),
('action="delete"\taction', 'action="delete"'),
('name\t@name','name="$1"'),
('messagenumber\t@messagenumber','messagenumber="$1"'),
('uid\t@uid','uid="$1"'),
('attachmentpath\t@attachmentpath','attachmentpath="$1"'),
('timeout\t@timeout','timeout="$1"'),
('maxrows\t@maxrows','maxrows="$1"'),
('startrow\t@startrow','startrow="$1"'),
('generateUniqueFileNames\t@generateUniqueFileNames','generateUniqueFileNames="$1"'),
('generateUniqueFileNames="true"\tgenerateUniqueFileNames', 'generateUniqueFileNames="true"'),
('generateUniqueFileNames="false"\tgenerateUniqueFileNames', 'generateUniqueFileNames="false"'),
('secure\t@secure','secure="$1"'),
('secure="true"\tsecure', 'secure="true"'),
('secure="false"\tsecure', 'secure="false"')
],
'cfprocessingdirective':
[
('suppressWhitespace\t@suppressWhitespace','suppressWhitespace="$1"'),
('suppressWhitespace="true"\tsuppressWhitespace', 'suppressWhitespace="true"'),
('suppressWhitespace="false"\tsuppressWhitespace', 'suppressWhitespace="false"'),
('pageEncoding\t@pageEncoding','pageEncoding="$1"'),
('pageEncoding="utf-8"\tpageEncoding', 'pageEncoding="utf-8"'),
('pageEncoding="iso-8859-1"\tpageEncoding', 'pageEncoding="iso-8859-1"'),
('pageEncoding="windows-1252"\tpageEncoding', 'pageEncoding="windows-1252"'),
('pageEncoding="us-ascii"\tpageEncoding', 'pageEncoding="us-ascii"'),
('pageEncoding="shift_jis"\tpageEncoding', 'pageEncoding="shift_jis"'),
('pageEncoding="iso-2022-jp"\tpageEncoding', 'pageEncoding="iso-2022-jp"'),
('pageEncoding="euc-jp"\tpageEncoding', 'pageEncoding="euc-jp"'),
('pageEncoding="euc-kr"\tpageEncoding', 'pageEncoding="euc-kr"'),
('pageEncoding="big5"\tpageEncoding', 'pageEncoding="big5"'),
('pageEncoding="euc-cn"\tpageEncoding', 'pageEncoding="euc-cn"'),
('pageEncoding="utf-16"\tpageEncoding', 'pageEncoding="utf-16"')
],
'cfprocparam':
[
('type\t@type','type="$1"'),
('type="in"\ttype', 'type="in"'),
('type="out"\ttype', 'type="out"'),
('type="inout"\ttype', 'type="inout"'),
('variable\t@variable','variable="$1"'),
('value\t@value','value="$1"'),
('cfsqltype\t@cfsqltype','cfsqltype="$1"'),
('cfsqltype="cf_sql_bigint"\tcfsqltype', 'cfsqltype="cf_sql_bigint"'),
('cfsqltype="cf_sql_bit"\tcfsqltype', 'cfsqltype="cf_sql_bit"'),
('cfsqltype="cf_sql_char"\tcfsqltype', 'cfsqltype="cf_sql_char"'),
('cfsqltype="cf_sql_blob"\tcfsqltype', 'cfsqltype="cf_sql_blob"'),
('cfsqltype="cf_sql_clob"\tcfsqltype', 'cfsqltype="cf_sql_clob"'),
('cfsqltype="cf_sql_date"\tcfsqltype', 'cfsqltype="cf_sql_date"'),
('cfsqltype="cf_sql_decimal"\tcfsqltype', 'cfsqltype="cf_sql_decimal"'),
('cfsqltype="cf_sql_double"\tcfsqltype', 'cfsqltype="cf_sql_double"'),
('cfsqltype="cf_sql_float"\tcfsqltype', 'cfsqltype="cf_sql_float"'),
('cfsqltype="cf_sql_idstamp"\tcfsqltype', 'cfsqltype="cf_sql_idstamp"'),
('cfsqltype="cf_sql_integer"\tcfsqltype', 'cfsqltype="cf_sql_integer"'),
('cfsqltype="cf_sql_longvarchar"\tcfsqltype', 'cfsqltype="cf_sql_longvarchar"'),
('cfsqltype="cf_sql_money"\tcfsqltype', 'cfsqltype="cf_sql_money"'),
('cfsqltype="cf_sql_money4"\tcfsqltype', 'cfsqltype="cf_sql_money4"'),
('cfsqltype="cf_sql_numeric"\tcfsqltype', 'cfsqltype="cf_sql_numeric"'),
('cfsqltype="cf_sql_real"\tcfsqltype', 'cfsqltype="cf_sql_real"'),
('cfsqltype="cf_sql_refcursor"\tcfsqltype', 'cfsqltype="cf_sql_refcursor"'),
('cfsqltype="cf_sql_smallint"\tcfsqltype', 'cfsqltype="cf_sql_smallint"'),
('cfsqltype="cf_sql_time"\tcfsqltype', 'cfsqltype="cf_sql_time"'),
('cfsqltype="cf_sql_timestamp"\tcfsqltype', 'cfsqltype="cf_sql_timestamp"'),
('cfsqltype="cf_sql_tinyint"\tcfsqltype', 'cfsqltype="cf_sql_tinyint"'),
('cfsqltype="cf_sql_varchar"\tcfsqltype', 'cfsqltype="cf_sql_varchar"'),
('cfsqltype="cf_sql_nchar"\tcfsqltype', 'cfsqltype="cf_sql_nchar"'),
('cfsqltype="cf_sql_nvarchar"\tcfsqltype', 'cfsqltype="cf_sql_nvarchar"'),
('cfsqltype="cf_sql_longnvarchar"\tcfsqltype', 'cfsqltype="cf_sql_longnvarchar"'),
('cfsqltype="cf_sql_nclob"\tcfsqltype', 'cfsqltype="cf_sql_nclob"'),
('cfsqltype="cf_sql_sqlxml"\tcfsqltype', 'cfsqltype="cf_sql_sqlxml"'),
('maxlength\t@maxlength','maxlength="$1"'),
('scale\t@scale','scale="$1"'),
('null\t@null','null="$1"'),
('null="true"\tnull', 'null="true"'),
('null="false"\tnull', 'null="false"')
],
'cfprocresult':
[
('name\t@name','name="$1"'),
('resultset\t@resultset','resultset="$1"'),
('maxrows\t@maxrows','maxrows="$1"')
],
'cfproperty':
[
('name\t@name','name="$1"'),
('type\t@type','type="$1"'),
('type="any"\ttype', 'type="any"'),
('type="array"\ttype', 'type="array"'),
('type="binary"\ttype', 'type="binary"'),
('type="boolean"\ttype', 'type="boolean"'),
('type="date"\ttype', 'type="date"'),
('type="guid"\ttype', 'type="guid"'),
('type="numeric"\ttype', 'type="numeric"'),
('type="query"\ttype', 'type="query"'),
('type="string"\ttype', 'type="string"'),
('type="struct"\ttype', 'type="struct"'),
('type="uuid"\ttype', 'type="uuid"'),
('type="variablename"\ttype', 'type="variablename"'),
('required\t@required','required="$1"'),
('required="true"\trequired', 'required="true"'),
('required="false"\trequired', 'required="false"'),
('default\t@default','default="$1"'),
('displayname\t@displayname','displayname="$1"'),
('hint\t@hint','hint="$1"'),
('fieldtype\t@fieldtype','fieldtype="$1"'),
('fieldtype="id"\tfieldtype', 'fieldtype="id"'),
('fieldtype="column"\tfieldtype', 'fieldtype="column"'),
('fieldtype="one-to-one"\tfieldtype', 'fieldtype="one-to-one"'),
('fieldtype="one-to-many"\tfieldtype', 'fieldtype="one-to-many"'),
('fieldtype="many-to-many"\tfieldtype', 'fieldtype="many-to-many"'),
('fieldtype="many-to-one"\tfieldtype', 'fieldtype="many-to-one"'),
('fieldtype="collection"\tfieldtype', 'fieldtype="collection"'),
('fieldtype="timestamp"\tfieldtype', 'fieldtype="timestamp"'),
('fieldtype="version"\tfieldtype', 'fieldtype="version"'),
('ormType\t@ormType','ormType="$1"'),
('ormType="string"\tormType', 'ormType="string"'),
('ormType="character"\tormType', 'ormType="character"'),
('ormType="char"\tormType', 'ormType="char"'),
('ormType="short"\tormType', 'ormType="short"'),
('ormType="integer"\tormType', 'ormType="integer"'),
('ormType="int"\tormType', 'ormType="int"'),
('ormType="long"\tormType', 'ormType="long"'),
('ormType="big_decimal"\tormType', 'ormType="big_decimal"'),
('ormType="float"\tormType', 'ormType="float"'),
('ormType="double"\tormType', 'ormType="double"'),
('ormType="boolean"\tormType', 'ormType="boolean"'),
('ormType="yes_no"\tormType', 'ormType="yes_no"'),
('ormType="true_false"\tormType', 'ormType="true_false"'),
('ormType="text"\tormType', 'ormType="text"'),
('ormType="date"\tormType', 'ormType="date"'),
('ormType="timestamp"\tormType', 'ormType="timestamp"'),
('ormType="binary"\tormType', 'ormType="binary"'),
('ormType="serializable"\tormType', 'ormType="serializable"'),
('ormType="blob"\tormType', 'ormType="blob"'),
('ormType="clob"\tormType', 'ormType="clob"'),
('column\t@column','column="$1"'),
('generator\t@generator','generator="$1"'),
('generator="increment"\tgenerator', 'generator="increment"'),
('generator="identity"\tgenerator', 'generator="identity"'),
('generator="sequence"\tgenerator', 'generator="sequence"'),
('generator="seqhilo"\tgenerator', 'generator="seqhilo"'),
('generator="uuid"\tgenerator', 'generator="uuid"'),
('generator="guid"\tgenerator', 'generator="guid"'),
('generator="native"\tgenerator', 'generator="native"'),
('generator="assigned"\tgenerator', 'generator="assigned"'),
('generator="select"\tgenerator', 'generator="select"'),
('generator="foreign"\tgenerator', 'generator="foreign"'),
('generator="sequence-indentity"\tgenerator', 'generator="sequence-indentity"'),
('sequence\t@sequence','sequence="$1"'),
('selectkey\t@selectkey','selectkey="$1"'),
('params\t@params','params="$1"'),
('length\t@length','length="$1"'),
('precision\t@precision','precision="$1"'),
('index\t@index','index="$1"'),
('setter\t@setter','setter="$1"'),
('setter="true"\tsetter', 'setter="true"'),
('setter="false"\tsetter', 'setter="false"'),
('getter\t@getter','getter="$1"'),
('getter="true"\tgetter', 'getter="true"'),
('getter="false"\tgetter', 'getter="false"'),
('source\t@source','source="$1"'),
('source="vm"\tsource', 'source="vm"'),
('source="db"\tsource', 'source="db"'),
('elementcolumn\t@elementcolumn','elementcolumn="$1"'),
('elementtype\t@elementtype','elementtype="$1"'),
('elementtype="string"\telementtype', 'elementtype="string"'),
('elementtype="character"\telementtype', 'elementtype="character"'),
('elementtype="char"\telementtype', 'elementtype="char"'),
('elementtype="short"\telementtype', 'elementtype="short"'),
('elementtype="integer"\telementtype', 'elementtype="integer"'),
('elementtype="int"\telementtype', 'elementtype="int"'),
('elementtype="long"\telementtype', 'elementtype="long"'),
('elementtype="big_decimal"\telementtype', 'elementtype="big_decimal"'),
('elementtype="float"\telementtype', 'elementtype="float"'),
('elementtype="double"\telementtype', 'elementtype="double"'),
('elementtype="boolean"\telementtype', 'elementtype="boolean"'),
('elementtype="yes_no"\telementtype', 'elementtype="yes_no"'),
('elementtype="true_false"\telementtype', 'elementtype="true_false"'),
('elementtype="text"\telementtype', 'elementtype="text"'),
('elementtype="date"\telementtype', 'elementtype="date"'),
('elementtype="timestamp"\telementtype', 'elementtype="timestamp"'),
('elementtype="binary"\telementtype', 'elementtype="binary"'),
('elementtype="serializable"\telementtype', 'elementtype="serializable"'),
('elementtype="blob"\telementtype', 'elementtype="blob"'),
('elementtype="clob"\telementtype', 'elementtype="clob"'),
('structkeytype\t@structkeytype','structkeytype="$1"'),
('structkeytype="string"\tstructkeytype', 'structkeytype="string"'),
('structkeytype="character"\tstructkeytype', 'structkeytype="character"'),
('structkeytype="char"\tstructkeytype', 'structkeytype="char"'),
('structkeytype="short"\tstructkeytype', 'structkeytype="short"'),
('structkeytype="integer"\tstructkeytype', 'structkeytype="integer"'),
('structkeytype="int"\tstructkeytype', 'structkeytype="int"'),
('structkeytype="long"\tstructkeytype', 'structkeytype="long"'),
('structkeytype="big_decimal"\tstructkeytype', 'structkeytype="big_decimal"'),
('structkeytype="float"\tstructkeytype', 'structkeytype="float"'),
('structkeytype="double"\tstructkeytype', 'structkeytype="double"'),
('structkeytype="boolean"\tstructkeytype', 'structkeytype="boolean"'),
('structkeytype="yes_no"\tstructkeytype', 'structkeytype="yes_no"'),
('structkeytype="true_false"\tstructkeytype', 'structkeytype="true_false"'),
('structkeytype="text"\tstructkeytype', 'structkeytype="text"'),
('structkeytype="date"\tstructkeytype', 'structkeytype="date"'),
('structkeytype="timestamp"\tstructkeytype', 'structkeytype="timestamp"'),
('structkeytype="binary"\tstructkeytype', 'structkeytype="binary"'),
('structkeytype="serializable"\tstructkeytype', 'structkeytype="serializable"'),
('structkeytype="blob"\tstructkeytype', 'structkeytype="blob"'),
('structkeytype="clob"\tstructkeytype', 'structkeytype="clob"'),
('structkeycolumn\t@structkeycolumn','structkeycolumn="$1"'),
('inversejoincolumn\t@inversejoincolumn','inversejoincolumn="$1"'),
('linkschema\t@linkschema','linkschema="$1"'),
('linkcatalog\t@linkcatalog','linkcatalog="$1"'),
('linktable\t@linktable','linktable="$1"'),
('missingRowIgnored\t@missingRowIgnored','missingRowIgnored="$1"'),
('missingRowIgnored="true"\tmissingRowIgnored', 'missingRowIgnored="true"'),
('missingRowIgnored="false"\tmissingRowIgnored', 'missingRowIgnored="false"'),
('inverse\t@inverse','inverse="$1"'),
('inverse="true"\tinverse', 'inverse="true"'),
('inverse="false"\tinverse', 'inverse="false"'),
('orderby\t@orderby','orderby="$1"'),
('fkcolumn\t@fkcolumn','fkcolumn="$1"'),
('fetch\t@fetch','fetch="$1"'),
('fetch="join"\tfetch', 'fetch="join"'),
('fetch="select"\tfetch', 'fetch="select"'),
('cascade\t@cascade','cascade="$1"'),
('cascade="all"\tcascade', 'cascade="all"'),
('cascade="none"\tcascade', 'cascade="none"'),
('cascade="save-update"\tcascade', 'cascade="save-update"'),
('cascade="delete"\tcascade', 'cascade="delete"'),
('cascade="all-delete-orphan"\tcascade', 'cascade="all-delete-orphan"'),
('cascade="delete-orphan"\tcascade', 'cascade="delete-orphan"'),
('cascade="create"\tcascade', 'cascade="create"'),
('cascade="merge"\tcascade', 'cascade="merge"'),
('cascade="lock"\tcascade', 'cascade="lock"'),
('cascade="refresh"\tcascade', 'cascade="refresh"'),
('cascade="evict"\tcascade', 'cascade="evict"'),
('cascade="replicate"\tcascade', 'cascade="replicate"'),
('constrained\t@constrained','constrained="$1"'),
('constrained="true"\tconstrained', 'constrained="true"'),
('constrained="false"\tconstrained', 'constrained="false"'),
('unique\t@unique','unique="$1"'),
('unique="true"\tunique', 'unique="true"'),
('unique="false"\tunique', 'unique="false"'),
('uniquekey\t@uniquekey','uniquekey="$1"'),
('notnull\t@notnull','notnull="$1"'),
('notnull="true"\tnotnull', 'notnull="true"'),
('notnull="false"\tnotnull', 'notnull="false"'),
('update\t@update','update="$1"'),
('update="true"\tupdate', 'update="true"'),
('update="false"\tupdate', 'update="false"'),
('insert\t@insert','insert="$1"'),
('insert="true"\tinsert', 'insert="true"'),
('insert="false"\tinsert', 'insert="false"'),
('generated\t@generated','generated="$1"'),
('generated="never"\tgenerated', 'generated="never"'),
('generated="insert"\tgenerated', 'generated="insert"'),
('generated="always"\tgenerated', 'generated="always"'),
('formula\t@formula','formula="$1"'),
('lazy\t@lazy','lazy="$1"'),
('lazy="true"\tlazy', 'lazy="true"'),
('lazy="false"\tlazy', 'lazy="false"'),
('lazy="extra"\tlazy', 'lazy="extra"'),
('optimisticLock\t@optimisticLock','optimisticLock="$1"'),
('optimisticLock="true"\toptimisticLock', 'optimisticLock="true"'),
('optimisticLock="false"\toptimisticLock', 'optimisticLock="false"'),
('scale\t@scale','scale="$1"'),
('mappedby\t@mappedby','mappedby="$1"'),
('cfc\t@cfc','cfc="$1"'),
('joinColumn\t@joinColumn','joinColumn="$1"'),
('validate\t@validate','validate="$1"'),
('validate="string"\tvalidate', 'validate="string"'),
('validate="boolean"\tvalidate', 'validate="boolean"'),
('validate="integer"\tvalidate', 'validate="integer"'),
('validate="numeric"\tvalidate', 'validate="numeric"'),
('validate="date"\tvalidate', 'validate="date"'),
('validate="time"\tvalidate', 'validate="time"'),
('validate="creditcard"\tvalidate', 'validate="creditcard"'),
('validate="email"\tvalidate', 'validate="email"'),
('validate="eurodate"\tvalidate', 'validate="eurodate"'),
('validate="regex"\tvalidate', 'validate="regex"'),
('validate="ssn"\tvalidate', 'validate="ssn"'),
('validate="telephone"\tvalidate', 'validate="telephone"'),
('validate="uuid"\tvalidate', 'validate="uuid"'),
('validate="guid"\tvalidate', 'validate="guid"'),
('validate="zipcode"\tvalidate', 'validate="zipcode"'),
('validateParams\t@validateParams','validateParams="$1"'),
('cacheUse\t@cacheUse','cacheUse="$1"'),
('cacheUse="read-only"\tcacheUse', 'cacheUse="read-only"'),
('cacheUse="nonstrict-read-write"\tcacheUse', 'cacheUse="nonstrict-read-write"'),
('cacheUse="read-write"\tcacheUse', 'cacheUse="read-write"'),
('cacheUse="transactional"\tcacheUse', 'cacheUse="transactional"'),
('sqlType\t@sqlType','sqlType="$1"'),
('dbDefault\t@dbDefault','dbDefault="$1"'),
('where\t@where','where="$1"'),
('persistent\t@persistent','persistent="$1"'),
('persistent="true"\tpersistent', 'persistent="true"'),
('persistent="false"\tpersistent', 'persistent="false"'),
('unSavedValue\t@unSavedValue','unSavedValue="$1"'),
('serializable\t@serializable','serializable="$1"'),
('serializable="true"\tserializable', 'serializable="true"'),
('serializable="false"\tserializable', 'serializable="false"'),
('singularname\t@singularname','singularname="$1"'),
('remotingFetch\t@remotingFetch','remotingFetch="$1"'),
('remotingFetch="false"\tremotingFetch', 'remotingFetch="false"'),
('remotingFetch="true"\tremotingFetch', 'remotingFetch="true"'),
('table\t@table','table="$1"'),
('indexBoost\t@indexBoost','indexBoost="$1"'),
('indexTokenize\t@indexTokenize','indexTokenize="$1"'),
('indexTokenize="false"\tindexTokenize', 'indexTokenize="false"'),
('indexTokenize="true"\tindexTokenize', 'indexTokenize="true"'),
('indexStore\t@indexStore','indexStore="$1"'),
('indexStore="true"\tindexStore', 'indexStore="true"'),
('indexStore="false"\tindexStore', 'indexStore="false"'),
('indexStore="compressed"\tindexStore', 'indexStore="compressed"'),
('indexFieldName\t@indexFieldName','indexFieldName="$1"'),
('indexable\t@indexable','indexable="$1"'),
('indexable="false"\tindexable', 'indexable="false"'),
('indexable="true"\tindexable', 'indexable="true"'),
('indexLanguage\t@indexLanguage','indexLanguage="$1"')
],
'cfquery':
[
('name\t@name','name="$1"'),
('datasource\t@datasource','datasource="$1"'),
('ormoptions\t@ormoptions','ormoptions="$1"'),
('dbtype\t@dbtype','dbtype="$1"'),
('dbtype="query"\tdbtype', 'dbtype="query"'),
('dbtype="hql"\tdbtype', 'dbtype="hql"'),
('username\t@username','username="$1"'),
('password\t@password','password="$1"'),
('maxrows\t@maxrows','maxrows="$1"'),
('blockfactor\t@blockfactor','blockfactor="$1"'),
('timeout\t@timeout','timeout="$1"'),
('cachedafter\t@cachedafter','cachedafter="$1"'),
('cachedwithin\t@cachedwithin','cachedwithin="$1"'),
('debug\t@debug','debug="$1"'),
('debug="true"\tdebug', 'debug="true"'),
('debug="false"\tdebug', 'debug="false"'),
('result\t@result','result="$1"'),
('cacheId\t@cacheId','cacheId="$1"'),
('cacheRegion\t@cacheRegion','cacheRegion="$1"'),
('fetchclientinfo\t@fetchclientinfo','fetchclientinfo="$1"'),
('clientinfo\t@clientinfo','clientinfo="$1"')
],
'cfqueryparam':
[
('value\t@value','value="$1"'),
('cfsqltype\t@cfsqltype','cfsqltype="$1"'),
('cfsqltype="cf_sql_bigint"\tcfsqltype', 'cfsqltype="cf_sql_bigint"'),
('cfsqltype="cf_sql_bit"\tcfsqltype', 'cfsqltype="cf_sql_bit"'),
('cfsqltype="cf_sql_char"\tcfsqltype', 'cfsqltype="cf_sql_char"'),
('cfsqltype="cf_sql_blob"\tcfsqltype', 'cfsqltype="cf_sql_blob"'),
('cfsqltype="cf_sql_clob"\tcfsqltype', 'cfsqltype="cf_sql_clob"'),
('cfsqltype="cf_sql_date"\tcfsqltype', 'cfsqltype="cf_sql_date"'),
('cfsqltype="cf_sql_decimal"\tcfsqltype', 'cfsqltype="cf_sql_decimal"'),
('cfsqltype="cf_sql_double"\tcfsqltype', 'cfsqltype="cf_sql_double"'),
('cfsqltype="cf_sql_float"\tcfsqltype', 'cfsqltype="cf_sql_float"'),
('cfsqltype="cf_sql_idstamp"\tcfsqltype', 'cfsqltype="cf_sql_idstamp"'),
('cfsqltype="cf_sql_integer"\tcfsqltype', 'cfsqltype="cf_sql_integer"'),
('cfsqltype="cf_sql_longvarchar"\tcfsqltype', 'cfsqltype="cf_sql_longvarchar"'),
('cfsqltype="cf_sql_money"\tcfsqltype', 'cfsqltype="cf_sql_money"'),
('cfsqltype="cf_sql_money4"\tcfsqltype', 'cfsqltype="cf_sql_money4"'),
('cfsqltype="cf_sql_numeric"\tcfsqltype', 'cfsqltype="cf_sql_numeric"'),
('cfsqltype="cf_sql_real"\tcfsqltype', 'cfsqltype="cf_sql_real"'),
('cfsqltype="cf_sql_refcursor"\tcfsqltype', 'cfsqltype="cf_sql_refcursor"'),
('cfsqltype="cf_sql_smallint"\tcfsqltype', 'cfsqltype="cf_sql_smallint"'),
('cfsqltype="cf_sql_time"\tcfsqltype', 'cfsqltype="cf_sql_time"'),
('cfsqltype="cf_sql_timestamp"\tcfsqltype', 'cfsqltype="cf_sql_timestamp"'),
('cfsqltype="cf_sql_tinyint"\tcfsqltype', 'cfsqltype="cf_sql_tinyint"'),
('cfsqltype="cf_sql_varchar"\tcfsqltype', 'cfsqltype="cf_sql_varchar"'),
('maxlength\t@maxlength','maxlength="$1"'),
('scale\t@scale','scale="$1"'),
('null\t@null','null="$1"'),
('null="true"\tnull', 'null="true"'),
('null="false"\tnull', 'null="false"'),
('list\t@list','list="$1"'),
('list="true"\tlist', 'list="true"'),
('list="false"\tlist', 'list="false"'),
('separator\t@separator','separator="$1"'),
('separator=","\tseparator', 'separator=","'),
('separator=";"\tseparator', 'separator=";"'),
('separator="|"\tseparator', 'separator="|"'),
('separator=":"\tseparator', 'separator=":"')
],
'cfregistry':
[
('action\t@action','action="$1"'),
('action="getall"\taction', 'action="getall"'),
('action="get"\taction', 'action="get"'),
('action="set"\taction', 'action="set"'),
('action="delete"\taction', 'action="delete"'),
('branch\t@branch','branch="$1"'),
('entry\t@entry','entry="$1"'),
('variable\t@variable','variable="$1"'),
('type\t@type','type="$1"'),
('type="string"\ttype', 'type="string"'),
('type="dword"\ttype', 'type="dword"'),
('type="key"\ttype', 'type="key"'),
('type="any"\ttype', 'type="any"'),
('sort\t@sort','sort="$1"'),
('sort="entry asc"\tsort', 'sort="entry asc"'),
('sort="entry desc"\tsort', 'sort="entry desc"'),
('sort="type asc"\tsort', 'sort="type asc"'),
('sort="type desc"\tsort', 'sort="type desc"'),
('sort="value asc"\tsort', 'sort="value asc"'),
('sort="value desc"\tsort', 'sort="value desc"'),
('directory\t@directory','directory="$1"'),
('name\t@name','name="$1"'),
('mode\t@mode','mode="$1"'),
('newdirectory\t@newdirectory','newdirectory="$1"'),
('value\t@value','value="$1"'),
('recurse\t@recurse','recurse="$1"'),
('recurse="true"\trecurse', 'recurse="true"'),
('recurse="false"\trecurse', 'recurse="false"'),
('registryversion\t@registryversion','registryversion="$1"')
],
'cfreport':
[
('template\t@template','template="$1"'),
('format\t@format','format="$1"'),
('format="pdf"\tformat', 'format="pdf"'),
('format="flashpaper"\tformat', 'format="flashpaper"'),
('format="excel"\tformat', 'format="excel"'),
('format="rtf"\tformat', 'format="rtf"'),
('format="html"\tformat', 'format="html"'),
('format="xml"\tformat', 'format="xml"'),
('name\t@name','name="$1"'),
('filename\t@filename','filename="$1"'),
('query\t@query','query="$1"'),
('overwrite\t@overwrite','overwrite="$1"'),
('overwrite="true"\toverwrite', 'overwrite="true"'),
('overwrite="false"\toverwrite', 'overwrite="false"'),
('encryption\t@encryption','encryption="$1"'),
('encryption="128-bit"\tencryption', 'encryption="128-bit"'),
('encryption="40-bit"\tencryption', 'encryption="40-bit"'),
('encryption="none"\tencryption', 'encryption="none"'),
('ownerpassword\t@ownerpassword','ownerpassword="$1"'),
('userpassword\t@userpassword','userpassword="$1"'),
('permissions\t@permissions','permissions="$1"'),
('permissions="allowprinting,allowcopy,allowscreenreaders"\tpermissions', 'permissions="allowprinting,allowcopy,allowscreenreaders"'),
('permissions="allowprinting"\tpermissions', 'permissions="allowprinting"'),
('permissions="allowmodifycontents"\tpermissions', 'permissions="allowmodifycontents"'),
('permissions="allowcopy"\tpermissions', 'permissions="allowcopy"'),
('permissions="allowmodifyannotations"\tpermissions', 'permissions="allowmodifyannotations"'),
('permissions="allowfillin"\tpermissions', 'permissions="allowfillin"'),
('permissions="allowscreenreaders"\tpermissions', 'permissions="allowscreenreaders"'),
('permissions="allowassembly"\tpermissions', 'permissions="allowassembly"'),
('permissions="allowdegradedprinting"\tpermissions', 'permissions="allowdegradedprinting"'),
('permissions="allowprinting,allowmodifycontents,allowcopy,allowmodifyannotations,allowfillin,allowscreenreaders,allowassembly,allowdegradedprinting"\tpermissions', 'permissions="allowprinting,allowmodifycontents,allowcopy,allowmodifyannotations,allowfillin,allowscreenreaders,allowassembly,allowdegradedprinting"'),
('datasource\t@datasource','datasource="$1"'),
('type\t@type','type="$1"'),
('type="standard"\ttype', 'type="standard"'),
('type="netscape"\ttype', 'type="netscape"'),
('type="microsoft"\ttype', 'type="microsoft"'),
('timeout\t@timeout','timeout="$1"'),
('report\t@report','report="$1"'),
('orderby\t@orderby','orderby="$1"'),
('username\t@username','username="$1"'),
('password\t@password','password="$1"'),
('formula\t@formula','formula="$1"'),
('resourceTimespan\t@resourceTimespan','resourceTimespan="$1"'),
('style\t@style','style="$1"')
],
'cfreportparam':
[
('name\t@name','name="$1"'),
('value\t@value','value="$1"'),
('chart\t@chart','chart="$1"'),
('query\t@query','query="$1"'),
('series\t@series','series="$1"'),
('style\t@style','style="$1"'),
('subreport\t@subreport','subreport="$1"')
],
'cfrethrow':
[

],
'cfreturn':
[

],
'cfsavecontent':
[
('variable\t@variable','variable="$1"')
],
'cfschedule':
[
('action\t@action','action="$1"'),
('action="delete"\taction', 'action="delete"'),
('action="update"\taction', 'action="update"'),
('action="run"\taction', 'action="run"'),
('action="pause"\taction', 'action="pause"'),
('action="resume"\taction', 'action="resume"'),
('action="list"\taction', 'action="list"'),
('action="pauseall"\taction', 'action="pauseall"'),
('action="resumeall"\taction', 'action="resumeall"'),
('task\t@task','task="$1"'),
('operation\t@operation','operation="$1"'),
('operation="httprequest"\toperation', 'operation="httprequest"'),
('file\t@file','file="$1"'),
('path\t@path','path="$1"'),
('startdate\t@startdate','startdate="$1"'),
('starttime\t@starttime','starttime="$1"'),
('URL\t@URL','URL="$1"'),
('port\t@port','port="$1"'),
('publish\t@publish','publish="$1"'),
('publish="true"\tpublish', 'publish="true"'),
('publish="false"\tpublish', 'publish="false"'),
('endDate\t@endDate','endDate="$1"'),
('endTime\t@endTime','endTime="$1"'),
('interval\t@interval','interval="$1"'),
('interval="once"\tinterval', 'interval="once"'),
('interval="daily"\tinterval', 'interval="daily"'),
('interval="weekly"\tinterval', 'interval="weekly"'),
('interval="monthly"\tinterval', 'interval="monthly"'),
('requesttimeout\t@requesttimeout','requesttimeout="$1"'),
('username\t@username','username="$1"'),
('password\t@password','password="$1"'),
('proxyserver\t@proxyserver','proxyserver="$1"'),
('proxyport\t@proxyport','proxyport="$1"'),
('proxyuser\t@proxyuser','proxyuser="$1"'),
('proxypassword\t@proxypassword','proxypassword="$1"'),
('resolveurl\t@resolveurl','resolveurl="$1"'),
('resolveurl="true"\tresolveurl', 'resolveurl="true"'),
('resolveurl="false"\tresolveurl', 'resolveurl="false"'),
('group\t@group','group="$1"'),
('onException\t@onException','onException="$1"'),
('onException="refire"\tonException', 'onException="refire"'),
('onException="pause"\tonException', 'onException="pause"'),
('onException="invokehandler"\tonException', 'onException="invokehandler"'),
('repeat\t@repeat','repeat="$1"'),
('onComplete\t@onComplete','onComplete="$1"'),
('cronTime\t@cronTime','cronTime="$1"'),
('priority\t@priority','priority="$1"'),
('eventHandler\t@eventHandler','eventHandler="$1"'),
('exclude\t@exclude','exclude="$1"'),
('cluster\t@cluster','cluster="$1"'),
('cluster="true"\tcluster', 'cluster="true"'),
('cluster="false"\tcluster', 'cluster="false"'),
('onMisfire\t@onMisfire','onMisfire="$1"'),
('onMisfire="invokehandler"\tonMisfire', 'onMisfire="invokehandler"'),
('onMisfire="fire_now"\tonMisfire', 'onMisfire="fire_now"'),
('retrycount\t@retrycount','retrycount="$1"'),
('mode\t@mode','mode="$1"'),
('mode="server"\tmode', 'mode="server"'),
('mode="application"\tmode', 'mode="application"'),
('result\t@result','result="$1"'),
('overwrite\t@overwrite','overwrite="$1"'),
('overwrite="true"\toverwrite', 'overwrite="true"'),
('overwrite="false"\toverwrite', 'overwrite="false"')
],
'cfscript':
[

],
'cfsearch':
[
('name\t@name','name="$1"'),
('collection\t@collection','collection="$1"'),
('category\t@category','category="$1"'),
('categorytree\t@categorytree','categorytree="$1"'),
('status\t@status','status="$1"'),
('type\t@type','type="$1"'),
('type="standard"\ttype', 'type="standard"'),
('type="dismax"\ttype', 'type="dismax"'),
('criteria\t@criteria','criteria="$1"'),
('maxrows\t@maxrows','maxrows="$1"'),
('startrow\t@startrow','startrow="$1"'),
('suggestions\t@suggestions','suggestions="$1"'),
('suggestions="always"\tsuggestions', 'suggestions="always"'),
('suggestions="never"\tsuggestions', 'suggestions="never"'),
('contextPassages\t@contextPassages','contextPassages="$1"'),
('contextBytes\t@contextBytes','contextBytes="$1"'),
('contextHighlightBegin\t@contextHighlightBegin','contextHighlightBegin="$1"'),
('contextHighlightBegin="<b>"\tcontextHighlightBegin', 'contextHighlightBegin="<b>"'),
('contextHighlightBegin="<strong>"\tcontextHighlightBegin', 'contextHighlightBegin="<strong>"'),
('contextHighlightBegin="<span class="highlight">"\tcontextHighlightBegin', 'contextHighlightBegin="<span class="highlight">"'),
('contextHighlightEnd\t@contextHighlightEnd','contextHighlightEnd="$1"'),
('contextHighlightEnd="</b>"\tcontextHighlightEnd', 'contextHighlightEnd="</b>"'),
('contextHighlightEnd="</strong>"\tcontextHighlightEnd', 'contextHighlightEnd="</strong>"'),
('contextHighlightEnd="</span>"\tcontextHighlightEnd', 'contextHighlightEnd="</span>"'),
('previousCriteria\t@previousCriteria','previousCriteria="$1"'),
('language\t@language','language="$1"'),
('orderBy\t@orderBy','orderBy="$1"'),
('searchcolumns\t@searchcolumns','searchcolumns="$1"'),
('searchtime\t@searchtime','searchtime="$1"')
],
'cfselect':
[
('name\t@name','name="$1"'),
('id\t@id','id="$1"'),
('bind\t@bind','bind="$1"'),
('bindAttribute\t@bindAttribute','bindAttribute="$1"'),
('bindOnLoad\t@bindOnLoad','bindOnLoad="$1"'),
('bindOnLoad="true"\tbindOnLoad', 'bindOnLoad="true"'),
('bindOnLoad="false"\tbindOnLoad', 'bindOnLoad="false"'),
('editable\t@editable','editable="$1"'),
('editable="true"\teditable', 'editable="true"'),
('editable="false"\teditable', 'editable="false"'),
('label\t@label','label="$1"'),
('style\t@style','style="$1"'),
('sourceForTooltip\t@sourceForTooltip','sourceForTooltip="$1"'),
('size\t@size','size="$1"'),
('required\t@required','required="$1"'),
('required="true"\trequired', 'required="true"'),
('required="false"\trequired', 'required="false"'),
('message\t@message','message="$1"'),
('onerror\t@onerror','onerror="$1"'),
('multiple\t@multiple','multiple="$1"'),
('multiple="true"\tmultiple', 'multiple="true"'),
('multiple="false"\tmultiple', 'multiple="false"'),
('query\t@query','query="$1"'),
('value\t@value','value="$1"'),
('display\t@display','display="$1"'),
('group\t@group','group="$1"'),
('queryposition\t@queryposition','queryposition="$1"'),
('queryposition="above"\tqueryposition', 'queryposition="above"'),
('queryposition="below"\tqueryposition', 'queryposition="below"'),
('selected\t@selected','selected="$1"'),
('onkeyup\t@onkeyup','onkeyup="$1"'),
('onkeydown\t@onkeydown','onkeydown="$1"'),
('onmouseup\t@onmouseup','onmouseup="$1"'),
('onmousedown\t@onmousedown','onmousedown="$1"'),
('onchange\t@onchange','onchange="$1"'),
('onclick\t@onclick','onclick="$1"'),
('enabled\t@enabled','enabled="$1"'),
('enabled="true"\tenabled', 'enabled="true"'),
('enabled="false"\tenabled', 'enabled="false"'),
('visible\t@visible','visible="$1"'),
('visible="true"\tvisible', 'visible="true"'),
('visible="false"\tvisible', 'visible="false"'),
('tooltip\t@tooltip','tooltip="$1"'),
('height\t@height','height="$1"'),
('width\t@width','width="$1"'),
('passthrough\t@passthrough','passthrough="$1"'),
('onbinderror\t@onbinderror','onbinderror="$1"')
],
'cfset':
[

],
'cfsetting':
[
('enablecfoutputonly\t@enablecfoutputonly','enablecfoutputonly="$1"'),
('enablecfoutputonly="true"\tenablecfoutputonly', 'enablecfoutputonly="true"'),
('enablecfoutputonly="false"\tenablecfoutputonly', 'enablecfoutputonly="false"'),
('showdebugoutput\t@showdebugoutput','showdebugoutput="$1"'),
('showdebugoutput="true"\tshowdebugoutput', 'showdebugoutput="true"'),
('showdebugoutput="false"\tshowdebugoutput', 'showdebugoutput="false"'),
('requesttimeout\t@requesttimeout','requesttimeout="$1"')
],
'cfsilent':
[

],
'cfslider':
[
('name\t@name','name="$1"'),
('label\t@label','label="$1"'),
('range\t@range','range="$1"'),
('scale\t@scale','scale="$1"'),
('value\t@value','value="$1"'),
('onvalidate\t@onvalidate','onvalidate="$1"'),
('message\t@message','message="$1"'),
('height\t@height','height="$1"'),
('width\t@width','width="$1"'),
('vspace\t@vspace','vspace="$1"'),
('hspace\t@hspace','hspace="$1"'),
('align\t@align','align="$1"'),
('align="top"\talign', 'align="top"'),
('align="left"\talign', 'align="left"'),
('align="bottom"\talign', 'align="bottom"'),
('align="baseline"\talign', 'align="baseline"'),
('align="texttop"\talign', 'align="texttop"'),
('align="absbottom"\talign', 'align="absbottom"'),
('align="middle"\talign', 'align="middle"'),
('align="absmiddle"\talign', 'align="absmiddle"'),
('align="right"\talign', 'align="right"'),
('lookandfeel\t@lookandfeel','lookandfeel="$1"'),
('lookandfeel="motif"\tlookandfeel', 'lookandfeel="motif"'),
('lookandfeel="windows"\tlookandfeel', 'lookandfeel="windows"'),
('lookandfeel="metal"\tlookandfeel', 'lookandfeel="metal"'),
('vertical\t@vertical','vertical="$1"'),
('vertical="true"\tvertical', 'vertical="true"'),
('vertical="false"\tvertical', 'vertical="false"'),
('bgcolor\t@bgcolor','bgcolor="$1"'),
('bgcolor="black"\tbgcolor', 'bgcolor="black"'),
('bgcolor="red"\tbgcolor', 'bgcolor="red"'),
('bgcolor="blue"\tbgcolor', 'bgcolor="blue"'),
('bgcolor="magenta"\tbgcolor', 'bgcolor="magenta"'),
('bgcolor="cyan"\tbgcolor', 'bgcolor="cyan"'),
('bgcolor="orange"\tbgcolor', 'bgcolor="orange"'),
('bgcolor="darkgray"\tbgcolor', 'bgcolor="darkgray"'),
('bgcolor="pink"\tbgcolor', 'bgcolor="pink"'),
('bgcolor="gray"\tbgcolor', 'bgcolor="gray"'),
('bgcolor="white"\tbgcolor', 'bgcolor="white"'),
('bgcolor="lightgray"\tbgcolor', 'bgcolor="lightgray"'),
('bgcolor="yellow"\tbgcolor', 'bgcolor="yellow"'),
('textcolor\t@textcolor','textcolor="$1"'),
('textcolor="black"\ttextcolor', 'textcolor="black"'),
('textcolor="red"\ttextcolor', 'textcolor="red"'),
('textcolor="blue"\ttextcolor', 'textcolor="blue"'),
('textcolor="magenta"\ttextcolor', 'textcolor="magenta"'),
('textcolor="cyan"\ttextcolor', 'textcolor="cyan"'),
('textcolor="orange"\ttextcolor', 'textcolor="orange"'),
('textcolor="darkgray"\ttextcolor', 'textcolor="darkgray"'),
('textcolor="pink"\ttextcolor', 'textcolor="pink"'),
('textcolor="gray"\ttextcolor', 'textcolor="gray"'),
('textcolor="white"\ttextcolor', 'textcolor="white"'),
('textcolor="lightgray"\ttextcolor', 'textcolor="lightgray"'),
('textcolor="yellow"\ttextcolor', 'textcolor="yellow"'),
('font\t@font','font="$1"'),
('font="arial"\tfont', 'font="arial"'),
('font="times"\tfont', 'font="times"'),
('font="courier"\tfont', 'font="courier"'),
('font="arialunicodems"\tfont', 'font="arialunicodems"'),
('fontsize\t@fontsize','fontsize="$1"'),
('italic\t@italic','italic="$1"'),
('italic="true"\titalic', 'italic="true"'),
('italic="false"\titalic', 'italic="false"'),
('bold\t@bold','bold="$1"'),
('bold="true"\tbold', 'bold="true"'),
('bold="false"\tbold', 'bold="false"'),
('notsupported\t@notsupported','notsupported="$1"'),
('clickToChange\t@clickToChange','clickToChange="$1"'),
('clickToChange="true"\tclickToChange', 'clickToChange="true"'),
('clickToChange="false"\tclickToChange', 'clickToChange="false"'),
('max\t@max','max="$1"'),
('onChange\t@onChange','onChange="$1"'),
('min\t@min','min="$1"'),
('onDrag\t@onDrag','onDrag="$1"'),
('onError\t@onError','onError="$1"'),
('increment\t@increment','increment="$1"'),
('tip\t@tip','tip="$1"'),
('tip="true"\ttip', 'tip="true"'),
('tip="false"\ttip', 'tip="false"'),
('format\t@format','format="$1"'),
('format="html"\tformat', 'format="html"'),
('format="applet"\tformat', 'format="applet"')
],
'cfstoredproc':
[
('procedure\t@procedure','procedure="$1"'),
('datasource\t@datasource','datasource="$1"'),
('username\t@username','username="$1"'),
('password\t@password','password="$1"'),
('blockfactor\t@blockfactor','blockfactor="$1"'),
('debug\t@debug','debug="$1"'),
('debug="true"\tdebug', 'debug="true"'),
('debug="false"\tdebug', 'debug="false"'),
('returncode\t@returncode','returncode="$1"'),
('returncode="true"\treturncode', 'returncode="true"'),
('returncode="false"\treturncode', 'returncode="false"'),
('result\t@result','result="$1"'),
('fetchclientinfo\t@fetchclientinfo','fetchclientinfo="$1"'),
('clientinfo\t@clientinfo','clientinfo="$1"'),
('timeout\t@timeout','timeout="$1"')
],
'cfswitch':
[
('expression\t@expression','expression="$1"')
],
'cftable':
[
('query\t@query','query="$1"'),
('maxrows\t@maxrows','maxrows="$1"'),
('colSpacing\t@colSpacing','colSpacing="$1"'),
('headerLines\t@headerLines','headerLines="$1"'),
('htmltable\t@htmltable','htmltable="$1"'),
('border\t@border','border="$1"'),
('colheaders\t@colheaders','colheaders="$1"'),
('startrow\t@startrow','startrow="$1"')
],
'cftextarea':
[
('name\t@name','name="$1"'),
('label\t@label','label="$1"'),
('style\t@style','style="$1"'),
('required\t@required','required="$1"'),
('required="true"\trequired', 'required="true"'),
('required="false"\trequired', 'required="false"'),
('html\t@html','html="$1"'),
('html="true"\thtml', 'html="true"'),
('html="false"\thtml', 'html="false"'),
('validate\t@validate','validate="$1"'),
('validateat\t@validateat','validateat="$1"'),
('validateat="onsubmit"\tvalidateat', 'validateat="onsubmit"'),
('validateat="onserver"\tvalidateat', 'validateat="onserver"'),
('validateat="onblur"\tvalidateat', 'validateat="onblur"'),
('message\t@message','message="$1"'),
('range\t@range','range="$1"'),
('maxlength\t@maxlength','maxlength="$1"'),
('pattern\t@pattern','pattern="$1"'),
('onvalidate\t@onvalidate','onvalidate="$1"'),
('onerror\t@onerror','onerror="$1"'),
('disabled\t@disabled','disabled="$1"'),
('disabled="true"\tdisabled', 'disabled="true"'),
('disabled="false"\tdisabled', 'disabled="false"'),
('value\t@value','value="$1"'),
('bind\t@bind','bind="$1"'),
('onkeyup\t@onkeyup','onkeyup="$1"'),
('onkeydown\t@onkeydown','onkeydown="$1"'),
('onmouseup\t@onmouseup','onmouseup="$1"'),
('onmousedown\t@onmousedown','onmousedown="$1"'),
('onchange\t@onchange','onchange="$1"'),
('onclick\t@onclick','onclick="$1"'),
('enabled\t@enabled','enabled="$1"'),
('enabled="true"\tenabled', 'enabled="true"'),
('enabled="false"\tenabled', 'enabled="false"'),
('visible\t@visible','visible="$1"'),
('visible="true"\tvisible', 'visible="true"'),
('visible="false"\tvisible', 'visible="false"'),
('tooltip\t@tooltip','tooltip="$1"'),
('height\t@height','height="$1"'),
('width\t@width','width="$1"'),
('basepath\t@basepath','basepath="$1"'),
('bindattribute\t@bindattribute','bindattribute="$1"'),
('bindonload\t@bindonload','bindonload="$1"'),
('bindonload="true"\tbindonload', 'bindonload="true"'),
('bindonload="false"\tbindonload', 'bindonload="false"'),
('fontformats\t@fontformats','fontformats="$1"'),
('fontnames\t@fontnames','fontnames="$1"'),
('fontsizes\t@fontsizes','fontsizes="$1"'),
('onbinderror\t@onbinderror','onbinderror="$1"'),
('richtext\t@richtext','richtext="$1"'),
('richtext="true"\trichtext', 'richtext="true"'),
('richtext="false"\trichtext', 'richtext="false"'),
('skin\t@skin','skin="$1"'),
('skin="default"\tskin', 'skin="default"'),
('skin="silver"\tskin', 'skin="silver"'),
('skin="office2003"\tskin', 'skin="office2003"'),
('wrap\t@wrap','wrap="$1"'),
('wrap="hard"\twrap', 'wrap="hard"'),
('wrap="off"\twrap', 'wrap="off"'),
('wrap="physical"\twrap', 'wrap="physical"'),
('wrap="virtual"\twrap', 'wrap="virtual"'),
('wrap="soft"\twrap', 'wrap="soft"'),
('sourcefortooltip\t@sourcefortooltip','sourcefortooltip="$1"'),
('stylesxml\t@stylesxml','stylesxml="$1"'),
('templatesxml\t@templatesxml','templatesxml="$1"'),
('toolbar\t@toolbar','toolbar="$1"'),
('toolbaronfocus\t@toolbaronfocus','toolbaronfocus="$1"'),
('secureUpload\t@secureUpload','secureUpload="$1"'),
('secureUpload="true"\tsecureUpload', 'secureUpload="true"'),
('secureUpload="false"\tsecureUpload', 'secureUpload="false"')
],
'cftextinput':
[
('name\t@name','name="$1"'),
('value\t@value','value="$1"'),
('required\t@required','required="$1"'),
('required="true"\trequired', 'required="true"'),
('required="false"\trequired', 'required="false"'),
('range\t@range','range="$1"'),
('validate\t@validate','validate="$1"'),
('validate="date"\tvalidate', 'validate="date"'),
('validate="eurodate"\tvalidate', 'validate="eurodate"'),
('validate="time"\tvalidate', 'validate="time"'),
('validate="float"\tvalidate', 'validate="float"'),
('validate="integer"\tvalidate', 'validate="integer"'),
('validate="telephone"\tvalidate', 'validate="telephone"'),
('validate="zipcode"\tvalidate', 'validate="zipcode"'),
('validate="creditcard"\tvalidate', 'validate="creditcard"'),
('validate="social_security_number"\tvalidate', 'validate="social_security_number"'),
('validate="regular_expression"\tvalidate', 'validate="regular_expression"'),
('onvalidate\t@onvalidate','onvalidate="$1"'),
('pattern\t@pattern','pattern="$1"'),
('message\t@message','message="$1"'),
('onerror\t@onerror','onerror="$1"'),
('size\t@size','size="$1"'),
('font\t@font','font="$1"'),
('font="arial"\tfont', 'font="arial"'),
('font="times"\tfont', 'font="times"'),
('font="courier"\tfont', 'font="courier"'),
('font="arialunicodems"\tfont', 'font="arialunicodems"'),
('fontsize\t@fontsize','fontsize="$1"'),
('italic\t@italic','italic="$1"'),
('italic="true"\titalic', 'italic="true"'),
('italic="false"\titalic', 'italic="false"'),
('bold\t@bold','bold="$1"'),
('bold="true"\tbold', 'bold="true"'),
('bold="false"\tbold', 'bold="false"'),
('height\t@height','height="$1"'),
('width\t@width','width="$1"'),
('vspace\t@vspace','vspace="$1"'),
('hspace\t@hspace','hspace="$1"'),
('align\t@align','align="$1"'),
('align="top"\talign', 'align="top"'),
('align="left"\talign', 'align="left"'),
('align="bottom"\talign', 'align="bottom"'),
('align="baseline"\talign', 'align="baseline"'),
('align="texttop"\talign', 'align="texttop"'),
('align="absbottom"\talign', 'align="absbottom"'),
('align="middle"\talign', 'align="middle"'),
('align="absmiddle"\talign', 'align="absmiddle"'),
('align="right"\talign', 'align="right"'),
('bgcolor\t@bgcolor','bgcolor="$1"'),
('bgcolor="black"\tbgcolor', 'bgcolor="black"'),
('bgcolor="red"\tbgcolor', 'bgcolor="red"'),
('bgcolor="blue"\tbgcolor', 'bgcolor="blue"'),
('bgcolor="magenta"\tbgcolor', 'bgcolor="magenta"'),
('bgcolor="cyan"\tbgcolor', 'bgcolor="cyan"'),
('bgcolor="orange"\tbgcolor', 'bgcolor="orange"'),
('bgcolor="darkgray"\tbgcolor', 'bgcolor="darkgray"'),
('bgcolor="pink"\tbgcolor', 'bgcolor="pink"'),
('bgcolor="gray"\tbgcolor', 'bgcolor="gray"'),
('bgcolor="white"\tbgcolor', 'bgcolor="white"'),
('bgcolor="lightgray"\tbgcolor', 'bgcolor="lightgray"'),
('bgcolor="yellow"\tbgcolor', 'bgcolor="yellow"'),
('textcolor\t@textcolor','textcolor="$1"'),
('textcolor="black"\ttextcolor', 'textcolor="black"'),
('textcolor="red"\ttextcolor', 'textcolor="red"'),
('textcolor="blue"\ttextcolor', 'textcolor="blue"'),
('textcolor="magenta"\ttextcolor', 'textcolor="magenta"'),
('textcolor="cyan"\ttextcolor', 'textcolor="cyan"'),
('textcolor="orange"\ttextcolor', 'textcolor="orange"'),
('textcolor="darkgray"\ttextcolor', 'textcolor="darkgray"'),
('textcolor="pink"\ttextcolor', 'textcolor="pink"'),
('textcolor="gray"\ttextcolor', 'textcolor="gray"'),
('textcolor="white"\ttextcolor', 'textcolor="white"'),
('textcolor="lightgray"\ttextcolor', 'textcolor="lightgray"'),
('textcolor="yellow"\ttextcolor', 'textcolor="yellow"'),
('maxlength\t@maxlength','maxlength="$1"'),
('notsupported\t@notsupported','notsupported="$1"'),
('label\t@label','label="$1"')
],
'cfthrow':
[
('type\t@type','type="$1"'),
('type="application"\ttype', 'type="application"'),
('message\t@message','message="$1"'),
('detail\t@detail','detail="$1"'),
('errorcode\t@errorcode','errorcode="$1"'),
('extendedinfo\t@extendedinfo','extendedinfo="$1"'),
('object\t@object','object="$1"')
],
'cftimer':
[
('label\t@label','label="$1"'),
('type\t@type','type="$1"'),
('type="inline"\ttype', 'type="inline"'),
('type="outline"\ttype', 'type="outline"'),
('type="comment"\ttype', 'type="comment"'),
('type="debug"\ttype', 'type="debug"')
],
'cftrace':
[
('abort\t@abort','abort="$1"'),
('abort="true"\tabort', 'abort="true"'),
('abort="false"\tabort', 'abort="false"'),
('category\t@category','category="$1"'),
('inline\t@inline','inline="$1"'),
('inline="true"\tinline', 'inline="true"'),
('inline="false"\tinline', 'inline="false"'),
('text\t@text','text="$1"'),
('type\t@type','type="$1"'),
('type="information"\ttype', 'type="information"'),
('type="warning"\ttype', 'type="warning"'),
('type="error"\ttype', 'type="error"'),
('type="fatal information"\ttype', 'type="fatal information"'),
('var\t@var','var="$1"')
],
'cftransaction':
[
('action\t@action','action="$1"'),
('action="begin"\taction', 'action="begin"'),
('action="commit"\taction', 'action="commit"'),
('action="rollback"\taction', 'action="rollback"'),
('action="setsavepoint"\taction', 'action="setsavepoint"'),
('isolation\t@isolation','isolation="$1"'),
('isolation="read_uncommitted"\tisolation', 'isolation="read_uncommitted"'),
('isolation="read_committed"\tisolation', 'isolation="read_committed"'),
('isolation="repeatable_read"\tisolation', 'isolation="repeatable_read"'),
('isolation="serializable"\tisolation', 'isolation="serializable"'),
('savepoint\t@savepoint','savepoint="$1"'),
('nested\t@nested','nested="$1"'),
('nested="true"\tnested', 'nested="true"'),
('nested="false"\tnested', 'nested="false"')
],
'cftree':
[
('name\t@name','name="$1"'),
('format\t@format','format="$1"'),
('format="applet"\tformat', 'format="applet"'),
('format="flash"\tformat', 'format="flash"'),
('format="html"\tformat', 'format="html"'),
('format="object"\tformat', 'format="object"'),
('format="xml"\tformat', 'format="xml"'),
('required\t@required','required="$1"'),
('required="true"\trequired', 'required="true"'),
('required="false"\trequired', 'required="false"'),
('delimiter\t@delimiter','delimiter="$1"'),
('delimiter="\\"\tdelimiter', 'delimiter="\\"'),
('delimiter=","\tdelimiter', 'delimiter=","'),
('delimiter=";"\tdelimiter', 'delimiter=";"'),
('delimiter="|"\tdelimiter', 'delimiter="|"'),
('delimiter=":"\tdelimiter', 'delimiter=":"'),
('completepath\t@completepath','completepath="$1"'),
('completepath="true"\tcompletepath', 'completepath="true"'),
('completepath="false"\tcompletepath', 'completepath="false"'),
('appendkey\t@appendkey','appendkey="$1"'),
('appendkey="true"\tappendkey', 'appendkey="true"'),
('appendkey="false"\tappendkey', 'appendkey="false"'),
('highlighthref\t@highlighthref','highlighthref="$1"'),
('highlighthref="true"\thighlighthref', 'highlighthref="true"'),
('highlighthref="false"\thighlighthref', 'highlighthref="false"'),
('onvalidate\t@onvalidate','onvalidate="$1"'),
('message\t@message','message="$1"'),
('onerror\t@onerror','onerror="$1"'),
('lookandfeel\t@lookandfeel','lookandfeel="$1"'),
('lookandfeel="motif"\tlookandfeel', 'lookandfeel="motif"'),
('lookandfeel="windows"\tlookandfeel', 'lookandfeel="windows"'),
('lookandfeel="metal"\tlookandfeel', 'lookandfeel="metal"'),
('font\t@font','font="$1"'),
('font="arial"\tfont', 'font="arial"'),
('font="times"\tfont', 'font="times"'),
('font="courier"\tfont', 'font="courier"'),
('font="arialunicodems"\tfont', 'font="arialunicodems"'),
('fontsize\t@fontsize','fontsize="$1"'),
('italic\t@italic','italic="$1"'),
('italic="true"\titalic', 'italic="true"'),
('italic="false"\titalic', 'italic="false"'),
('bold\t@bold','bold="$1"'),
('bold="true"\tbold', 'bold="true"'),
('bold="false"\tbold', 'bold="false"'),
('height\t@height','height="$1"'),
('width\t@width','width="$1"'),
('vspace\t@vspace','vspace="$1"'),
('hspace\t@hspace','hspace="$1"'),
('align\t@align','align="$1"'),
('align="top"\talign', 'align="top"'),
('align="left"\talign', 'align="left"'),
('align="bottom"\talign', 'align="bottom"'),
('align="baseline"\talign', 'align="baseline"'),
('align="texttop"\talign', 'align="texttop"'),
('align="absbottom"\talign', 'align="absbottom"'),
('align="middle"\talign', 'align="middle"'),
('align="absmiddle"\talign', 'align="absmiddle"'),
('align="right"\talign', 'align="right"'),
('border\t@border','border="$1"'),
('border="true"\tborder', 'border="true"'),
('border="false"\tborder', 'border="false"'),
('hscroll\t@hscroll','hscroll="$1"'),
('hscroll="true"\thscroll', 'hscroll="true"'),
('hscroll="false"\thscroll', 'hscroll="false"'),
('vscroll\t@vscroll','vscroll="$1"'),
('vscroll="true"\tvscroll', 'vscroll="true"'),
('vscroll="false"\tvscroll', 'vscroll="false"'),
('style\t@style','style="$1"'),
('enabled\t@enabled','enabled="$1"'),
('enabled="true"\tenabled', 'enabled="true"'),
('enabled="false"\tenabled', 'enabled="false"'),
('visible\t@visible','visible="$1"'),
('visible="true"\tvisible', 'visible="true"'),
('visible="false"\tvisible', 'visible="false"'),
('tooltip\t@tooltip','tooltip="$1"'),
('onchange\t@onchange','onchange="$1"'),
('onblur\t@onblur','onblur="$1"'),
('onfocus\t@onfocus','onfocus="$1"'),
('notsupported\t@notsupported','notsupported="$1"'),
('cache\t@cache','cache="$1"'),
('cache="true"\tcache', 'cache="true"'),
('cache="false"\tcache', 'cache="false"'),
('label\t@label','label="$1"'),
('value\t@value','value="$1"')
],
'cftreeitem':
[
('bind\t@bind','bind="$1"'),
('value\t@value','value="$1"'),
('display\t@display','display="$1"'),
('parent\t@parent','parent="$1"'),
('img\t@img','img="$1"'),
('img="cd"\timg', 'img="cd"'),
('img="computer"\timg', 'img="computer"'),
('img="document"\timg', 'img="document"'),
('img="element"\timg', 'img="element"'),
('img="folder"\timg', 'img="folder"'),
('img="floppy"\timg', 'img="floppy"'),
('img="fixed"\timg', 'img="fixed"'),
('img="remote"\timg', 'img="remote"'),
('imgopen\t@imgopen','imgopen="$1"'),
('href\t@href','href="$1"'),
('target\t@target','target="$1"'),
('query\t@query','query="$1"'),
('queryAsRoot\t@queryAsRoot','queryAsRoot="$1"'),
('expand\t@expand','expand="$1"'),
('expand="true"\texpand', 'expand="true"'),
('expand="false"\texpand', 'expand="false"'),
('onbinderror\t@onbinderror','onbinderror="$1"')
],
'cftry':
[

],
'cfupdate':
[
('datasource\t@datasource','datasource="$1"'),
('tablename\t@tablename','tablename="$1"'),
('tableowner\t@tableowner','tableowner="$1"'),
('tablequalifier\t@tablequalifier','tablequalifier="$1"'),
('username\t@username','username="$1"'),
('password\t@password','password="$1"'),
('formfields\t@formfields','formfields="$1"'),
('clientinfo\t@clientinfo','clientinfo="$1"')
],
'cfwddx':
[
('action\t@action','action="$1"'),
('action="cfml2wddx"\taction', 'action="cfml2wddx"'),
('action="wddx2cfml"\taction', 'action="wddx2cfml"'),
('action="cfml2js"\taction', 'action="cfml2js"'),
('action="wddx2js"\taction', 'action="wddx2js"'),
('input\t@input','input="$1"'),
('output\t@output','output="$1"'),
('toplevelvariable\t@toplevelvariable','toplevelvariable="$1"'),
('usetimezoneinfo\t@usetimezoneinfo','usetimezoneinfo="$1"'),
('usetimezoneinfo="true"\tusetimezoneinfo', 'usetimezoneinfo="true"'),
('usetimezoneinfo="false"\tusetimezoneinfo', 'usetimezoneinfo="false"'),
('validate\t@validate','validate="$1"'),
('validate="true"\tvalidate', 'validate="true"'),
('validate="false"\tvalidate', 'validate="false"')
],
'cfwindow':
[
('bodyStyle\t@bodyStyle','bodyStyle="$1"'),
('center\t@center','center="$1"'),
('center="true"\tcenter', 'center="true"'),
('center="false"\tcenter', 'center="false"'),
('closable\t@closable','closable="$1"'),
('closable="true"\tclosable', 'closable="true"'),
('closable="false"\tclosable', 'closable="false"'),
('draggable\t@draggable','draggable="$1"'),
('draggable="true"\tdraggable', 'draggable="true"'),
('draggable="false"\tdraggable', 'draggable="false"'),
('headerStyle\t@headerStyle','headerStyle="$1"'),
('height\t@height','height="$1"'),
('initShow\t@initShow','initShow="$1"'),
('initShow="true"\tinitShow', 'initShow="true"'),
('initShow="false"\tinitShow', 'initShow="false"'),
('minHeight\t@minHeight','minHeight="$1"'),
('minWidth\t@minWidth','minWidth="$1"'),
('modal\t@modal','modal="$1"'),
('modal="true"\tmodal', 'modal="true"'),
('modal="false"\tmodal', 'modal="false"'),
('name\t@name','name="$1"'),
('onBindError\t@onBindError','onBindError="$1"'),
('resizable\t@resizable','resizable="$1"'),
('resizable="true"\tresizable', 'resizable="true"'),
('resizable="false"\tresizable', 'resizable="false"'),
('source\t@source','source="$1"'),
('title\t@title','title="$1"'),
('width\t@width','width="$1"'),
('x\t@x','x="$1"'),
('y\t@y','y="$1"'),
('refreshonshow\t@refreshonshow','refreshonshow="$1"'),
('refreshonshow="true"\trefreshonshow', 'refreshonshow="true"'),
('refreshonshow="false"\trefreshonshow', 'refreshonshow="false"'),
('destroyOnClose\t@destroyOnClose','destroyOnClose="$1"'),
('destroyOnClose="true"\tdestroyOnClose', 'destroyOnClose="true"'),
('destroyOnClose="false"\tdestroyOnClose', 'destroyOnClose="false"')
],
'cfxml':
[
('variable\t@variable','variable="$1"'),
('casesensitive\t@casesensitive','casesensitive="$1"'),
('casesensitive="true"\tcasesensitive', 'casesensitive="true"'),
('casesensitive="false"\tcasesensitive', 'casesensitive="false"')
],
'cfajaximport':
[
('scriptsrc\t@scriptsrc','scriptsrc="$1"'),
('csssrc\t@csssrc','csssrc="$1"'),
('tags\t@tags','tags="$1"'),
('params\t@params','params="$1"')
],
'cfmenu':
[
('bgcolor\t@bgcolor','bgcolor="$1"'),
('childstyle\t@childstyle','childstyle="$1"'),
('font\t@font','font="$1"'),
('fontcolor\t@fontcolor','fontcolor="$1"'),
('fontsize\t@fontsize','fontsize="$1"'),
('menustyle\t@menustyle','menustyle="$1"'),
('name\t@name','name="$1"'),
('selectedfontcolor\t@selectedfontcolor','selectedfontcolor="$1"'),
('selecteditemcolor\t@selecteditemcolor','selecteditemcolor="$1"'),
('type\t@type','type="$1"'),
('type="horizontal"\ttype', 'type="horizontal"'),
('type="vertical"\ttype', 'type="vertical"'),
('width\t@width','width="$1"')
],
'cfmenuitem':
[
('display\t@display','display="$1"'),
('childstyle\t@childstyle','childstyle="$1"'),
('divider\t@divider','divider="$1"'),
('divider="true"\tdivider', 'divider="true"'),
('divider="false"\tdivider', 'divider="false"'),
('href\t@href','href="$1"'),
('image\t@image','image="$1"'),
('menustyle\t@menustyle','menustyle="$1"'),
('name\t@name','name="$1"'),
('style\t@style','style="$1"'),
('target\t@target','target="$1"')
],
'cfprint':
[
('source\t@source','source="$1"'),
('attributestruct\t@attributestruct','attributestruct="$1"'),
('copies\t@copies','copies="$1"'),
('jobname\t@jobname','jobname="$1"'),
('orientation\t@orientation','orientation="$1"'),
('orientation="portrait"\torientation', 'orientation="portrait"'),
('orientation="landscape"\torientation', 'orientation="landscape"'),
('orientation="reverse-portrait"\torientation', 'orientation="reverse-portrait"'),
('orientation="reverse-landscape"\torientation', 'orientation="reverse-landscape"'),
('pages\t@pages','pages="$1"'),
('password\t@password','password="$1"'),
('papersize\t@papersize','papersize="$1"'),
('papersize="letter"\tpapersize', 'papersize="letter"'),
('papersize="legal"\tpapersize', 'papersize="legal"'),
('papersize="a4"\tpapersize', 'papersize="a4"'),
('papersize="a5"\tpapersize', 'papersize="a5"'),
('papersize="b4"\tpapersize', 'papersize="b4"'),
('papersize="b5"\tpapersize', 'papersize="b5"'),
('papersize="b4-jis"\tpapersize', 'papersize="b4-jis"'),
('papersize="b5-jis"\tpapersize', 'papersize="b5-jis"'),
('quality\t@quality','quality="$1"'),
('quality="normal"\tquality', 'quality="normal"'),
('quality="draft"\tquality', 'quality="draft"'),
('quality="high"\tquality', 'quality="high"'),
('color\t@color','color="$1"'),
('color="true"\tcolor', 'color="true"'),
('color="false"\tcolor', 'color="false"'),
('coverpage\t@coverpage','coverpage="$1"'),
('coverpage="true"\tcoverpage', 'coverpage="true"'),
('coverpage="false"\tcoverpage', 'coverpage="false"'),
('type\t@type','type="$1"'),
('type="pdf"\ttype', 'type="pdf"'),
('printer\t@printer','printer="$1"'),
('sides\t@sides','sides="$1"'),
('sides="duplex"\tsides', 'sides="duplex"'),
('sides="one-sided"\tsides', 'sides="one-sided"'),
('sides="tumble"\tsides', 'sides="tumble"'),
('sides="two-sided-long-edge"\tsides', 'sides="two-sided-long-edge"'),
('sides="two-sided-short-edge"\tsides', 'sides="two-sided-short-edge"'),
('paper\t@paper','paper="$1"'),
('paper="na-letter"\tpaper', 'paper="na-letter"'),
('paper="na-legal"\tpaper', 'paper="na-legal"'),
('paper="iso-a4"\tpaper', 'paper="iso-a4"'),
('paper="iso-a5"\tpaper', 'paper="iso-a5"'),
('paper="iso-b4"\tpaper', 'paper="iso-b4"'),
('paper="iso-b5"\tpaper', 'paper="iso-b5"'),
('paper="jis-b4"\tpaper', 'paper="jis-b4"'),
('paper="jis-b5"\tpaper', 'paper="jis-b5"'),
('fidelity\t@fidelity','fidelity="$1"'),
('fidelity="true"\tfidelity', 'fidelity="true"'),
('fidelity="false"\tfidelity', 'fidelity="false"')
],
'cfsprydataset':
[
('bind\t@bind','bind="$1"'),
('name\t@name','name="$1"'),
('onbinderror\t@onbinderror','onbinderror="$1"'),
('options\t@options','options="$1"'),
('type\t@type','type="$1"'),
('type="xml"\ttype', 'type="xml"'),
('type="json"\ttype', 'type="json"'),
('xpath\t@xpath','xpath="$1"')
],
'cftooltip':
[
('preventoverlap\t@preventoverlap','preventoverlap="$1"'),
('preventoverlap="true"\tpreventoverlap', 'preventoverlap="true"'),
('preventoverlap="false"\tpreventoverlap', 'preventoverlap="false"'),
('autodismissdelay\t@autodismissdelay','autodismissdelay="$1"'),
('hidedelay\t@hidedelay','hidedelay="$1"'),
('showdelay\t@showdelay','showdelay="$1"'),
('sourcefortooltip\t@sourcefortooltip','sourcefortooltip="$1"'),
('tooltip\t@tooltip','tooltip="$1"'),
('style\t@style','style="$1"')
],
'cfajaxproxy':
[
('cfc\t@cfc','cfc="$1"'),
('jsclassname\t@jsclassname','jsclassname="$1"'),
('bind\t@bind','bind="$1"'),
('onerror\t@onerror','onerror="$1"'),
('onsuccess\t@onsuccess','onsuccess="$1"')
],
'cfexchangecalendar':
[
('action\t@action','action="$1"'),
('action="create"\taction', 'action="create"'),
('action="delete"\taction', 'action="delete"'),
('action="deleteattachments"\taction', 'action="deleteattachments"'),
('action="get"\taction', 'action="get"'),
('action="getattachments"\taction', 'action="getattachments"'),
('action="modify"\taction', 'action="modify"'),
('action="respond"\taction', 'action="respond"'),
('action="getuseravailability"\taction', 'action="getuseravailability"'),
('action="getroomslist"\taction', 'action="getroomslist"'),
('action="getrooms"\taction', 'action="getrooms"'),
('attachmentpath\t@attachmentpath','attachmentpath="$1"'),
('connection\t@connection','connection="$1"'),
('event\t@event','event="$1"'),
('generateUniquefilenames\t@generateUniquefilenames','generateUniquefilenames="$1"'),
('generateUniquefilenames="yes"\tgenerateUniquefilenames', 'generateUniquefilenames="yes"'),
('generateUniquefilenames="no"\tgenerateUniquefilenames', 'generateUniquefilenames="no"'),
('message\t@message','message="$1"'),
('name\t@name','name="$1"'),
('notify\t@notify','notify="$1"'),
('notify="yes"\tnotify', 'notify="yes"'),
('notify="no"\tnotify', 'notify="no"'),
('responseType\t@responseType','responseType="$1"'),
('responseType="accept"\tresponseType', 'responseType="accept"'),
('responseType="decline"\tresponseType', 'responseType="decline"'),
('responseType="tentative"\tresponseType', 'responseType="tentative"'),
('result\t@result','result="$1"'),
('uid\t@uid','uid="$1"'),
('attendees\t@attendees','attendees="$1"'),
('dataRequestType\t@dataRequestType','dataRequestType="$1"'),
('dataRequestType="freebusy"\tdataRequestType', 'dataRequestType="freebusy"'),
('dataRequestType="suggestions"\tdataRequestType', 'dataRequestType="suggestions"'),
('dataRequestType="freebusyandsuggestions"\tdataRequestType', 'dataRequestType="freebusyandsuggestions"'),
('emailaddress\t@emailaddress','emailaddress="$1"'),
('startdate\t@startdate','startdate="$1"'),
('enddate\t@enddate','enddate="$1"'),
('getoccurrence\t@getoccurrence','getoccurrence="$1"')
],
'cfexchangeconnection':
[
('action\t@action','action="$1"'),
('action="open"\taction', 'action="open"'),
('action="close"\taction', 'action="close"'),
('action="getsubfolders"\taction', 'action="getsubfolders"'),
('connection\t@connection','connection="$1"'),
('mailboxName\t@mailboxName','mailboxName="$1"'),
('password\t@password','password="$1"'),
('port\t@port','port="$1"'),
('protocol\t@protocol','protocol="$1"'),
('protocol="http"\tprotocol', 'protocol="http"'),
('protocol="https"\tprotocol', 'protocol="https"'),
('proxyHost\t@proxyHost','proxyHost="$1"'),
('proxyPort\t@proxyPort','proxyPort="$1"'),
('server\t@server','server="$1"'),
('username\t@username','username="$1"'),
('folder\t@folder','folder="$1"'),
('recurse\t@recurse','recurse="$1"'),
('recurse="false"\trecurse', 'recurse="false"'),
('recurse="true"\trecurse', 'recurse="true"'),
('name\t@name','name="$1"'),
('exchangeServerLanguage\t@exchangeServerLanguage','exchangeServerLanguage="$1"'),
('formBasedAuthentication\t@formBasedAuthentication','formBasedAuthentication="$1"'),
('formBasedAuthentication="true"\tformBasedAuthentication', 'formBasedAuthentication="true"'),
('formBasedAuthentication="false"\tformBasedAuthentication', 'formBasedAuthentication="false"'),
('serverversion\t@serverversion','serverversion="$1"'),
('serverversion="2003"\tserverversion', 'serverversion="2003"'),
('serverversion="2007"\tserverversion', 'serverversion="2007"'),
('serverversion="2010"\tserverversion', 'serverversion="2010"')
],
'cfexchangecontact':
[
('action\t@action','action="$1"'),
('action="create"\taction', 'action="create"'),
('action="delete"\taction', 'action="delete"'),
('action="deleteattachments"\taction', 'action="deleteattachments"'),
('action="get"\taction', 'action="get"'),
('action="getattachments"\taction', 'action="getattachments"'),
('action="modify"\taction', 'action="modify"'),
('attachmentPath\t@attachmentPath','attachmentPath="$1"'),
('connection\t@connection','connection="$1"'),
('contact\t@contact','contact="$1"'),
('generateUniqueFilenames\t@generateUniqueFilenames','generateUniqueFilenames="$1"'),
('generateUniqueFilenames="yes"\tgenerateUniqueFilenames', 'generateUniqueFilenames="yes"'),
('generateUniqueFilenames="no"\tgenerateUniqueFilenames', 'generateUniqueFilenames="no"'),
('name\t@name','name="$1"'),
('result\t@result','result="$1"'),
('uid\t@uid','uid="$1"')
],
'cfexchangefilter':
[
('name\t@name','name="$1"'),
('name="alldayevent"\tname', 'name="alldayevent"'),
('name="assistant"\tname', 'name="assistant"'),
('name="attributes"\tname', 'name="attributes"'),
('name="attributes"\tname', 'name="attributes"'),
('name="bcc"\tname', 'name="bcc"'),
('name="billinginfo"\tname', 'name="billinginfo"'),
('name="businesaddress"\tname', 'name="businesaddress"'),
('name="businessfax"\tname', 'name="businessfax"'),
('name="businessphonenumber"\tname', 'name="businessphonenumber"'),
('name="cc"\tname', 'name="cc"'),
('name="companies"\tname', 'name="companies"'),
('name="company"\tname', 'name="company"'),
('name="datecompleted"\tname', 'name="datecompleted"'),
('name="displayas"\tname', 'name="displayas"'),
('name="duedate"\tname', 'name="duedate"'),
('name="duration"\tname', 'name="duration"'),
('name="email1"\tname', 'name="email1"'),
('name="email2"\tname', 'name="email2"'),
('name="email3"\tname', 'name="email3"'),
('name="endtime"\tname', 'name="endtime"'),
('name="firstname"\tname', 'name="firstname"'),
('name="folder"\tname', 'name="folder"'),
('name="fromid"\tname', 'name="fromid"'),
('name="hasattachment"\tname', 'name="hasattachment"'),
('name="homeaddress"\tname', 'name="homeaddress"'),
('name="homephonenumber"\tname', 'name="homephonenumber"'),
('name="importance"\tname', 'name="importance"'),
('name="isread"\tname', 'name="isread"'),
('name="isrecurring"\tname', 'name="isrecurring"'),
('name="jobtitle"\tname', 'name="jobtitle"'),
('name="lastname"\tname', 'name="lastname"'),
('name="location"\tname', 'name="location"'),
('name="mail_id"\tname', 'name="mail_id"'),
('name="mailingaddresstype"\tname', 'name="mailingaddresstype"'),
('name="manager"\tname', 'name="manager"'),
('name="meeting uids"\tname', 'name="meeting uids"'),
('name="meeting_response"\tname', 'name="meeting_response"'),
('name="meetinguid"\tname', 'name="meetinguid"'),
('name="message"\tname', 'name="message"'),
('name="messagetype"\tname', 'name="messagetype"'),
('name="middlename"\tname', 'name="middlename"'),
('name="mileage"\tname', 'name="mileage"'),
('name="mobilephonenumber"\tname', 'name="mobilephonenumber"'),
('name="name"\tname', 'name="name"'),
('name="nickname"\tname', 'name="nickname"'),
('name="office"\tname', 'name="office"'),
('name="optionalattendees"\tname', 'name="optionalattendees"'),
('name="organizer"\tname', 'name="organizer"'),
('name="otheraddress"\tname', 'name="otheraddress"'),
('name="otherphonenumber"\tname', 'name="otherphonenumber"'),
('name="profession"\tname', 'name="profession"'),
('name="requiredattendees"\tname', 'name="requiredattendees"'),
('name="sensitivity"\tname', 'name="sensitivity"'),
('name="spousename"\tname', 'name="spousename"'),
('name="startdate"\tname', 'name="startdate"'),
('name="starttime"\tname', 'name="starttime"'),
('name="status"\tname', 'name="status"'),
('name="subject"\tname', 'name="subject"'),
('name="timereceived"\tname', 'name="timereceived"'),
('name="timesent"\tname', 'name="timesent"'),
('name="toid"\tname', 'name="toid"'),
('name="totalwork"\tname', 'name="totalwork"'),
('name="uid"\tname', 'name="uid"'),
('name="valid"\tname', 'name="valid"'),
('name="webpage"\tname', 'name="webpage"'),
('name="lastmodified"\tname', 'name="lastmodified"'),
('name="recurrenceid"\tname', 'name="recurrenceid"'),
('name="maxrows"\tname', 'name="maxrows"'),
('from\t@from','from="$1"'),
('to\t@to','to="$1"'),
('value\t@value','value="$1"')
],
'cfexchangemail':
[
('action\t@action','action="$1"'),
('action="get"\taction', 'action="get"'),
('action="getattachments"\taction', 'action="getattachments"'),
('action="getmeetinginfo"\taction', 'action="getmeetinginfo"'),
('action="delete"\taction', 'action="delete"'),
('action="deleteattachments"\taction', 'action="deleteattachments"'),
('action="move"\taction', 'action="move"'),
('action="set"\taction', 'action="set"'),
('attachmentPath\t@attachmentPath','attachmentPath="$1"'),
('connection\t@connection','connection="$1"'),
('folder\t@folder','folder="$1"'),
('generateUniqueFilenames\t@generateUniqueFilenames','generateUniqueFilenames="$1"'),
('generateUniqueFilenames="yes"\tgenerateUniqueFilenames', 'generateUniqueFilenames="yes"'),
('generateUniqueFilenames="no"\tgenerateUniqueFilenames', 'generateUniqueFilenames="no"'),
('mailUID\t@mailUID','mailUID="$1"'),
('meetingUID\t@meetingUID','meetingUID="$1"'),
('message\t@message','message="$1"'),
('name\t@name','name="$1"'),
('UID\t@UID','UID="$1"'),
('destinationfolder\t@destinationfolder','destinationfolder="$1"')
],
'cfexchangetask':
[
('action\t@action','action="$1"'),
('action="create"\taction', 'action="create"'),
('action="delete"\taction', 'action="delete"'),
('action="deleteattachments"\taction', 'action="deleteattachments"'),
('action="get"\taction', 'action="get"'),
('action="getattachments"\taction', 'action="getattachments"'),
('action="modify"\taction', 'action="modify"'),
('attachmentPath\t@attachmentPath','attachmentPath="$1"'),
('connection\t@connection','connection="$1"'),
('task\t@task','task="$1"'),
('name\t@name','name="$1"'),
('result\t@result','result="$1"'),
('uid\t@uid','uid="$1"')
],
'cfexchangefolder':
[
('action\t@action','action="$1"'),
('action="getinfo"\taction', 'action="getinfo"'),
('action="getextendedlnfo"\taction', 'action="getextendedlnfo"'),
('action="findsubfolders"\taction', 'action="findsubfolders"'),
('action="create"\taction', 'action="create"'),
('action="copy"\taction', 'action="copy"'),
('action="delete"\taction', 'action="delete"'),
('action="move"\taction', 'action="move"'),
('action="modify"\taction', 'action="modify"'),
('action="empty"\taction', 'action="empty"'),
('name\t@name','name="$1"'),
('folderID\t@folderID','folderID="$1"'),
('folderPath\t@folderPath','folderPath="$1"'),
('pathDelimiter\t@pathDelimiter','pathDelimiter="$1"'),
('parentFolderId\t@parentFolderId','parentFolderId="$1"'),
('connection\t@connection','connection="$1"'),
('result\t@result','result="$1"'),
('destinationFolderID\t@destinationFolderID','destinationFolderID="$1"'),
('sourceFolderID\t@sourceFolderID','sourceFolderID="$1"'),
('deleteType\t@deleteType','deleteType="$1"'),
('deleteType="harddelete"\tdeleteType', 'deleteType="harddelete"'),
('deleteType="softdelete"\tdeleteType', 'deleteType="softdelete"'),
('deleteType="movetodeleteditems"\tdeleteType', 'deleteType="movetodeleteditems"'),
('deleteSubFolders\t@deleteSubFolders','deleteSubFolders="$1"'),
('deleteSubFolders="true"\tdeleteSubFolders', 'deleteSubFolders="true"'),
('deleteSubFolders="false"\tdeleteSubFolders', 'deleteSubFolders="false"'),
('folder\t@folder','folder="$1"'),
('uid\t@uid','uid="$1"')
],
'cfexchangeconversation':
[
('action\t@action','action="$1"'),
('action="get"\taction', 'action="get"'),
('action="setreadstate"\taction', 'action="setreadstate"'),
('action="copy"\taction', 'action="copy"'),
('action="move"\taction', 'action="move"'),
('action="delete"\taction', 'action="delete"'),
('name\t@name','name="$1"'),
('folderID\t@folderID','folderID="$1"'),
('uid\t@uid','uid="$1"'),
('isRead\t@isRead','isRead="$1"'),
('isRead="true"\tisRead', 'isRead="true"'),
('isRead="false"\tisRead', 'isRead="false"'),
('destinationFolderID\t@destinationFolderID','destinationFolderID="$1"'),
('connection\t@connection','connection="$1"'),
('deleteType\t@deleteType','deleteType="$1"'),
('deleteType="harddelete"\tdeleteType', 'deleteType="harddelete"'),
('deleteType="softdelete"\tdeleteType', 'deleteType="softdelete"'),
('deleteType="movetodeleteditems"\tdeleteType', 'deleteType="movetodeleteditems"')
],
'cffeed':
[
('action\t@action','action="$1"'),
('action="create"\taction', 'action="create"'),
('action="read"\taction', 'action="read"'),
('columnMap\t@columnMap','columnMap="$1"'),
('enclosureDir\t@enclosureDir','enclosureDir="$1"'),
('ignoreEnclosureError\t@ignoreEnclosureError','ignoreEnclosureError="$1"'),
('ignoreEnclosureError="true"\tignoreEnclosureError', 'ignoreEnclosureError="true"'),
('ignoreEnclosureError="false"\tignoreEnclosureError', 'ignoreEnclosureError="false"'),
('name\t@name','name="$1"'),
('outputFile\t@outputFile','outputFile="$1"'),
('overwrite\t@overwrite','overwrite="$1"'),
('overwrite="true"\toverwrite', 'overwrite="true"'),
('overwrite="false"\toverwrite', 'overwrite="false"'),
('overwriteEnclosure\t@overwriteEnclosure','overwriteEnclosure="$1"'),
('properties\t@properties','properties="$1"'),
('query\t@query','query="$1"'),
('source\t@source','source="$1"'),
('timeout\t@timeout','timeout="$1"'),
('proxyServer\t@proxyServer','proxyServer="$1"'),
('xmlvar\t@xmlvar','xmlvar="$1"'),
('proxyPort\t@proxyPort','proxyPort="$1"'),
('proxyPassword\t@proxyPassword','proxyPassword="$1"'),
('userAgent\t@userAgent','userAgent="$1"'),
('proxyUser\t@proxyUser','proxyUser="$1"'),
('escapeChars\t@escapeChars','escapeChars="$1"'),
('escapeChars="true"\tescapeChars', 'escapeChars="true"'),
('escapeChars="false"\tescapeChars', 'escapeChars="false"')
],
'cfimage':
[
('action\t@action','action="$1"'),
('action="border"\taction', 'action="border"'),
('action="captcha"\taction', 'action="captcha"'),
('action="convert"\taction', 'action="convert"'),
('action="info"\taction', 'action="info"'),
('action="read"\taction', 'action="read"'),
('action="resize"\taction', 'action="resize"'),
('action="rotate"\taction', 'action="rotate"'),
('action="write"\taction', 'action="write"'),
('action="writetobrowser"\taction', 'action="writetobrowser"'),
('angle\t@angle','angle="$1"'),
('color\t@color','color="$1"'),
('destination\t@destination','destination="$1"'),
('difficulty\t@difficulty','difficulty="$1"'),
('difficulty="high"\tdifficulty', 'difficulty="high"'),
('difficulty="medium"\tdifficulty', 'difficulty="medium"'),
('difficulty="low"\tdifficulty', 'difficulty="low"'),
('fontSize\t@fontSize','fontSize="$1"'),
('format\t@format','format="$1"'),
('format="png"\tformat', 'format="png"'),
('format="jpg"\tformat', 'format="jpg"'),
('format="jpeg"\tformat', 'format="jpeg"'),
('height\t@height','height="$1"'),
('isBase64\t@isBase64','isBase64="$1"'),
('isBase64="yes"\tisBase64', 'isBase64="yes"'),
('isBase64="no"\tisBase64', 'isBase64="no"'),
('name\t@name','name="$1"'),
('overwrite\t@overwrite','overwrite="$1"'),
('overwrite="yes"\toverwrite', 'overwrite="yes"'),
('overwrite="no"\toverwrite', 'overwrite="no"'),
('quality\t@quality','quality="$1"'),
('source\t@source','source="$1"'),
('structName\t@structName','structName="$1"'),
('text\t@text','text="$1"'),
('thickness\t@thickness','thickness="$1"'),
('width\t@width','width="$1"'),
('fonts\t@fonts','fonts="$1"'),
('interpolation\t@interpolation','interpolation="$1"'),
('interpolation="highestquality"\tinterpolation', 'interpolation="highestquality"'),
('interpolation="highquality"\tinterpolation', 'interpolation="highquality"'),
('interpolation="mediumquality"\tinterpolation', 'interpolation="mediumquality"'),
('interpolation="highestperformance"\tinterpolation', 'interpolation="highestperformance"'),
('interpolation="highperformance"\tinterpolation', 'interpolation="highperformance"'),
('interpolation="mediumperformance"\tinterpolation', 'interpolation="mediumperformance"'),
('interpolation="nearest"\tinterpolation', 'interpolation="nearest"'),
('interpolation="bilinear"\tinterpolation', 'interpolation="bilinear"'),
('interpolation="bicubic"\tinterpolation', 'interpolation="bicubic"'),
('interpolation="bessel"\tinterpolation', 'interpolation="bessel"'),
('interpolation="blackman"\tinterpolation', 'interpolation="blackman"'),
('interpolation="hamming"\tinterpolation', 'interpolation="hamming"'),
('interpolation="hanning"\tinterpolation', 'interpolation="hanning"'),
('interpolation="hermite"\tinterpolation', 'interpolation="hermite"'),
('interpolation="lanczos"\tinterpolation', 'interpolation="lanczos"'),
('interpolation="mitchell"\tinterpolation', 'interpolation="mitchell"'),
('interpolation="quadratic"\tinterpolation', 'interpolation="quadratic"')
],
'cfinterface':
[
('displayName\t@displayName','displayName="$1"'),
('extends\t@extends','extends="$1"'),
('hint\t@hint','hint="$1"')
],
'cfpdf':
[
('action\t@action','action="$1"'),
('action="addwatermark"\taction', 'action="addwatermark"'),
('action="deletepages"\taction', 'action="deletepages"'),
('action="getinfo"\taction', 'action="getinfo"'),
('action="merge"\taction', 'action="merge"'),
('action="protect"\taction', 'action="protect"'),
('action="processddx"\taction', 'action="processddx"'),
('action="read"\taction', 'action="read"'),
('action="removewatermark"\taction', 'action="removewatermark"'),
('action="setinfo"\taction', 'action="setinfo"'),
('action="thumbnail"\taction', 'action="thumbnail"'),
('action="write"\taction', 'action="write"'),
('action="extracttext"\taction', 'action="extracttext"'),
('action="extractimage"\taction', 'action="extractimage"'),
('action="addheader"\taction', 'action="addheader"'),
('action="addfooter"\taction', 'action="addfooter"'),
('action="removeheaderfooter"\taction', 'action="removeheaderfooter"'),
('action="optimize"\taction', 'action="optimize"'),
('action="transform"\taction', 'action="transform"'),
('ascending\t@ascending','ascending="$1"'),
('ascending="yes"\tascending', 'ascending="yes"'),
('ascending="no"\tascending', 'ascending="no"'),
('copyfrom\t@copyfrom','copyfrom="$1"'),
('destination\t@destination','destination="$1"'),
('directory\t@directory','directory="$1"'),
('encrypt\t@encrypt','encrypt="$1"'),
('encrypt="rc4_40"\tencrypt', 'encrypt="rc4_40"'),
('encrypt="rc4_128"\tencrypt', 'encrypt="rc4_128"'),
('encrypt="rc4_128m"\tencrypt', 'encrypt="rc4_128m"'),
('encrypt="aes_128"\tencrypt', 'encrypt="aes_128"'),
('encrypt="none"\tencrypt', 'encrypt="none"'),
('flatten\t@flatten','flatten="$1"'),
('flatten="yes"\tflatten', 'flatten="yes"'),
('flatten="no"\tflatten', 'flatten="no"'),
('foreground\t@foreground','foreground="$1"'),
('foreground="yes"\tforeground', 'foreground="yes"'),
('foreground="no"\tforeground', 'foreground="no"'),
('image\t@image','image="$1"'),
('info\t@info','info="$1"'),
('isBase64\t@isBase64','isBase64="$1"'),
('isBase64="yes"\tisBase64', 'isBase64="yes"'),
('isBase64="no"\tisBase64', 'isBase64="no"'),
('keepbookmark\t@keepbookmark','keepbookmark="$1"'),
('keepbookmark="true"\tkeepbookmark', 'keepbookmark="true"'),
('keepbookmark="false"\tkeepbookmark', 'keepbookmark="false"'),
('name\t@name','name="$1"'),
('newOwnerPassword\t@newOwnerPassword','newOwnerPassword="$1"'),
('newUserPassword\t@newUserPassword','newUserPassword="$1"'),
('opacity\t@opacity','opacity="$1"'),
('order\t@order','order="$1"'),
('order="name"\torder', 'order="name"'),
('order="time"\torder', 'order="time"'),
('overwrite\t@overwrite','overwrite="$1"'),
('overwrite="yes"\toverwrite', 'overwrite="yes"'),
('overwrite="no"\toverwrite', 'overwrite="no"'),
('password\t@password','password="$1"'),
('permissions\t@permissions','permissions="$1"'),
('permissions="all"\tpermissions', 'permissions="all"'),
('permissions="allowassembly"\tpermissions', 'permissions="allowassembly"'),
('permissions="allowcopy"\tpermissions', 'permissions="allowcopy"'),
('permissions="allowdegradedprinting"\tpermissions', 'permissions="allowdegradedprinting"'),
('permissions="allowfillin"\tpermissions', 'permissions="allowfillin"'),
('permissions="allowmodifyannotations"\tpermissions', 'permissions="allowmodifyannotations"'),
('permissions="allowmodifycontents"\tpermissions', 'permissions="allowmodifycontents"'),
('permissions="allowprinting"\tpermissions', 'permissions="allowprinting"'),
('permissions="allowscreenreaders"\tpermissions', 'permissions="allowscreenreaders"'),
('permissions="allowsecure"\tpermissions', 'permissions="allowsecure"'),
('permissions="none"\tpermissions', 'permissions="none"'),
('position\t@position','position="$1"'),
('rotation\t@rotation','rotation="$1"'),
('showonprint\t@showonprint','showonprint="$1"'),
('showonprint="yes"\tshowonprint', 'showonprint="yes"'),
('showonprint="no"\tshowonprint', 'showonprint="no"'),
('source\t@source','source="$1"'),
('type\t@type','type="$1"'),
('type="string"\ttype', 'type="string"'),
('type="xml"\ttype', 'type="xml"'),
('version\t@version','version="$1"'),
('version="1.1"\tversion', 'version="1.1"'),
('version="1.2"\tversion', 'version="1.2"'),
('version="1.3"\tversion', 'version="1.3"'),
('version="1.4"\tversion', 'version="1.4"'),
('version="1.5"\tversion', 'version="1.5"'),
('version="1.6"\tversion', 'version="1.6"'),
('transparent\t@transparent','transparent="$1"'),
('transparent="true"\ttransparent', 'transparent="true"'),
('transparent="false"\ttransparent', 'transparent="false"'),
('resolution\t@resolution','resolution="$1"'),
('stoponerror\t@stoponerror','stoponerror="$1"'),
('stoponerror="true"\tstoponerror', 'stoponerror="true"'),
('stoponerror="false"\tstoponerror', 'stoponerror="false"'),
('inputfiles\t@inputfiles','inputfiles="$1"'),
('scale\t@scale','scale="$1"'),
('imageprefix\t@imageprefix','imageprefix="$1"'),
('outputfiles\t@outputfiles','outputfiles="$1"'),
('pages\t@pages','pages="$1"'),
('ddxfile\t@ddxfile','ddxfile="$1"'),
('saveoption\t@saveoption','saveoption="$1"'),
('saveoption="full"\tsaveoption', 'saveoption="full"'),
('saveoption="incremental"\tsaveoption', 'saveoption="incremental"'),
('saveoption="linear"\tsaveoption', 'saveoption="linear"'),
('format\t@format','format="$1"'),
('format="jpg"\tformat', 'format="jpg"'),
('format="tiff"\tformat', 'format="tiff"'),
('format="png"\tformat', 'format="png"'),
('hires\t@hires','hires="$1"'),
('hires="true"\thires', 'hires="true"'),
('hires="false"\thires', 'hires="false"'),
('maxScale\t@maxScale','maxScale="$1"'),
('maxBreadth\t@maxBreadth','maxBreadth="$1"'),
('maxLength\t@maxLength','maxLength="$1"'),
('compressTIFFs\t@compressTIFFs','compressTIFFs="$1"'),
('compressTIFFs="true"\tcompressTIFFs', 'compressTIFFs="true"'),
('compressTIFFs="false"\tcompressTIFFs', 'compressTIFFs="false"'),
('overridepage\t@overridepage','overridepage="$1"'),
('overridepage="true"\toverridepage', 'overridepage="true"'),
('overridepage="false"\toverridepage', 'overridepage="false"'),
('package\t@package','package="$1"'),
('package="true"\tpackage', 'package="true"'),
('package="false"\tpackage', 'package="false"'),
('hScale\t@hScale','hScale="$1"'),
('vScale\t@vScale','vScale="$1"'),
('noBookMarks\t@noBookMarks','noBookMarks="$1"'),
('noBookMarks="true"\tnoBookMarks', 'noBookMarks="true"'),
('noBookMarks="false"\tnoBookMarks', 'noBookMarks="false"'),
('noAttachments\t@noAttachments','noAttachments="$1"'),
('noAttachments="true"\tnoAttachments', 'noAttachments="true"'),
('noAttachments="false"\tnoAttachments', 'noAttachments="false"'),
('noComments\t@noComments','noComments="$1"'),
('noComments="true"\tnoComments', 'noComments="true"'),
('noComments="false"\tnoComments', 'noComments="false"'),
('noJavaScripts\t@noJavaScripts','noJavaScripts="$1"'),
('noJavaScripts="true"\tnoJavaScripts', 'noJavaScripts="true"'),
('noJavaScripts="false"\tnoJavaScripts', 'noJavaScripts="false"'),
('noLinks\t@noLinks','noLinks="$1"'),
('noLinks="true"\tnoLinks', 'noLinks="true"'),
('noLinks="false"\tnoLinks', 'noLinks="false"'),
('noMetadata\t@noMetadata','noMetadata="$1"'),
('noMetadata="true"\tnoMetadata', 'noMetadata="true"'),
('noMetadata="false"\tnoMetadata', 'noMetadata="false"'),
('noThumbnails\t@noThumbnails','noThumbnails="$1"'),
('noThumbnails="true"\tnoThumbnails', 'noThumbnails="true"'),
('noThumbnails="false"\tnoThumbnails', 'noThumbnails="false"'),
('noFonts\t@noFonts','noFonts="$1"'),
('noFonts="true"\tnoFonts', 'noFonts="true"'),
('noFonts="false"\tnoFonts', 'noFonts="false"'),
('algo\t@algo','algo="$1"'),
('algo="bicubic"\talgo', 'algo="bicubic"'),
('algo="bilinear"\talgo', 'algo="bilinear"'),
('algo="nearest_neighbour"\talgo', 'algo="nearest_neighbour"'),
('topMargin\t@topMargin','topMargin="$1"'),
('leftMargin\t@leftMargin','leftMargin="$1"'),
('rightMargin\t@rightMargin','rightMargin="$1"'),
('bottomMargin\t@bottomMargin','bottomMargin="$1"'),
('numberFormat\t@numberFormat','numberFormat="$1"'),
('numberFormat="numeric"\tnumberFormat', 'numberFormat="numeric"'),
('numberFormat="lowercaseroman"\tnumberFormat', 'numberFormat="lowercaseroman"'),
('numberFormat="uppercaseroman"\tnumberFormat', 'numberFormat="uppercaseroman"'),
('align\t@align','align="$1"'),
('align="right"\talign', 'align="right"'),
('align="left"\talign', 'align="left"'),
('align="center"\talign', 'align="center"'),
('honourspaces\t@honourspaces','honourspaces="$1"'),
('honourspaces="true"\thonourspaces', 'honourspaces="true"'),
('honourspaces="false"\thonourspaces', 'honourspaces="false"'),
('addQuads\t@addQuads','addQuads="$1"'),
('addQuads="true"\taddQuads', 'addQuads="true"'),
('addQuads="false"\taddQuads', 'addQuads="false"'),
('text\t@text','text="$1"'),
('text="_pagelabel"\ttext', 'text="_pagelabel"'),
('text="_lastpagelabel"\ttext', 'text="_lastpagelabel"'),
('text="_pagenumber"\ttext', 'text="_pagenumber"'),
('text="_lastpagenumber"\ttext', 'text="_lastpagenumber"'),
('useStructure\t@useStructure','useStructure="$1"'),
('useStructure="true"\tuseStructure', 'useStructure="true"'),
('useStructure="false"\tuseStructure', 'useStructure="false"'),
('jpgdpi\t@jpgdpi','jpgdpi="$1"'),
('encodeAll\t@encodeAll','encodeAll="$1"'),
('encodeAll="true"\tencodeAll', 'encodeAll="true"'),
('encodeAll="false"\tencodeAll', 'encodeAll="false"'),
('charset\t@charset','charset="$1"')
],
'cfpdfform':
[
('action\t@action','action="$1"'),
('action="populate"\taction', 'action="populate"'),
('action="read"\taction', 'action="read"'),
('datafile\t@datafile','datafile="$1"'),
('destination\t@destination','destination="$1"'),
('overwrite\t@overwrite','overwrite="$1"'),
('overwrite="yes"\toverwrite', 'overwrite="yes"'),
('overwrite="no"\toverwrite', 'overwrite="no"'),
('overwritedata\t@overwritedata','overwritedata="$1"'),
('overwritedata="yes"\toverwritedata', 'overwritedata="yes"'),
('overwritedata="no"\toverwritedata', 'overwritedata="no"'),
('result\t@result','result="$1"'),
('source\t@source','source="$1"'),
('xmldata\t@xmldata','xmldata="$1"'),
('xmldata="populate"\txmldata', 'xmldata="populate"'),
('xmldata="read"\txmldata', 'xmldata="read"'),
('name\t@name','name="$1"'),
('fdf\t@fdf','fdf="$1"'),
('fdf="true"\tfdf', 'fdf="true"'),
('fdf="false"\tfdf', 'fdf="false"'),
('fdfData\t@fdfData','fdfData="$1"')
],
'cfpdfformparam':
[
('index\t@index','index="$1"'),
('name\t@name','name="$1"'),
('value\t@value','value="$1"'),
('imagefield\t@imagefield','imagefield="$1"')
],
'cfpdfparam':
[
('password\t@password','password="$1"'),
('source\t@source','source="$1"'),
('pages\t@pages','pages="$1"')
],
'cfpdfsubform':
[
('index\t@index','index="$1"'),
('name\t@name','name="$1"')
],
'cfpresentation':
[
('backgroundColor\t@backgroundColor','backgroundColor="$1"'),
('control\t@control','control="$1"'),
('control="normal"\tcontrol', 'control="normal"'),
('control="brief"\tcontrol', 'control="brief"'),
('controlLocation\t@controlLocation','controlLocation="$1"'),
('controlLocation="right"\tcontrolLocation', 'controlLocation="right"'),
('controlLocation="left"\tcontrolLocation', 'controlLocation="left"'),
('directory\t@directory','directory="$1"'),
('glowColor\t@glowColor','glowColor="$1"'),
('initialTab\t@initialTab','initialTab="$1"'),
('initialTab="outline"\tinitialTab', 'initialTab="outline"'),
('initialTab="search"\tinitialTab', 'initialTab="search"'),
('initialTab="notes"\tinitialTab', 'initialTab="notes"'),
('lightColor\t@lightColor','lightColor="$1"'),
('overwrite\t@overwrite','overwrite="$1"'),
('overwrite="yes"\toverwrite', 'overwrite="yes"'),
('overwrite="no"\toverwrite', 'overwrite="no"'),
('primaryColor\t@primaryColor','primaryColor="$1"'),
('shadowColor\t@shadowColor','shadowColor="$1"'),
('showNotes\t@showNotes','showNotes="$1"'),
('showNotes="yes"\tshowNotes', 'showNotes="yes"'),
('showNotes="no"\tshowNotes', 'showNotes="no"'),
('showOutline\t@showOutline','showOutline="$1"'),
('showOutline="yes"\tshowOutline', 'showOutline="yes"'),
('showOutline="no"\tshowOutline', 'showOutline="no"'),
('showSearch\t@showSearch','showSearch="$1"'),
('showSearch="yes"\tshowSearch', 'showSearch="yes"'),
('showSearch="no"\tshowSearch', 'showSearch="no"'),
('textColor\t@textColor','textColor="$1"'),
('title\t@title','title="$1"'),
('authpassword\t@authpassword','authpassword="$1"'),
('authuser\t@authuser','authuser="$1"'),
('autoplay\t@autoplay','autoplay="$1"'),
('autoplay="false"\tautoplay', 'autoplay="false"'),
('autoplay="true"\tautoplay', 'autoplay="true"'),
('loop\t@loop','loop="$1"'),
('loop="false"\tloop', 'loop="false"'),
('loop="true"\tloop', 'loop="true"'),
('proxypassword\t@proxypassword','proxypassword="$1"'),
('proxyuser\t@proxyuser','proxyuser="$1"'),
('proxyhost\t@proxyhost','proxyhost="$1"'),
('proxyport\t@proxyport','proxyport="$1"'),
('useragent\t@useragent','useragent="$1"'),
('destination\t@destination','destination="$1"'),
('format\t@format','format="$1"'),
('format="html"\tformat', 'format="html"'),
('format="ppt"\tformat', 'format="ppt"')
],
'cfpresentationslide':
[
('audio\t@audio','audio="$1"'),
('bottomMargin\t@bottomMargin','bottomMargin="$1"'),
('duration\t@duration','duration="$1"'),
('notes\t@notes','notes="$1"'),
('presenter\t@presenter','presenter="$1"'),
('rightMargin\t@rightMargin','rightMargin="$1"'),
('scale\t@scale','scale="$1"'),
('src\t@src','src="$1"'),
('title\t@title','title="$1"'),
('topMargin\t@topMargin','topMargin="$1"'),
('video\t@video','video="$1"'),
('advance\t@advance','advance="$1"'),
('advance="auto"\tadvance', 'advance="auto"'),
('advance="never"\tadvance', 'advance="never"'),
('advance="click"\tadvance', 'advance="click"'),
('authpassword\t@authpassword','authpassword="$1"'),
('authuser\t@authuser','authuser="$1"'),
('marginbottom\t@marginbottom','marginbottom="$1"'),
('marginleft\t@marginleft','marginleft="$1"'),
('marginright\t@marginright','marginright="$1"'),
('margintop\t@margintop','margintop="$1"'),
('useragent\t@useragent','useragent="$1"'),
('slides\t@slides','slides="$1"'),
('useexternalprogram\t@useexternalprogram','useexternalprogram="$1"')
],
'cfpresenter':
[
('biography\t@biography','biography="$1"'),
('email\t@email','email="$1"'),
('image\t@image','image="$1"'),
('name\t@name','name="$1"'),
('logo\t@logo','logo="$1"'),
('title\t@title','title="$1"')
],
'cfthread':
[
('action\t@action','action="$1"'),
('action="join"\taction', 'action="join"'),
('action="run"\taction', 'action="run"'),
('action="sleep"\taction', 'action="sleep"'),
('action="terminate"\taction', 'action="terminate"'),
('duration\t@duration','duration="$1"'),
('name\t@name','name="$1"'),
('priority\t@priority','priority="$1"'),
('priority="high"\tpriority', 'priority="high"'),
('priority="low"\tpriority', 'priority="low"'),
('priority="normal"\tpriority', 'priority="normal"'),
('timeout\t@timeout','timeout="$1"')
],
'cfzip':
[
('action\t@action','action="$1"'),
('action="delete"\taction', 'action="delete"'),
('action="list"\taction', 'action="list"'),
('action="read"\taction', 'action="read"'),
('action="readbinary"\taction', 'action="readbinary"'),
('action="unzip"\taction', 'action="unzip"'),
('action="zip"\taction', 'action="zip"'),
('charset\t@charset','charset="$1"'),
('charset="jis"\tcharset', 'charset="jis"'),
('charset="rfc1345"\tcharset', 'charset="rfc1345"'),
('charset="utf-16"\tcharset', 'charset="utf-16"'),
('destination\t@destination','destination="$1"'),
('entrypath\t@entrypath','entrypath="$1"'),
('file\t@file','file="$1"'),
('filter\t@filter','filter="$1"'),
('name\t@name','name="$1"'),
('overwrite\t@overwrite','overwrite="$1"'),
('overwrite="yes"\toverwrite', 'overwrite="yes"'),
('overwrite="no"\toverwrite', 'overwrite="no"'),
('prefix\t@prefix','prefix="$1"'),
('recurse\t@recurse','recurse="$1"'),
('recurse="yes"\trecurse', 'recurse="yes"'),
('recurse="no"\trecurse', 'recurse="no"'),
('showDirectory\t@showDirectory','showDirectory="$1"'),
('showDirectory="yes"\tshowDirectory', 'showDirectory="yes"'),
('showDirectory="no"\tshowDirectory', 'showDirectory="no"'),
('source\t@source','source="$1"'),
('storePath\t@storePath','storePath="$1"'),
('storePath="yes"\tstorePath', 'storePath="yes"'),
('storePath="no"\tstorePath', 'storePath="no"'),
('variable\t@variable','variable="$1"')
],
'cfzipparam':
[
('charset\t@charset','charset="$1"'),
('charset="jis"\tcharset', 'charset="jis"'),
('charset="rfc1345"\tcharset', 'charset="rfc1345"'),
('charset="utf-16"\tcharset', 'charset="utf-16"'),
('content\t@content','content="$1"'),
('entrypath\t@entrypath','entrypath="$1"'),
('filter\t@filter','filter="$1"'),
('prefix\t@prefix','prefix="$1"'),
('recurse\t@recurse','recurse="$1"'),
('recurse="yes"\trecurse', 'recurse="yes"'),
('recurse="no"\trecurse', 'recurse="no"'),
('source\t@source','source="$1"')
],
'cfprogressbar':
[
('width\t@width','width="$1"'),
('height\t@height','height="$1"'),
('bind\t@bind','bind="$1"'),
('oncomplete\t@oncomplete','oncomplete="$1"'),
('name\t@name','name="$1"'),
('duration\t@duration','duration="$1"'),
('interval\t@interval','interval="$1"'),
('style\t@style','style="$1"'),
('style="bgcolor"\tstyle', 'style="bgcolor"'),
('style="progresscolor"\tstyle', 'style="progresscolor"'),
('style="textcolor"\tstyle', 'style="textcolor"'),
('autoDisplay\t@autoDisplay','autoDisplay="$1"'),
('autoDisplay="true"\tautoDisplay', 'autoDisplay="true"'),
('autoDisplay="false"\tautoDisplay', 'autoDisplay="false"'),
('onError\t@onError','onError="$1"')
],
'cfspreadsheet':
[
('password\t@password','password="$1"'),
('sheetname\t@sheetname','sheetname="$1"'),
('action\t@action','action="$1"'),
('action="write"\taction', 'action="write"'),
('action="update"\taction', 'action="update"'),
('action="read"\taction', 'action="read"'),
('rows\t@rows','rows="$1"'),
('overwrite\t@overwrite','overwrite="$1"'),
('overwrite="true"\toverwrite', 'overwrite="true"'),
('overwrite="false"\toverwrite', 'overwrite="false"'),
('src\t@src','src="$1"'),
('filename\t@filename','filename="$1"'),
('columns\t@columns','columns="$1"'),
('columnnames\t@columnnames','columnnames="$1"'),
('query\t@query','query="$1"'),
('sheet\t@sheet','sheet="$1"'),
('headerrow\t@headerrow','headerrow="$1"'),
('name\t@name','name="$1"'),
('format\t@format','format="$1"'),
('format="html"\tformat', 'format="html"'),
('format="csv"\tformat', 'format="csv"'),
('excludeheaderrow\t@excludeheaderrow','excludeheaderrow="$1"'),
('excludeheaderrow="true"\texcludeheaderrow', 'excludeheaderrow="true"'),
('excludeheaderrow="false"\texcludeheaderrow', 'excludeheaderrow="false"')
],
'cfmediaplayer':
[
('width\t@width','width="$1"'),
('height\t@height','height="$1"'),
('fullscreencontrol\t@fullscreencontrol','fullscreencontrol="$1"'),
('fullscreencontrol="false"\tfullscreencontrol', 'fullscreencontrol="false"'),
('fullscreencontrol="true"\tfullscreencontrol', 'fullscreencontrol="true"'),
('hideBorder\t@hideBorder','hideBorder="$1"'),
('hideBorder="false"\thideBorder', 'hideBorder="false"'),
('hideBorder="true"\thideBorder', 'hideBorder="true"'),
('controlbar\t@controlbar','controlbar="$1"'),
('controlbar="false"\tcontrolbar', 'controlbar="false"'),
('controlbar="true"\tcontrolbar', 'controlbar="true"'),
('align\t@align','align="$1"'),
('align="left"\talign', 'align="left"'),
('align="right"\talign', 'align="right"'),
('align="center"\talign', 'align="center"'),
('onload\t@onload','onload="$1"'),
('bgcolor\t@bgcolor','bgcolor="$1"'),
('source\t@source','source="$1"'),
('name\t@name','name="$1"'),
('quality\t@quality','quality="$1"'),
('quality="high"\tquality', 'quality="high"'),
('quality="medium"\tquality', 'quality="medium"'),
('quality="low"\tquality', 'quality="low"'),
('hideTitle\t@hideTitle','hideTitle="$1"'),
('hideTitle="false"\thideTitle', 'hideTitle="false"'),
('hideTitle="true"\thideTitle', 'hideTitle="true"'),
('oncomplete\t@oncomplete','oncomplete="$1"'),
('onstart\t@onstart','onstart="$1"'),
('wmode\t@wmode','wmode="$1"'),
('wmode="opaque"\twmode', 'wmode="opaque"'),
('wmode="transparent"\twmode', 'wmode="transparent"'),
('wmode="window"\twmode', 'wmode="window"'),
('autoPlay\t@autoPlay','autoPlay="$1"'),
('autoPlay="false"\tautoPlay', 'autoPlay="false"'),
('autoPlay="true"\tautoPlay', 'autoPlay="true"'),
('style\t@style','style="$1"'),
('type\t@type','type="$1"'),
('type="flash"\ttype', 'type="flash"'),
('type="html"\ttype', 'type="html"'),
('repeat\t@repeat','repeat="$1"'),
('repeat="true"\trepeat', 'repeat="true"'),
('repeat="false"\trepeat', 'repeat="false"'),
('posterImage\t@posterImage','posterImage="$1"'),
('skin\t@skin','skin="$1"'),
('title\t@title','title="$1"'),
('onerror\t@onerror','onerror="$1"'),
('onpause\t@onpause','onpause="$1"')
],
'cffileupload':
[
('url\t@url','url="$1"'),
('width\t@width','width="$1"'),
('title\t@title','title="$1"'),
('extensionfilter\t@extensionfilter','extensionfilter="$1"'),
('uploadbuttonlabel\t@uploadbuttonlabel','uploadbuttonlabel="$1"'),
('progressbar\t@progressbar','progressbar="$1"'),
('progressbar="true"\tprogressbar', 'progressbar="true"'),
('progressbar="false"\tprogressbar', 'progressbar="false"'),
('height\t@height','height="$1"'),
('maxUploadSize\t@maxUploadSize','maxUploadSize="$1"'),
('maxFileSelect\t@maxFileSelect','maxFileSelect="$1"'),
('style\t@style','style="$1"'),
('bgcolor\t@bgcolor','bgcolor="$1"'),
('addButtonLabel\t@addButtonLabel','addButtonLabel="$1"'),
('name\t@name','name="$1"'),
('oncomplete\t@oncomplete','oncomplete="$1"'),
('onerror\t@onerror','onerror="$1"'),
('clearButtonLabel\t@clearButtonLabel','clearButtonLabel="$1"'),
('deleteButtonLabel\t@deleteButtonLabel','deleteButtonLabel="$1"'),
('align\t@align','align="$1"'),
('align="left"\talign', 'align="left"'),
('align="right"\talign', 'align="right"'),
('align="center"\talign', 'align="center"'),
('align="justify"\talign', 'align="justify"'),
('wmode\t@wmode','wmode="$1"'),
('wmode="opaque"\twmode', 'wmode="opaque"'),
('wmode="transparent"\twmode', 'wmode="transparent"'),
('wmode="window"\twmode', 'wmode="window"'),
('stopOnError\t@stopOnError','stopOnError="$1"'),
('stopOnError="true"\tstopOnError', 'stopOnError="true"'),
('stopOnError="false"\tstopOnError', 'stopOnError="false"'),
('hideUploadButton\t@hideUploadButton','hideUploadButton="$1"'),
('hideUploadButton="true"\thideUploadButton', 'hideUploadButton="true"'),
('hideUploadButton="false"\thideUploadButton', 'hideUploadButton="false"'),
('onUploadComplete\t@onUploadComplete','onUploadComplete="$1"')
],
'cfsharepoint':
[
('password\t@password','password="$1"'),
('action\t@action','action="$1"'),
('action="cancreatedwsurl"\taction', 'action="cancreatedwsurl"'),
('action="createdws"\taction', 'action="createdws"'),
('action="createdwsfolder"\taction', 'action="createdwsfolder"'),
('action="deletedws"\taction', 'action="deletedws"'),
('action="deletedwsfolder"\taction', 'action="deletedwsfolder"'),
('action="finddwsdoc"\taction', 'action="finddwsdoc"'),
('action="getdwsdata"\taction', 'action="getdwsdata"'),
('action="removedwsuser"\taction', 'action="removedwsuser"'),
('action="renamedws"\taction', 'action="renamedws"'),
('action="updatedwsdata"\taction', 'action="updatedwsdata"'),
('action="delete"\taction', 'action="delete"'),
('action="download"\taction', 'action="download"'),
('action="getimaginglistitems"\taction', 'action="getimaginglistitems"'),
('action="getitemsbyids"\taction', 'action="getitemsbyids"'),
('action="listpicturelibrary"\taction', 'action="listpicturelibrary"'),
('action="rename"\taction', 'action="rename"'),
('action="upload"\taction', 'action="upload"'),
('action="addattachment"\taction', 'action="addattachment"'),
('action="addlist"\taction', 'action="addlist"'),
('action="deleteattachment"\taction', 'action="deleteattachment"'),
('action="deletelist"\taction', 'action="deletelist"'),
('action="getattachmentcollection"\taction', 'action="getattachmentcollection"'),
('action="getlist"\taction', 'action="getlist"'),
('action="getlistcollection"\taction', 'action="getlistcollection"'),
('action="getlistitems"\taction', 'action="getlistitems"'),
('action="updatelist"\taction', 'action="updatelist"'),
('action="updatelistitems"\taction', 'action="updatelistitems"'),
('action="query"\taction', 'action="query"'),
('action="queryex"\taction', 'action="queryex"'),
('action="registration"\taction', 'action="registration"'),
('action="status"\taction', 'action="status"'),
('action="addgrouptorole"\taction', 'action="addgrouptorole"'),
('action="addrole"\taction', 'action="addrole"'),
('action="addusercollectiontogroup"\taction', 'action="addusercollectiontogroup"'),
('action="addusercollectiontorole"\taction', 'action="addusercollectiontorole"'),
('action="addusertogroup"\taction', 'action="addusertogroup"'),
('action="getgroupcollection"\taction', 'action="getgroupcollection"'),
('action="getrolecollection"\taction', 'action="getrolecollection"'),
('action="getusercollectionfromrole"\taction', 'action="getusercollectionfromrole"'),
('action="getusercollectionfromrole"\taction', 'action="getusercollectionfromrole"'),
('action="getuserinfo"\taction', 'action="getuserinfo"'),
('action="removerole"\taction', 'action="removerole"'),
('action="removeusercollectionfromgroup"\taction', 'action="removeusercollectionfromgroup"'),
('action="removeuserfromgroup"\taction', 'action="removeuserfromgroup"'),
('action="addview"\taction', 'action="addview"'),
('action="deleteview"\taction', 'action="deleteview"'),
('action="getview"\taction', 'action="getview"'),
('action="getviewcollection"\taction', 'action="getviewcollection"'),
('action="updateview"\taction', 'action="updateview"'),
('login\t@login','login="$1"'),
('params\t@params','params="$1"'),
('domain\t@domain','domain="$1"'),
('username\t@username','username="$1"'),
('name\t@name','name="$1"'),
('wsdl\t@wsdl','wsdl="$1"')
],
'cfmapitem':
[
('longitude\t@longitude','longitude="$1"'),
('address\t@address','address="$1"'),
('tip\t@tip','tip="$1"'),
('latitude\t@latitude','latitude="$1"'),
('name\t@name','name="$1"'),
('showMarkerWindow\t@showMarkerWindow','showMarkerWindow="$1"'),
('showMarkerWindow="true"\tshowMarkerWindow', 'showMarkerWindow="true"'),
('showMarkerWindow="false"\tshowMarkerWindow', 'showMarkerWindow="false"'),
('markerWindowContent\t@markerWindowContent','markerWindowContent="$1"'),
('markerIcon\t@markerIcon','markerIcon="$1"'),
('markerColor\t@markerColor','markerColor="$1"'),
('showmarkerwinodw\t@showmarkerwinodw','showmarkerwinodw="$1"'),
('showuser\t@showuser','showuser="$1"')
],
'cfmap':
[
('width\t@width','width="$1"'),
('centerlongitude\t@centerlongitude','centerlongitude="$1"'),
('centeraddress\t@centeraddress','centeraddress="$1"'),
('continuouszoom\t@continuouszoom','continuouszoom="$1"'),
('continuouszoom="true"\tcontinuouszoom', 'continuouszoom="true"'),
('continuouszoom="false"\tcontinuouszoom', 'continuouszoom="false"'),
('type\t@type','type="$1"'),
('type="map"\ttype', 'type="map"'),
('type="satellite"\ttype', 'type="satellite"'),
('type="hybrid"\ttype', 'type="hybrid"'),
('type="earth"\ttype', 'type="earth"'),
('type="terrain"\ttype', 'type="terrain"'),
('title\t@title','title="$1"'),
('zoomcontrol\t@zoomcontrol','zoomcontrol="$1"'),
('zoomcontrol="none"\tzoomcontrol', 'zoomcontrol="none"'),
('zoomcontrol="small"\tzoomcontrol', 'zoomcontrol="small"'),
('zoomcontrol="large"\tzoomcontrol', 'zoomcontrol="large"'),
('zoomcontrol="small3d"\tzoomcontrol', 'zoomcontrol="small3d"'),
('zoomcontrol="large3d"\tzoomcontrol', 'zoomcontrol="large3d"'),
('tip\t@tip','tip="$1"'),
('tip="true"\ttip', 'tip="true"'),
('tip="false"\ttip', 'tip="false"'),
('overview\t@overview','overview="$1"'),
('overview="true"\toverview', 'overview="true"'),
('overview="false"\toverview', 'overview="false"'),
('hideborder\t@hideborder','hideborder="$1"'),
('hideborder="true"\thideborder', 'hideborder="true"'),
('hideborder="false"\thideborder', 'hideborder="false"'),
('doubleclickzoom\t@doubleclickzoom','doubleclickzoom="$1"'),
('doubleclickzoom="true"\tdoubleclickzoom', 'doubleclickzoom="true"'),
('doubleclickzoom="false"\tdoubleclickzoom', 'doubleclickzoom="false"'),
('key\t@key','key="$1"'),
('collapsible\t@collapsible','collapsible="$1"'),
('collapsible="true"\tcollapsible', 'collapsible="true"'),
('collapsible="false"\tcollapsible', 'collapsible="false"'),
('zoomlevel\t@zoomlevel','zoomlevel="$1"'),
('height\t@height','height="$1"'),
('centerlatitude\t@centerlatitude','centerlatitude="$1"'),
('onload\t@onload','onload="$1"'),
('typecontrol\t@typecontrol','typecontrol="$1"'),
('typecontrol="none"\ttypecontrol', 'typecontrol="none"'),
('typecontrol="basic"\ttypecontrol', 'typecontrol="basic"'),
('typecontrol="advanced"\ttypecontrol', 'typecontrol="advanced"'),
('displayscale\t@displayscale','displayscale="$1"'),
('displayscale="true"\tdisplayscale', 'displayscale="true"'),
('displayscale="false"\tdisplayscale', 'displayscale="false"'),
('name\t@name','name="$1"'),
('scrollwheelzoom\t@scrollwheelzoom','scrollwheelzoom="$1"'),
('scrollwheelzoom="true"\tscrollwheelzoom', 'scrollwheelzoom="true"'),
('scrollwheelzoom="false"\tscrollwheelzoom', 'scrollwheelzoom="false"'),
('markerBind\t@markerBind','markerBind="$1"'),
('showMarkerWindow\t@showMarkerWindow','showMarkerWindow="$1"'),
('showMarkerWindow="true"\tshowMarkerWindow', 'showMarkerWindow="true"'),
('showMarkerWindow="false"\tshowMarkerWindow', 'showMarkerWindow="false"'),
('markerWindowContent\t@markerWindowContent','markerWindowContent="$1"'),
('markerIcon\t@markerIcon','markerIcon="$1"'),
('markerColor\t@markerColor','markerColor="$1"'),
('onError\t@onError','onError="$1"'),
('showCenterMarker\t@showCenterMarker','showCenterMarker="$1"'),
('showCenterMarker="true"\tshowCenterMarker', 'showCenterMarker="true"'),
('showCenterMarker="false"\tshowCenterMarker', 'showCenterMarker="false"'),
('showScale\t@showScale','showScale="$1"'),
('showScale="true"\tshowScale', 'showScale="true"'),
('showScale="false"\tshowScale', 'showScale="false"'),
('showallmarkers\t@showallmarkers','showallmarkers="$1"'),
('showmarkerwinodw\t@showmarkerwinodw','showmarkerwinodw="$1"'),
('showuser\t@showuser','showuser="$1"'),
('initshow\t@initshow','initshow="$1"'),
('initshow="true"\tinitshow', 'initshow="true"'),
('initshow="false"\tinitshow', 'initshow="false"')
],
'cfmessagebox':
[
('labelcancel\t@labelcancel','labelcancel="$1"'),
('callbackHandler\t@callbackHandler','callbackHandler="$1"'),
('labelok\t@labelok','labelok="$1"'),
('title\t@title','title="$1"'),
('type\t@type','type="$1"'),
('type="alert"\ttype', 'type="alert"'),
('type="confirm"\ttype', 'type="confirm"'),
('type="prompt"\ttype', 'type="prompt"'),
('message\t@message','message="$1"'),
('labelno\t@labelno','labelno="$1"'),
('labelyes\t@labelyes','labelyes="$1"'),
('multiline\t@multiline','multiline="$1"'),
('multiline="true"\tmultiline', 'multiline="true"'),
('multiline="false"\tmultiline', 'multiline="false"'),
('name\t@name','name="$1"'),
('bodyStyle\t@bodyStyle','bodyStyle="$1"'),
('buttonType\t@buttonType','buttonType="$1"'),
('buttonType="yesno"\tbuttonType', 'buttonType="yesno"'),
('buttonType="yesnocancel"\tbuttonType', 'buttonType="yesnocancel"'),
('icon\t@icon','icon="$1"'),
('modal\t@modal','modal="$1"'),
('modal="true"\tmodal', 'modal="true"'),
('modal="false"\tmodal', 'modal="false"'),
('width\t@width','width="$1"'),
('x\t@x','x="$1"'),
('y\t@y','y="$1"')
],
'cfwebsocket':
[
('onerror\t@onerror','onerror="$1"'),
('onopen\t@onopen','onopen="$1"'),
('subscribeto\t@subscribeto','subscribeto="$1"'),
('name\t@name','name="$1"'),
('usecfauth\t@usecfauth','usecfauth="$1"'),
('usecfauth="true"\tusecfauth', 'usecfauth="true"'),
('usecfauth="false"\tusecfauth', 'usecfauth="false"'),
('onclose\t@onclose','onclose="$1"'),
('onmessage\t@onmessage','onmessage="$1"')
]
}
# ***********************************************************************************************************************
# ***********************************************************************************************************************
# ***********************************************************************************************************************
# ***********************************************************************************************************************
# ***********************************************************************************************************************
# ***********************************************************************************************************************
# ***********************************************************************************************************************
FUNCTIONS = {
'abs(${1:number})':
[

],
'aCos(${1:number})':
[

],
'ajaxLink("${1:url}")':
[

],
'ajaxOnLoad("${1:functionName}")':
[

],
'applicationStartTime()':
[

],
'applicationStop()':
[

],
'array()':
[

],
'_jsonArray()':
[

],
'arrayAppend(${1:array},${2:value})':
[
('true','true'),
('false','false')
],
'arrayAvg(${1:array})':
[

],
'arrayClear(${1:array})':
[

],
'arrayContains(${1:haystack},${2:needle})':
[

],
'arrayContainsNoCase(${1:haystack},${2:needle})':
[

],
'arrayDelete(${1:array},${2:value})':
[
('scope','"$0"')
],
'arrayDeleteAt(${1:array},${2:position})':
[

],
'arrayFind(${1:array},${2:value_or_closure})':
[

],
'arrayFindAll(${1:array},${2:value_or_closure})':
[

],
'arrayFindAllNoCase(${1:array},${2:value})':
[

],
'arrayEach(${1:array},${2:closure})':
[

],
'arrayFilter(${1:array},${2:filter})':
[

],
'arrayFindNoCase(${1:array},${2:value})':
[

],
'arrayFirst(${1:array})':
[

],
'arrayIndexExists(${1:array},${2:index})':
[

],
'arrayIsDefined(${1:array},${2:index})':
[

],
'arrayLast(${1:array})':
[

],
'arrayInsertAt(${1:array},${2:position},${3:value})':
[

],
'arrayIsEmpty(${1:array})':
[

],
'arrayLen(${1:array})':
[

],
'arrayMax(${1:array})':
[

],
'arrayMid(${1:array},${2:start})':
[
('count','$0')
],
'arrayMin(${1:array})':
[

],
'arrayMerge(${1:array1},${2:array2})':
[
('true','true'),
('false','false')
],
'arrayNew(${1:dimension})':
[

],
'arrayPrepend(${1:array},${2:value})':
[

],
'arrayResize(${1:array},${2:minimum_size})':
[

],
'arrayReverse(${1:array})':
[

],
'arraySet(${1:array},${2:start_pos},${3:end_pos},${4:value})':
[

],
'arraySlice(${1:array},${2:offset})':
[
('length','$0')
],
'arraySort(${1:array},${2:sorttype_or_closure})':
[
('sort_order','"$0"'),
('true','true'),
('false','false')
],
'arraySum(${1:array})':
[

],
'arraySwap(${1:array},${2:position1},${3:position2})':
[

],
'arrayToList(${1:array})':
[
('delimiter','"$0"')
],
'arrayToStruct(${1:array})':
[

],
'asc("${1:string}")':
[

],
'aSin(${1:number})':
[

],
'atn(${1:number})':
[

],
'beat(${1:time})':
[

],
'binaryDecode("${1:encoded_binary}","${2:binaryencoding}")':
[

],
'binaryEncode(${1:binary},"${2:encoding}")':
[

],
'charsetDecode("${1:encoded_binary}","${2:encoding}")':
[

],
'charsetEncode(${1:binary},"${2:encoding}")':
[

],
'bitAnd(${1:number1},${2:number2})':
[

],
'bitMaskClear(${1:number},${2:start},${3:length})':
[

],
'bitMaskRead(${1:number},${2:start},${3:length})':
[

],
'bitMaskSet(${1:number},${2:mask},${3:start},${4:length})':
[

],
'bitNot(${1:number})':
[

],
'bitOr(${1:number1},${2:number2})':
[

],
'bitSHLN(${1:number},${2:count})':
[

],
'bitSHRN(${1:number},${2:count})':
[

],
'bitXor(${1:number1},${2:number2})':
[

],
'cacheClear()':
[
('filter','"$0"'),
('cacheName','"$0"')
],
'cacheCount("${1:cacheName}")':
[

],
'cacheDelete("${1:id}")':
[
('true','true'),
('false','false'),
('cacheName','"$0"')
],
'cacheGet("${1:id}")':
[
('true','true'),
('false','false'),
('cacheName','"$0"')
],
'cacheGetDefaultCacheName("${1:type}")':
[

],
'cacheGetAll()':
[
('filter','"$0"'),
('cacheName','"$0"')
],
'cacheGetAllIds()':
[
('filter','"$0"'),
('cacheName','"$0"')
],
'cacheGetMetadata()':
[
('id','"$0"'),
('cacheName','"$0"')
],
'cacheGetProperties("${1:type}")':
[

],
'cacheKeyExists()':
[
('key','"$0"'),
('cacheName','"$0"')
],
'cacheSetProperties(${1:propsSruct})':
[

],
'cachePut("${1:id}",${2:value})':
[
('timeSpan','$0'),
('idleTime','$0'),
('cacheName','"$0"')
],
'cacheRemove(${1:ids})':
[
('true','true'),
('false','false'),
('cacheName','"$0"')
],
'ceiling(${1:number})':
[

],
'chr(${1:number})':
[

],
'cJustify("${1:string}",${2:length})':
[

],
'compare("${1:string1}","${2:string2}")':
[

],
'compareNoCase("${1:string1}","${2:string2}")':
[

],
'componentInfo(${1:component})':
[

],
'componentCacheClear()':
[

],
'componentCacheList()':
[

],
'cSRFGenerateToken()':
[
('key','"$0"'),
('true','true'),
('false','false')
],
'cSRFVerifyToken()':
[
('token','"$0"'),
('key','"$0"')
],
'ctCacheClear()':
[

],
'ctCacheList()':
[

],
'compress("${1:format}","${2:source}","${3:target}")':
[
('true','true'),
('false','false'),
('mode','"$0"')
],
'cos(${1:number})':
[

],
'createDate(${1:year},${2:month},${3:day})':
[
('timezone','"$0"')
],
'createDateTime(${1:year},${2:month},${3:day},${4:hour},${5:minute},${6:second})':
[
('millis','$0'),
('timezone','"$0"')
],
'_createComponent()':
[

],
'createDynamicProxy(${1:cfc},${2:interfaces})':
[

],
'createObject("${1:type}")':
[
('classname','"$0"'),
('context','$0'),
('arg4','$0')
],
'createODBCDate(${1:date})':
[

],
'createODBCDateTime(${1:date})':
[

],
'createODBCTime(${1:date})':
[

],
'createTime(${1:hour},${2:minute},${3:second})':
[
('millis','$0'),
('timezone','"$0"')
],
'createTimeSpan(${1:days},${2:hours},${3:minutes},${4:seconds})':
[
('milliseconds','$0')
],
'createUUID()':
[

],
'createUniqueId()':
[

],
'createGUID()':
[

],
'datasourceFlushMetaCache("${1:datasourceName}")':
[

],
'dateAdd("${1:datepart}",${2:number},${3:date})':
[

],
'_dateAdd(${1:date},"${2:datepart}",${3:number})':
[

],
'dateCompare(${1:date1},${2:date2})':
[
('datepart','"$0"')
],
'dateConvert("${1:conversion_type}",${2:date})':
[

],
'dateDiff("${1:datepart}",${2:date1},${3:date2})':
[

],
'_dateDiff(${1:date1},${2:date2})':
[
('datepart','"$0"')
],
'dateFormat(${1:date})':
[
('mask','"$0"'),
('timezone','"$0"')
],
'datePart("${1:datepart}",${2:date})':
[
('timezone','"$0"')
],
'_datePart(${1:date},"${2:datepart}")':
[
('timezone','"$0"')
],
'day(${1:date})':
[
('timezone','"$0"')
],
'dayOfWeek(${1:date})':
[
('timezone','"$0"')
],
'lsdayOfWeek(${1:date})':
[
('locale','"$0"'),
('timezone','"$0"')
],
'dayOfWeekAsString(${1:day_of_week})':
[
('locale','"$0"')
],
'dayOfWeekShortAsString(${1:day_of_week})':
[
('locale','"$0"')
],
'dayOfYear(${1:date})':
[
('timezone','"$0"')
],
'daysInMonth(${1:date})':
[
('timezone','"$0"')
],
'daysInYear(${1:date})':
[
('timezone','"$0"')
],
'daysInYear("${1:string}")':
[

],
'decimalFormat(${1:number})':
[

],
'decrementValue(${1:number})':
[

],
'decodeFromURL("${1:string}")':
[

],
'each(${1:collection},${2:closure})':
[

],
'empty(${1:variable})':
[

],
'eSAPIDecode("${1:decodeFrom}","${2:string}")':
[

],
'decrypt("${1:encrypted_string}","${2:key}")':
[
('algorithm','"$0"'),
('encoding','"$0"')
],
'decryptBinary(${1:input},"${2:key}")':
[
('algorithm','"$0"')
],
'deleteClientVariable("${1:name}")':
[

],
'directoryCopy("${1:source}")':
[
('destination','"$0"'),
('true','true'),
('false','false'),
('filter','$0')
],
'directoryCreate("${1:path}")':
[
('true','true'),
('false','false')
],
'directoryDelete("${1:path}")':
[
('true','true'),
('false','false')
],
'directoryExists("${1:path}")':
[
('allowRealPath','$0')
],
'directoryList("${1:path}")':
[
('true','true'),
('false','false'),
('listInfo','"$0"'),
('filter','$0'),
('sort','"$0"')
],
'directoryRename("${1:oldPath}","${2:newPath}")':
[

],
'deserializeJSON("${1:JSONVar}")':
[
('true','true'),
('false','false')
],
'dollarFormat("${1:number}")':
[

],
'dotNetToCFType(${1:input})':
[

],
'_dump(${1:value})':
[
('label','"$0"'),
('true','true'),
('false','false'),
('show','"$0"'),
('hide','"$0"'),
('output','"$0"'),
('format','"$0"'),
('keys','$0'),
('true','true'),
('false','false'),
('true','true'),
('false','false')
],
'dump(${1:value})':
[
('label','"$0"'),
('true','true'),
('false','false'),
('top','$0'),
('show','"$0"'),
('hide','"$0"'),
('output','"$0"'),
('format','"$0"'),
('keys','$0'),
('true','true'),
('false','false'),
('true','true'),
('false','false')
],
'dumpStruct(${1:value})':
[
('top','$0'),
('show','"$0"'),
('hide','"$0"'),
('keys','$0'),
('true','true'),
('false','false'),
('true','true'),
('false','false'),
('label','"$0"')
],
'duplicate(${1:variable_name})':
[
('true','true'),
('false','false')
],
'cfusion_encrypt("${1:string}")':
[
('key','"$0"')
],
'cfusion_decrypt("${1:string}")':
[
('key','"$0"')
],
'encodeForHTML("${1:string}")':
[

],
'encodeForHTMLAttribute("${1:string}")':
[

],
'encodeForCSS("${1:string}")':
[

],
'encodeForJavaScript("${1:string}")':
[

],
'encodeForXML("${1:string}")':
[

],
'encodeForXMLAttribute("${1:string}")':
[

],
'encodeForURL("${1:string}")':
[

],
'encodeForLDAP("${1:string}")':
[

],
'encodeForDN("${1:string}")':
[

],
'encodeForXPath("${1:string}")':
[

],
'eSAPIEncode("${1:encodeFor}","${2:string}")':
[

],
'encrypt("${1:string}","${2:key}")':
[
('algorithm','"$0"'),
('encoding','"$0"')
],
'encryptBinary(${1:bytes},"${2:key}")':
[
('algorithm','"$0"')
],
'entityDelete(${1:name})':
[

],
'entityLoad("${1:name}")':
[
('idOrFilter','$0'),
('uniqueOrOrder','$0'),
('options','$0')
],
'entityLoadByPK("${1:name}")':
[
('id','"$0"'),
('true','true'),
('false','false')
],
'entityLoadByExample()':
[
('sampleEntity','$0'),
('true','true'),
('false','false')
],
'entityMerge(${1:entity})':
[

],
'entityNew()':
[
('entityName','"$0"'),
('properties','$0')
],
'entityNameArray()':
[

],
'entityNameList("${1:delimiter}")':
[

],
'entityReload(${1:entity})':
[

],
'entitySave()':
[
('entity','$0'),
('true','true'),
('false','false')
],
'entityToQuery()':
[
('entity','$0'),
('name','"$0"')
],
'evaluate()':
[

],
'evaluateComponent("${1:name}","${2:md5}",${3:thisData})':
[
('variablesData','$0')
],
'evaluateJava(${1:stringOrBinary})':
[

],
'exp(${1:number})':
[

],
'contractPath("${1:path}")':
[
('true','true'),
('false','false')
],
'expandPath("${1:relative_path}")':
[

],
'extract("${1:format}","${2:source}","${3:target}")':
[

],
'fileAppend("${1:file}",${2:data})':
[
('charset','"$0"')
],
'fileGetMimeType(${1:file})':
[
('true','true'),
('false','false')
],
'fileOpen("${1:path}")':
[
('mode','"$0"'),
('charset','"$0"'),
('true','true'),
('false','false')
],
'fileRead(${1:file})':
[
('charsetOrBufferSize','$0')
],
'fileReadLine(${1:fileObj})':
[

],
'fileSeek(${1:fileObj},${2:pos})':
[

],
'fileSkipBytes(${1:fileObj},${2:len})':
[

],
'fileUpload("${1:destination}")':
[
('fileField','"$0"'),
('accept','"$0"'),
('nameConflict','"$0"'),
('mode','"$0"'),
('attributes','"$0"'),
('acl','$0')
],
'fileUploadAll("${1:destination}")':
[
('accept','"$0"'),
('nameConflict','"$0"'),
('mode','"$0"'),
('attributes','"$0"'),
('acl','$0')
],
'fileClose(${1:fileObj})':
[

],
'fileCopy(${1:source},${2:destination})':
[

],
'fileMove(${1:source},${2:destination})':
[

],
'fileDelete(${1:source})':
[

],
'fileExists(${1:source})':
[
('allowRealPath','$0')
],
'fileIsEOF(${1:source})':
[

],
'fileReadBinary(${1:source})':
[

],
'fileSetAccessMode(${1:source},"${2:mode}")':
[

],
'fileSetAttribute(${1:source},"${2:attribute}")':
[

],
'fileSetLastModified(${1:source},${2:date})':
[

],
'fileWrite(${1:file},${2:data})':
[
('charset','"$0"')
],
'fileWriteLine(${1:file},"${2:data}")':
[

],
'find("${1:substring}","${2:string}")':
[
('start','$0')
],
'findNoCase("${1:substring}","${2:string}")':
[
('start','$0')
],
'findOneOf("${1:set}","${2:string}")':
[
('start','$0')
],
'firstDayOfMonth(${1:date})':
[
('timezone','"$0"')
],
'fix(${1:number})':
[

],
'formatBaseN(${1:number},${2:radix})':
[

],
'generateSecretKey("${1:algorithm}")':
[
('keySize','$0')
],
'getAuthUser()':
[

],
'getApplicationSettings(${1:suppressFunction})':
[

],
'getApplicationMetadata()':
[

],
'getBaseTagData("${1:tagname}")':
[
('instancenumber','$0')
],
'getBaseTagList("${1:delimiter}")':
[

],
'getBaseTemplatePath()':
[

],
'getClassPath()':
[

],
'getComponentMetaData(${1:pathOrCFC})':
[

],
'getContextRoot()':
[

],
'getCPUUsage(${1:time})':
[

],
'getClientVariablesList()':
[

],
'getCurrentTemplatePath()':
[

],
'getCurrentContext()':
[

],
'callStackDump("${1:output}")':
[

],
'callStackGet()':
[

],
'canonicalize("${1:input}",${2:restrictMultiple},${3:restrictMixed})':
[

],
'getFunctionCalledName()':
[

],
'getFreeSpace(${1:filepath})':
[

],
'getTotalSpace(${1:filepath})':
[

],
'getDirectoryFromPath("${1:path}")':
[

],
'getEncoding("${1:scope}")':
[

],
'getException(${1:object})':
[

],
'getFileFromPath("${1:path}")':
[

],
'getFileInfo(${1:file})':
[

],
'getFunctionData("${1:functionName}")':
[

],
'getLocaleDisplayName()':
[
('locale','"$0"'),
('dspLocale','"$0"')
],
'getLocalHostIP()':
[

],
'getVFSMetaData("${1:scheme}")':
[

],
'getPrinterInfo("${1:printer}")':
[

],
'getRailoId()':
[

],
'getReadableImageFormats()':
[

],
'getUserRoles()':
[

],
'getWriteableImageFormats()':
[

],
'getTagData("${1:nameSpaceWithSeperator}","${2:tagName}")':
[

],
'getFunctionList()':
[

],
'getGatewayHelper("${1:gatewayID}")':
[

],
'getTagList()':
[

],
'getHTTPRequestData()':
[

],
'getHttpTimeString(${1:date_time_object})':
[

],
'getK2ServerDocCount()':
[

],
'getK2ServerDocCountLimit()':
[

],
'getLocale()':
[

],
'getMemoryUsage("${1:type}")':
[

],
'getMetadata()':
[
('object','$0'),
('true','true'),
('false','false')
],
'getMetricData("${1:monitor_name}")':
[

],
'getNumericDate(${1:arg1})':
[

],
'getPageContext()':
[

],
'getProfileSections("${1:iniFile}")':
[

],
'getProfileString("${1:iniPath}","${2:section}","${3:entry}")':
[

],
'getSOAPRequest(${1:webservice})':
[

],
'getSOAPRequestHeader("${1:namespace}","${2:name}")':
[
('true','true'),
('false','false')
],
'addSOAPRequestHeader(${1:webservice},"${2:namespace}","${3:name}",${4:value})':
[
('true','true'),
('false','false')
],
'addSOAPResponseHeader("${1:namespace}","${2:name}",${3:value})':
[
('true','true'),
('false','false')
],
'getSOAPResponse(${1:webservice})':
[

],
'getSOAPResponseHeader(${1:webservice},"${2:namespace}","${3:name}")':
[
('true','true'),
('false','false')
],
'getTempDirectory()':
[

],
'getSystemFreeMemory()':
[

],
'getSystemTotalMemory()':
[

],
'getTempFile("${1:dir}","${2:prefix}")':
[

],
'getTemplatePath()':
[

],
'getTickCount("${1:unit}")':
[

],
'getTimeZoneInfo()':
[

],
'getTimeZone()':
[

],
'setTimeZone("${1:timezone}")':
[

],
'getToken("${1:string}",${2:index})':
[
('delimiters','"$0"')
],
'getVariable("${1:name}")':
[

],
'hash(${1:input})':
[
('algorithm','"$0"'),
('encoding','"$0"'),
('numIterations','$0')
],
'hour(${1:Date})':
[
('timezone','"$0"')
],
'hMAC(${1:message},${2:key})':
[
('algorithm','"$0"'),
('encoding','"$0"')
],
'hTMLCodeFormat("${1:string}")':
[
('version','$0')
],
'hTMLEditFormat("${1:string}")':
[
('version','$0')
],
'iIf(${1:condition},"${2:string_expression1}","${3:string_expression2}")':
[

],
'imageAddBorder(${1:name})':
[
('thickness','$0'),
('color','"$0"'),
('borderType','"$0"')
],
'imageBlur(${1:name})':
[
('blurRadius','$0')
],
'imageClearRect(${1:name})':
[
('x','$0'),
('y','$0'),
('width','$0'),
('height','$0')
],
'imageFilterColorMap("${1:type}")':
[
('lineColor1','"$0"'),
('lineColor2','"$0"')
],
'imageFilterKernel(${1:width},${2:height},${3:data})':
[

],
'imageFilterWarpGrid(${1:rows},${2:cols},${3:width},${4:height})':
[

],
'imageFilterCurves()':
[

],
'imageCopy(${1:name},${2:x},${3:y},${4:width},${5:height})':
[
('dx','$0'),
('dy','$0')
],
'imageCrop(${1:name},${2:x},${3:y},${4:width},${5:height})':
[

],
'imageDrawArc(${1:name},${2:x},${3:y},${4:width},${5:height},${6:startAngle},${7:arcAngle})':
[
('true','true'),
('false','false')
],
'imageDrawBeveledRect(${1:name},${2:x},${3:y},${4:width},${5:height})':
[
('true','true'),
('false','false'),
('true','true'),
('false','false')
],
'imageDrawCubicCurve(${1:name},${2:x1},${3:y1},${4:ctrlx1},${5:ctrly1},${6:ctrlx2},${7:ctrly2},${8:x2},${9:y2})':
[

],
'imageDrawImage(${1:name},${2:image},${3:x},${4:y})':
[

],
'imageDrawLine(${1:name},${2:x1},${3:y1},${4:x2},${5:y2})':
[

],
'imageDrawLines(${1:name},${2:xcoords},${3:ycoords})':
[
('true','true'),
('false','false'),
('true','true'),
('false','false')
],
'imageDrawOval(${1:name},${2:x},${3:y},${4:width},${5:height})':
[
('true','true'),
('false','false')
],
'imageDrawPoint(${1:name},${2:x},${3:y})':
[

],
'imageDrawQuadraticCurve(${1:name},${2:x1},${3:y1},${4:ctrlx},${5:ctrly},${6:x2},${7:y2})':
[

],
'imageDrawRect(${1:name},${2:x},${3:y},${4:width},${5:height})':
[
('true','true'),
('false','false')
],
'imageDrawRoundRect(${1:name},${2:x},${3:y},${4:width},${5:height},${6:arcWidth},${7:arcHeight})':
[
('true','true'),
('false','false')
],
'imageDrawText(${1:name},"${2:str}",${3:x},${4:y})':
[
('attributeCollection','$0')
],
'imageFilter(${1:name})':
[
('filtername','"$0"'),
('parameters','$0')
],
'imageFlip(${1:name})':
[
('transpose','"$0"')
],
'imageGetBlob(${1:source})':
[

],
'imageGetBufferedImage(${1:name})':
[

],
'imageGetEXIFMetadata(${1:name})':
[

],
'imageGetEXIFTag(${1:name},"${2:tagName}")':
[

],
'imageGetHeight(${1:name})':
[

],
'imageGetWidth(${1:name})':
[

],
'imageGetIPTCTag(${1:name},"${2:tagName}")':
[

],
'imageGrayscale(${1:name})':
[

],
'imageFormats()':
[

],
'imageFonts()':
[

],
'imageInfo(${1:name})':
[

],
'imageNegative(${1:name})':
[

],
'imageNew()':
[
('source','$0'),
('width','"$0"'),
('height','"$0"'),
('imageType','"$0"'),
('canvasColor','"$0"')
],
'imageOverlay(${1:source1},${2:source2})':
[

],
'imagePaste(${1:image1},${2:image2})':
[
('x','$0'),
('y','$0')
],
'imageReadBase64("${1:b64str}")':
[

],
'imageRead(${1:path})':
[

],
'imageResize(${1:name},"${2:width}")':
[
('height','"$0"'),
('interpolation','"$0"'),
('blurFactor','$0')
],
'imageRotate(${1:name})':
[
('x','"$0"'),
('y','"$0"'),
('angle','"$0"'),
('interpolation','"$0"')
],
'imageRotateDrawingAxis(${1:name})':
[
('angle','$0'),
('x','$0'),
('y','$0')
],
'imageScaleToFit(${1:name})':
[
('fitWidth','"$0"'),
('fitHeight','"$0"'),
('interpolation','"$0"'),
('blurFactor','$0')
],
'imageWrite(${1:name})':
[
('destination','"$0"'),
('quality','$0'),
('true','true'),
('false','false')
],
'imageWriteBase64(${1:name})':
[
('destination','"$0"'),
('format','"$0"'),
('true','true'),
('false','false')
],
'imageSetAntialiasing(${1:name})':
[
('antialias','"$0"')
],
'imageSetBackgroundColor(${1:name})':
[
('color','"$0"')
],
'imageSetDrawingAlpha(${1:name})':
[
('alpha','$0')
],
'imageSetDrawingColor(${1:name})':
[
('color','"$0"')
],
'imageSetDrawingStroke(${1:name})':
[
('attributeCollection','$0')
],
'imageSetDrawingTransparency(${1:name})':
[
('percent','$0')
],
'imageSharpen(${1:name})':
[
('gain','$0')
],
'imageShear(${1:name},${2:shear})':
[
('direction','"$0"'),
('interpolation','"$0"')
],
'imageShearDrawingAxis(${1:name},${2:shx},${3:shy})':
[

],
'imageTranslate(${1:name},${2:xTrans},${3:yTrans})':
[
('interpolation','"$0"')
],
'imageTranslateDrawingAxis(${1:name},${2:x},${3:y})':
[

],
'imageXORDrawingMode(${1:name},"${2:color}")':
[

],
'intergralContext()':
[

],
'invoke(${1:object},"${2:name}")':
[
('arguments','$0')
],
'isClosure(${1:object})':
[

],
'isImage(${1:name})':
[

],
'isImageFile("${1:path}")':
[

],
'isIPInRange(${1:ips},"${2:ip}")':
[

],
'isJson(${1:var})':
[

],
'isIPv6("${1:hostname}")':
[

],
'isPDFFile("${1:path}")':
[

],
'isPDFObject(${1:value})':
[

],
'isZipFile("${1:path}")':
[

],
'incrementValue(${1:number})':
[

],
'inputBaseN("${1:string}",${2:radix})':
[

],
'insert("${1:substring}","${2:string}",${3:position})':
[

],
'int(${1:number})':
[

],
'isArray(${1:value})':
[
('dimension','$0')
],
'isBinary(${1:value})':
[

],
'isBoolean(${1:value})':
[

],
'isCustomFunction(${1:name})':
[

],
'isDate(${1:string})':
[

],
'isDDX("${1:pathOrString}")':
[

],
'isInstanceOf(${1:obj},"${2:type}")':
[

],
'isDebugMode()':
[

],
'isDefined("${1:variable}")':
[

],
'isK2ServerABroker()':
[

],
'isK2ServerDocCountExceeded()':
[

],
'isK2ServerOnline()':
[

],
'isLeapYear(${1:year})':
[

],
'isLocalHost(${1:ip})':
[

],
'isNotMap(${1:obj})':
[

],
'isNull(${1:object})':
[

],
'isNumeric(${1:string})':
[

],
'isNumericDate(${1:number})':
[

],
'isObject(${1:value})':
[

],
'isQuery(${1:value})':
[

],
'isSimpleValue(${1:value})':
[

],
'isSOAPRequest()':
[

],
'isStruct(${1:variable})':
[

],
'isUserInRole(${1:role_name})':
[

],
'isUserInAnyRole("${1:role_list}")':
[

],
'isUserLoggedIn()':
[

],
'isValid("${1:type}",${2:value})':
[
('min_or_pattern','$0'),
('max','$0')
],
'isWddx(${1:value})':
[

],
'isVideoFile("${1:value}")':
[

],
'isXML(${1:value})':
[

],
'isXmlAttribute(${1:value})':
[

],
'isXmlDoc(${1:value})':
[

],
'isXmlElem(${1:value})':
[

],
'isXmlNode(${1:value})':
[

],
'isXmlRoot(${1:value})':
[

],
'javaCast("${1:type}",${2:variable})':
[

],
'jSStringFormat("${1:string}")':
[

],
'lCase("${1:string}")':
[

],
'left("${1:string}",${2:count})':
[

],
'len("${1:value}")':
[

],
'listAppend("${1:list}","${2:value}")':
[
('delimiters','"$0"')
],
'listAvg("${1:list}")':
[
('delimiters','"$0"')
],
'listChangeDelims("${1:list}","${2:new_delimiter}")':
[
('delimiters','"$0"'),
('true','true'),
('false','false')
],
'listCompact("${1:list}")':
[
('delimiters','"$0"')
],
'listContains("${1:list}","${2:substring}")':
[
('delimiters','"$0"'),
('true','true'),
('false','false')
],
'listContainsNoCase("${1:list}","${2:substring}")':
[
('delimiters','"$0"'),
('true','true'),
('false','false')
],
'listDeleteAt("${1:list}",${2:position})':
[
('delimiters','"$0"'),
('true','true'),
('false','false')
],
'listFilter("${1:list}",${2:filter})':
[

],
'listFind("${1:list}","${2:value}")':
[
('delimiters','"$0"'),
('true','true'),
('false','false')
],
'listFindNoCase("${1:list}","${2:value}")':
[
('delimiters','"$0"'),
('true','true'),
('false','false')
],
'listFirst("${1:list}")':
[
('delimiters','"$0"'),
('true','true'),
('false','false')
],
'listGetAt("${1:list}",${2:position})':
[
('delimiters','"$0"'),
('true','true'),
('false','false')
],
'listInsertAt("${1:list}",${2:position},"${3:value}")':
[
('delimiters','"$0"'),
('true','true'),
('false','false')
],
'listIndexExists("${1:list}",${2:index})':
[
('delimiter','"$0"'),
('true','true'),
('false','false')
],
'listItemTrim("${1:list}")':
[
('delimiters','"$0"'),
('true','true'),
('false','false')
],
'listLast("${1:list}")':
[
('delimiters','"$0"'),
('true','true'),
('false','false')
],
'listLen("${1:list}")':
[
('delimiters','"$0"'),
('true','true'),
('false','false')
],
'listPrepend("${1:list}","${2:value}")':
[
('delimiters','"$0"')
],
'listQualify("${1:list}","${2:qualifier}")':
[
('delimiters','"$0"'),
('elements','"$0"'),
('true','true'),
('false','false')
],
'listRest("${1:list}")':
[
('delimiters','"$0"'),
('true','true'),
('false','false')
],
'listRemoveDuplicates("${1:list}")':
[
('delimiters','"$0"')
],
'listSetAt("${1:list}",${2:position},"${3:value}")':
[
('delimiters','"$0"'),
('true','true'),
('false','false')
],
'listSort("${1:list}","${2:sort_type}")':
[
('sort_order','"$0"'),
('delimiters','"$0"'),
('true','true'),
('false','false')
],
'listToArray("${1:list}")':
[
('delimiter','"$0"'),
('true','true'),
('false','false'),
('true','true'),
('false','false')
],
'listTrim("${1:list}")':
[
('delimiters','"$0"')
],
'listValueCount("${1:list}","${2:value}")':
[
('delimiter','"$0"'),
('true','true'),
('false','false')
],
'listValueCountNoCase("${1:list}","${2:value}")':
[
('delimiter','"$0"'),
('true','true'),
('false','false')
],
'lJustify("${1:string}",${2:length})':
[

],
'log(${1:number})':
[

],
'log10(${1:number})':
[

],
'lSCurrencyFormat(${1:number})':
[
('type','"$0"'),
('locale','"$0"')
],
'lSDateFormat(${1:date})':
[
('mask','"$0"'),
('locale','"$0"'),
('timezone','"$0"')
],
'lSDateTimeFormat(${1:date})':
[
('mask','"$0"'),
('locale','"$0"'),
('timezone','"$0"')
],
'lSEuroCurrencyFormat(${1:currency_number})':
[
('type','"$0"'),
('locale','"$0"')
],
'lSIsCurrency("${1:string}")':
[
('locale','"$0"')
],
'lSIsDate(${1:string})':
[
('locale','"$0"'),
('timezone','"$0"')
],
'lSIsNumeric("${1:string}")':
[
('locale','"$0"')
],
'lSNumberFormat(${1:number})':
[
('mask','"$0"'),
('locale','"$0"')
],
'lSParseCurrency("${1:string}")':
[
('locale','"$0"')
],
'lSParseDateTime(${1:date})':
[
('locale','"$0"'),
('timezone','"$0"'),
('format','"$0"')
],
'lSParseEuroCurrency("${1:currency_string}")':
[
('locale','"$0"')
],
'lSParseNumber("${1:string}")':
[
('locale','"$0"')
],
'lSTimeFormat(${1:time})':
[
('mask','"$0"'),
('locale','"$0"'),
('timezone','"$0"')
],
'lTrim("${1:string}")':
[

],
'max(${1:number1},${2:number2})':
[

],
'metaphone("${1:str}")':
[

],
'mid("${1:string}",${2:start})':
[
('count','$0')
],
'min(${1:number1},${2:number2})':
[

],
'minute(${1:date})':
[
('timezone','"$0"')
],
'millisecond(${1:date})':
[
('timezone','"$0"')
],
'month(${1:Date})':
[
('timezone','"$0"')
],
'monthAsString(${1:monthnumber})':
[
('locale','"$0"')
],
'monthShortAsString(${1:monthnumber})':
[

],
'newLine()':
[

],
'now()':
[

],
'nowServer()':
[

],
'numberFormat(${1:number})':
[
('mask','"$0"')
],
'nullValue()':
[

],
'objectEquals()':
[
('left','$0'),
('right','$0')
],
'objectLoad(${1:input})':
[

],
'objectSave()':
[
('input','$0'),
('filepath','"$0"')
],
'ORMExecuteQuery()':
[
('hql','"$0"'),
('paramsOrUnique','$0'),
('uniqueOrQueryOptions','$0'),
('queryOptions','$0')
],
'ORMClearSession()':
[

],
'ORMCloseSession()':
[

],
'ORMEvictCollection()':
[
('entityName','$0'),
('collectionName','$0'),
('primaryKey','$0')
],
'ORMEvictEntity()':
[
('entityName','$0'),
('primaryKey','$0')
],
'ORMEvictQueries(${1:cacheName})':
[

],
'ORMFlush()':
[

],
'ORMGetSession()':
[

],
'ORMGetSessionFactory()':
[

],
'ORMReload()':
[

],
'pagePoolClear()':
[

],
'pagePoolList()':
[

],
'paragraphFormat("${1:string}")':
[

],
'parameterExists(${1:parameter})':
[

],
'parseDateTime(${1:date})':
[
('popConversion','"$0"'),
('timezone','"$0"')
],
'parseNumber("${1:nummber}")':
[
('radix','"$0"')
],
'precisionEvaluate()':
[

],
'precisionEvaluate()':
[

],
'preserveSingleQuotes("${1:string}")':
[

],
'quarter(${1:date})':
[
('timezone','"$0"')
],
'query()':
[

],
'queryAddColumn(${1:query},"${2:column}")':
[
('datatype_or_array','$0'),
('array','$0')
],
'queryAddRow(${1:query})':
[
('numberOrData','$0')
],
'queryColumnCount(${1:query})':
[

],
'queryColumnExists(${1:query},"${2:column}")':
[

],
'queryConvertForGrid(${1:query},${2:page},${3:pageSize})':
[

],
'queryColumnArray(${1:query})':
[

],
'queryColumnData(${1:query},"${2:columnName}")':
[
('closure','$0')
],
'queryColumnList(${1:query})':
[
('delimiter','"$0"')
],
'queryDeleteColumn(${1:query})':
[
('column','$0')
],
'queryDeleteRow(${1:query})':
[
('row','$0')
],
'queryGetCell(${1:query},"${2:column_name}")':
[
('row_number','$0')
],
'queryNew("${1:columnlist}")':
[
('columntypelist','"$0"'),
('data','$0')
],
'queryRecordCount(${1:query})':
[

],
'querySetCell(${1:query},"${2:column_name}",${3:value})':
[
('row_number','$0')
],
'querySlice(${1:query},${2:offset})':
[
('length','$0')
],
'querySort(${1:query},"${2:column_name}")':
[
('direction','"$0"')
],
'quotedValueList(${1:query_column})':
[
('delimiter','"$0"')
],
'rand("${1:algorithm}")':
[

],
'randomize(${1:number})':
[
('algorithm','"$0"')
],
'randRange(${1:number1},${2:number2})':
[
('algorithm','"$0"')
],
'releaseComObject(${1:comObject})':
[

],
'rEFind("${1:reg_expression}","${2:string}")':
[
('start','$0'),
('true','true'),
('false','false')
],
'rEFindNoCase("${1:reg_expression}","${2:string}")':
[
('start','$0'),
('true','true'),
('false','false')
],
'rEMatch("${1:reg_expression}","${2:string}")':
[

],
'rEMatchNoCase("${1:reg_expression}","${2:string}")':
[

],
'removeChars("${1:string}",${2:start},${3:count})':
[

],
'repeatString("${1:string}",${2:count})':
[

],
'replace("${1:string}","${2:substring1}","${3:substring2}")':
[
('scope','"$0"')
],
'replaceList("${1:string}","${2:list1}","${3:list2}")':
[
('delimiter_list1','"$0"'),
('delimiter_list2','"$0"')
],
'replaceNoCase("${1:string}","${2:substring1}","${3:substring2}")':
[
('scope','"$0"')
],
'rEReplace("${1:string}","${2:reg_expression}","${3:substring}")':
[
('scope','"$0"')
],
'rEReplaceNoCase("${1:string}","${2:reg_expression}","${3:substring}")':
[
('scope','"$0"')
],
'restDeleteApplication()':
[
('dirPath','"$0"'),
('password','"$0"')
],
'restInitApplication()':
[
('dirPath','"$0"'),
('serviceMapping','"$0"'),
('true','true'),
('false','false'),
('password','"$0"')
],
'restSetResponse(${1:response})':
[

],
'reverse("${1:string}")':
[

],
'right("${1:string}",${2:count})':
[

],
'rJustify("${1:string}",${2:length})':
[

],
'round(${1:number})':
[

],
'rTrim("${1:string}")':
[

],
'second(${1:date})':
[
('timezone','"$0"')
],
'sendGatewayMessage("${1:gatewayID}",${2:data})':
[

],
'serialize(${1:object})':
[

],
'serializeJSON(${1:var})':
[
('true','true'),
('false','false')
],
'sessionStartTime()':
[

],
'sessionInvalidate()':
[

],
'sessionRotate()':
[

],
'setEncoding("${1:scope}","${2:encoding}")':
[

],
'setLocale("${1:new_locale}")':
[

],
'setProfileString("${1:iniPath}","${2:section}","${3:entry}","${4:value}")':
[

],
'setVariable("${1:name}",${2:value})':
[

],
'sgn(${1:number})':
[

],
'sin(${1:number})':
[

],
'sizeOf(${1:obj})':
[
('true','true'),
('false','false')
],
'soundex("${1:str}")':
[

],
'spanExcluding("${1:string}","${2:set}")':
[

],
'spanIncluding("${1:string}","${2:set}")':
[

],
'spreadsheetSetCellValue()':
[
('spreadSheet','$0'),
('value','"$0"'),
('row','$0'),
('column','$0')
],
'spreadSheetNew()':
[
('sheetName','$0'),
('xmlFormat','$0')
],
'spreadSheetWrite()':
[
('spreadSheet','$0'),
('path','"$0"'),
('password','$0'),
('true','true'),
('false','false')
],
'sqr(${1:number})':
[

],
'sleep(${1:duration})':
[

],
'sSLCertificateList("${1:host}")':
[
('port','$0')
],
'sSLCertificateInstall("${1:host}")':
[
('port','$0')
],
'stripCr("${1:string}")':
[

],
'stringlen("${1:string}")':
[

],
'storeAddACL("${1:url}",${2:aclObject})':
[

],
'storeGetACL("${1:url}")':
[

],
'storeSetACL("${1:url}",${2:aclObject})':
[

],
'_jsonStruct()':
[

],
'struct()':
[

],
'structAppend(${1:Struct1},${2:Struct2})':
[
('true','true'),
('false','false')
],
'structClear(${1:structure})':
[

],
'structCopy(${1:structure})':
[

],
'structCount(${1:structure})':
[

],
'structDelete(${1:structure},"${2:key}")':
[
('true','true'),
('false','false')
],
'structEach(${1:struct},${2:closure})':
[

],
'structFilter(${1:struct},${2:filter})':
[

],
'structFind(${1:structure},"${2:key}")':
[

],
'structFindKey(${1:Top},"${2:Key}")':
[
('Scope','"$0"')
],
'structFindValue(${1:Top},"${2:Key}")':
[
('Scope','"$0"')
],
'structGet("${1:PathDesired}")':
[

],
'structInsert(${1:structure},"${2:key}",${3:value})':
[
('true','true'),
('false','false')
],
'structIsEmpty(${1:structure})':
[

],
'structKeyArray(${1:structure})':
[

],
'structKeyExists(${1:structure},"${2:key}")':
[

],
'structKeyList(${1:structure})':
[
('delimiter','"$0"')
],
'structKeyTranslate(${1:structure})':
[
('true','true'),
('false','false'),
('true','true'),
('false','false')
],
'structNew("${1:type}")':
[

],
'structSort(${1:base})':
[
('sortType','"$0"'),
('sortOrder','"$0"'),
('pathToSubElement','"$0"')
],
'structUpdate(${1:structure},"${2:key}",${3:value})':
[

],
'systemCacheClear("${1:cacheName}")':
[

],
'systemOutput(${1:obj})':
[
('true','true'),
('false','false'),
('true','true'),
('false','false')
],
'tan(${1:number})':
[

],
'timeFormat(${1:time})':
[
('mask','"$0"'),
('timezone','"$0"')
],
'toBase64(${1:strOrBin})':
[
('encoding','"$0"')
],
'toBinary(${1:data})':
[

],
'toNumeric(${1:value})':
[
('radix','$0')
],
'toScript(${1:cfvar},"${2:javascriptvar}")':
[
('true','true'),
('false','false'),
('true','true'),
('false','false')
],
'toString()':
[
('value','$0'),
('encoding','"$0"')
],
'trim("${1:string}")':
[

],
'uCase("${1:string}")':
[

],
'ucFirst("${1:string}")':
[

],
'unserializeJava("${1:string}")':
[

],
'URLDecode("${1:string}")':
[
('charset','"$0"')
],
'URLEncode("${1:string}")':
[
('charset','"$0"'),
('true','true'),
('false','false')
],
'URLEncodedFormat("${1:string}")':
[
('charset','"$0"'),
('true','true'),
('false','false')
],
'URLSessionFormat("${1:url}")':
[

],
'val(${1:value})':
[

],
'valueArray(${1:query_column})':
[

],
'valueList(${1:query_column})':
[
('delimiter','"$0"')
],
'verifyClient()':
[

],
'week(${1:date})':
[
('timezone','"$0"')
],
'lsweek(${1:date})':
[
('locale','"$0"'),
('timezone','"$0"')
],
'wrap("${1:string}",${2:limit})':
[
('true','true'),
('false','false')
],
'writeOutput("${1:string}")':
[

],
'echo("${1:string}")':
[

],
'xmlChildPos(${1:node},"${2:childName}",${3:index})':
[

],
'xmlElemNew(${1:xmlObj})':
[
('namespace_or_childName','"$0"'),
('childName','"$0"')
],
'xMLFormat("${1:string}")':
[

],
'xmlGetNodeType(${1:xml})':
[

],
'xmlNew(${1:caseSensitive})':
[

],
'xmlParse("${1:xmlString}")':
[
('true','true'),
('false','false'),
('validator','"$0"')
],
'htmlParse("${1:html}")':
[
('true','true'),
('false','false')
],
'xmlSearch(${1:xml},"${2:xpath}")':
[

],
'xmlTransform(${1:xml},"${2:xsl}")':
[
('parameters','$0')
],
'xmlValidate("${1:xmlDoc}")':
[
('validator','"$0"')
],
'year(${1:date})':
[
('timezone','"$0"')
],
'yesNoFormat(${1:value})':
[

],
'trueFalseFormat(${1:value})':
[

],
'private void function ${1:value}($0) {\n}':
[

],
'private string function ${1:value}($0) {\n}':
[

]
}