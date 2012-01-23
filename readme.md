# ColdFusion package for Sublime Text 2

* ColdFusion CFML, cfscript, and script-based CFCs syntax highlighting. (see tmLanguage files)
* Auto inserts closing hash # (see Default (platform).sublime-keymap)
* Provides completions that match just after typing an opening angle bracket (see cfml_completions.py)
* Exhaustive library of snippet bindings (see ColdFusion.sublime-completions)
* Keyboard Shortcuts (see Default (platform).sublime-keymap)

### Keyboard Shortcuts
* shift+3 `#SELECTION#`
* ctrl+shift+3 `<cfoutput>#SELECTION#</cfoutput>`
* ctrl+shift+o `<cfoutput>SELECTION</cfoutput>`
* ctrl+alt+r `<cfscript>SELECTION</cfscript>`
* ctrl+alt+d  `<cfdump var="#SELECTION#">`
* ctrl+shift+m  `<!--- SELECTION --->`
* ctrl+r `Goto Symbol command`

## Installation

The recommmended method of installation is via Package Control. It will download upgrade to your packages automatically.

### Package Control

* Follow instructions on http://wbond.net/sublime_packages/package_control
* Install using Package Control: Install > ColdFusion package

### Using Git

Go to your Sublime Text 2 `Packages` directory and clone the repository using the command below:

    git clone https://github.com/SublimeText/ColdFusion "ColdFusion"

### Download Manually

* Download the files using the GitHub .zip download option
* Unzip the files and rename the folder to `ColdFusion`
* Copy the folder to your Sublime Text 2 `Packages` directory

##Notes
* cfml_completions.py auto complete will only work with Sublime Text 2 Build 2151 or greater
