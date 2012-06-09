/*
	Requires CF9, and a CFEclipse dictionary file
	Converts a CFEclipse dictionary file to a CF structure
	then outputs the Python completion object for use with
	ColdFusionTagCompletions, example:

	<cfscript>
		importer = CreateObject("import");
		importer.init(ExpandPath("/") & "cf9.xml").convert();
	</cfscript>
	<pre>
	<cfoutput>#importer.outputpython()#</cfoutput>
	</pre>
*/
component output="false" displayname="import" {
	this.tagxml = "";
	this.newtags = [];
	this.newtagtemplate = {
		name = "",
		endtagrequired = true,
		completions = [],
		attributes = {}
	};
	this.newattributetemplate = {
		name = "",
		completions = []
	};

	public function init(filename) {
		var filecontent = FileRead( filename );
		this.tagxml = XmlParse( filecontent ).dictionary.tags;
		return this;
	}

	public function convert() {
		var i = 0;
		var j = 0;
		var k = 0;
		var newtag = {};
		var newattribute = {};
		var currenttag = "";
		var paramname = "";
		for ( i = 1; i <= ArrayLen( this.tagxml.Tag ); i++ ) {
			currenttag = this.tagxml.Tag[i];
			newtag = Duplicate( this.newtagtemplate );
			if ( StructKeyExists( currenttag.XmlAttributes, "endtagrequired" ) EQ false ) {
				newtag.endtagrequired = "false";
			}
			newtag.name = currenttag.XmlAttributes.Name;
			if ( StructKeyExists( currenttag, "parameter" ) ) {
				for ( j = 1; j <= ArrayLen( currenttag.parameter ); j++ ) {
					paramname = currenttag.parameter[j].XmlAttributes.name;
					newtag.completions.add( paramname );
					newattribute = Duplicate( this.newattributetemplate );
					newattribute.name = currenttag.parameter[j].XmlAttributes.name;
					if ( StructKeyExists( currenttag.parameter[j].XmlAttributes, "type" ) && ( currenttag.parameter[j].XmlAttributes.type == "Boolean" ||
							( StructKeyExists( currenttag.parameter[j], "values" ) && StructKeyExists( currenttag.parameter[j].values, "value" ) ) ) ) {

						switch ( currenttag.parameter[j].XmlAttributes.type ) {
							case "Boolean":
								newattribute.completions.add( "true" );
								newattribute.completions.add( "false" );
								break;
							case "String":
								if ( StructKeyExists( currenttag.parameter[j],"values" ) && StructKeyExists( currenttag.parameter[j].values,"value") ) {
									for ( k = 1; k <= ArrayLen( currenttag.parameter[j].values.value ); k++ ) {
										newattribute.completions.add( Replace( currenttag.parameter[j].values.value[k].xmlattributes.option, '"', '', "all" ) );
									}
								}
								break;
						}

					}
					newtag.attributes[newattribute.name] = newattribute;
					/*
					if ( StructKeyExists( currenttag.parameter[j].XmlAttributes, "required" ) && currenttag.parameter[j].XmlAttributes.required EQ "true" ) {

					}
					*/
				}
			}
			this.newtags.add( newtag );
		}
		return this.newtags;
	}

	public function outputpython( includeValuesInMainList = true ) {
		var pythonoutput = "";
		var tagIterator = this.newtags.iterator();
		var compIterator = "";
		var tag = "";
		var comp = "";
		var attrCompIterator = "";
		var attrComp = "";
		var crlf = chr( 13 ) & chr( 10 );
		var attrIterator = "";
		var attr = "";

		while( tagIterator.hasNext() ) {
			tag = tagIterator.next();
			pythonoutput &= "self.completions['" & tag.name & "'] = {" & crlf;
			compIter = tag.completions.iterator();
			pythonoutput &= "	'completions': [" & crlf;
			while ( compIter.hasNext() ) {
				comp = compIter.next();
				pythonoutput &= '		("' & comp & '\t@' & comp & '", "' & comp & '=\"$1\"$0")';
				if ( arguments.includeValuesInMainList && StructKeyExists( tag.attributes, comp ) ) {
					attrCompIterator = tag.attributes[comp].completions.iterator();
					while ( attrCompIterator.hasNext() ) {
						attrcomp = attrCompIterator.next();
						pythonoutput &= "," & crlf;
						pythonoutput &= '		("' & comp & '=\"' & attrcomp & '\"\t' & comp & '", "' & comp & '=\"${1:' & attrcomp & '}\"$0")';
					}
				}
				if ( compIter.hasNext() ) {
					pythonoutput &= ",";
				}
				pythonoutput &= crlf;
			}
			pythonoutput &= "	]," & crlf;
			attrIterator = StructKeyArray(tag.attributes).iterator();
			pythonoutput &= "	'attributes': [";
			while ( attrIterator.hasNext() ) {
				attr = attrIterator.next();
				pythonoutput &= crlf & '		"' & attr & '"';
				if ( attrIterator.hasNext() ) {
					pythonoutput &= ",";
				}
			}
			pythonoutput &= crlf & "	]" & crlf;
			pythonoutput &= "}" & crlf;
		}
		return pythonoutput;
	}
}
