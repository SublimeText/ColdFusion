# ColdFusion Package for Sublime Text 2

### What's New
* Added Command ```ColdFusion: Insert CFlib UDF``` (6/2/12)

### Features

* ColdFusion cfml, and script-based CFCs syntax highlighting. (see tmLanguage files)
* Auto inserts closing hash # (see Default (platform).sublime-keymap)
* Provides completions that match just after typing an opening angle bracket (see cfml_completions.py)
* Exhaustive library of snippet bindings (see ColdFusion.sublime-completions)
* ColdFusion specific key bindings (see Default (platform).sublime-keymap)

## Installation

The recommended method of installation is via Package Control.

### Package Control

* Follow instructions on http://wbond.net/sublime_packages/package_control
* Install using Package Control: Install > ColdFusion package

### Using Git

Go to your Sublime Text 2 `Packages` directory and clone the repository using the command below:

    git clone https://github.com/SublimeText/ColdFusion

### Download Manually

* Download the files using the GitHub .zip download option
* Unzip the files and rename the folder to `ColdFusion`
* Copy the folder to your Sublime Text 2 `Packages` directory

- - -

## Key bindings

Some packages will override key bindings. If you have problems with a specific key shortcut,
you can add it to your User - Key Bindings file ```Preferences > Key Bindings - User```

You can also use ```sublime.log_commands(True)``` in the console (```ctrl+~```) to output key presses.

<table>
    <tr>
        <td>
<kbd>shift</kbd>+<kbd>3</kbd> <code>#SELECTION#</code>
        </td>
        <td>
<kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>o</kbd> <code>&lt;cfoutput&gt;SELECTION&lt;/cfoutput&gt;</code>
        </td>
    </tr>
    <tr>
        <td>
<kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>3</kbd> <code>&lt;cfoutput&gt;#SELECTION#&lt;/cfoutput&gt;</code>
        </td>
        <td>
<kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>a</kbd> <code>&lt;cfabort /&gt;</code>
        </td>
    </tr>
    <tr>
        <td>
<kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>d</kbd> <code>&lt;cfdump var=&quot;#SELECTION#&quot;&gt;</code>
        </td>
        <td>
<kbd>alt</kbd>+<kbd>shift</kbd>+<kbd>r</kbd> <code>&lt;cfscript&gt;SELECTION&lt;/cfscript&gt;</code>
        </td>
    </tr>
    <tr>
        <td>
<kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>c</kbd> <code>cfml comment</code>
        </td>
        <td>
<kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>shift</kbd>+<kbd>/</kbd> <code>javadoc comment</code>
        </td>
    </tr>
    <tr>
        <td>
<kbd>alt</kbd>+<kbd>enter</kbd> <code>terminates statement; adds new line</code>
        </td>
        <td>
<kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>=</kbd> <code>&lt;cfset SELECTION /&gt;</code>
        </td>
    </tr>
</table>

* For some more useful default key bindings see: https://gist.github.com/2918078

##Completions and Snippets
**Note**: A classic completions plug-in is available from @bbluemel which can be downloaded at

https://github.com/bbluemel/ColdFusionTagCompletions
***
Although, this package includes CFScript completions (```.sublime-completions```) and ColdFusion tag completions (API-injected), it's recommended that you create your own custom snippets using code that fits your particular coding style.
To create a new snippet select ```Tools > New Snippet...``` from the Sublime Text menu.
Use ```<scope>text.html.cfm - string</scope>``` for ColdFusion markup snippets and ```<scope>source.cfscript - string</scope>``` for CFScript snippets.

Completions in order of priority are:
* Snippets
* API-injected completions
* ```.sublime-completions``` files
* words in the current buffer

The following list contains snippets repositories made available by ColdFusion community members:

* https://github.com/indynagpal/sublime-stuff
* https://github.com/bittersweetryan/ColdFusion-Script-Sublime-Snippets

To install snippets just put the ```.sublime-snippet``` files in your Packages/User folder or sub-folder (to get to your Packages/User folder select ```Preferences > Browse Packages...``` from the Sublime Text 2 menu).
##Custom Themes
If you'd like to customize your favorite theme for ColdFusion support, you can use the ```entity.name.tag.cf``` scope in your tmTheme file.
For example the following definition will use the color ```#C87551``` for all ColdFusion tags:
```
<dict>
    <key>name</key>
    <string>Entity</string>
    <key>scope</key>
    <string>entity.name.tag.cf</string>
    <key>settings</key>
    <dict>
        <key>fontStyle</key>
        <string></string>
        <key>foreground</key>
        <string>#C87551</string>
    </dict>
</dict>
```
You can use <kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>shift</kbd>+<kbd>p</kbd> to get the scope name at the cursor position for more theme customizing .

##Additional Packages
Some additional packages you might want to check out (these packages are all available through Package Control):

* https://github.com/BoundInCode/AutoFileName (provides file auto-complete)
* https://github.com/weslly/ColorPicker (choose a color and get the hex code)
* https://github.com/xobb1t/Sublime-AdvancedNewFile (create new files faster)
* https://github.com/kemayo/sublime-text-2-git (git commands)
* https://github.com/facelessuser/ExportHtml (provides printing)
* https://github.com/dz0ny/LiveReload-sublimetext2 (live reload browser)
* https://github.com/bgreenlee/sublime-github (github gists and more)
* https://github.com/virtix/sublime-text-2-mxunit (mxunit testing)

These packages require manual installation

* https://github.com/DominicWatson/SublimeText2CfQuickDocsLauncher (cfml documentation)

##License
Copyright (c) 2012

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
