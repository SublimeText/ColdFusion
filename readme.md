# Official ColdFusion Package for Sublime Text 2
## Official Package Control ColdFusion Package

* ColdFusion CFML, cfscript, and script-based CFCs syntax highlighting. (see tmLanguage files)
* Auto inserts closing hash # (see Default (platform).sublime-keymap)
* Provides completions that match just after typing an opening angle bracket (see cfml_completions.py)
* Exhaustive library of snippet bindings (see ColdFusion.sublime-completions)
* Keyboard Shortcuts (see Default (platform).sublime-keymap)

### ColdFusion Keybindings

* <kbd>shift</kbd>+<kbd>3</kbd> `#SELECTION#`
* <kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>o</kbd> `<cfoutput>SELECTION</cfoutput>`
* <kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>3</kbd> `<cfoutput>#SELECTION#</cfoutput>`
* <kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>a</kbd> `<cfabort />`
* <kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>r</kbd> `<cfscript>SELECTION</cfscript>`
* <kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>d</kbd> `<cfdump var="#SELECTION#">`
* <kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>c</kbd> `cfml comment`
* <kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>shift</kbd>+<kbd>/</kbd> `javadoc comment`
* <kbd>ctrl</kbd>+<kbd>enter</kbd> `terminates statement; adds new line`

#### Other Keybindings

* <kbd>ctrl</kbd>+<kbd>r</kbd> `goto symbol command`
* <kbd>alt</kbd>+<kbd>shift</kbd>+<kbd>w</kbd> `wrap selection in tag`
* <kbd>ctrl</kbd>+<kbd>/</kbd> `line comment`
* <kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>/</kbd> `block comment`
* To see all keybindings select `Preferences > Keybindings - Default` from the menu

#### Overridden Sublime Text 2 Keyboard Shortcuts

* <kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>d</kbd> `duplicate line`
* <kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>a</kbd> `expand selection to tag`

## Installation

The recommmended method of installation is via Package Control. It will download upgrades to your packages automatically.

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
