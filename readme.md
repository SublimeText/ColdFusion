# ColdFusion Package for Sublime Text

### Sublime Text 3
The development branch contains a rewrite of the ColdFusion plugin.
The only installation method is via Git.
```
cd Packages/
git clone https://github.com/SublimeText/ColdFusion.git
cd ColdFusion
git checkout development
```
* CFLIB Command is not currently working.
* Tag Operator Completions is not yet implemented
* CFScript component method completions is not yet implemented
* Only CF10 Dictionary is imported.

### What's New
* Added Tag Operator completions for cfscript (10/21/12)
* Added CFScript component method completions (6/28/12)
* Added "auto_close_cfml", "auto_indent_on_close" settings (6/25/12)
* Added Tag Attribute completions (6/24/12)
* Added Command ```ColdFusion: Insert CFlib UDF``` (6/2/12)

### Features

* ColdFusion cfml, and script-based CFCs syntax highlighting. (see tmLanguage files)
* Auto inserts closing hash # (see Default (platform).sublime-keymap)
* Provides completions that match just after typing an opening angle bracket (see cfml_completions.py)
* Auto Complete ColdFusion Tags and Attributes (opt. cf7, cf8, cf9 & cf10)
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

You can also use ```sublime.log_commands(True)``` in the console (```ctrl+~```) to output key presses and their corresponding command to the console pane.

<table>
    <tr>
        <td>
<kbd>⇧</kbd>+<kbd>#</kbd> <code>#SELECTION#</code>
        </td>
        <td>
<kbd>Ctrl</kbd>+<kbd>⇧</kbd>+<kbd>O</kbd> <code>&lt;cfoutput&gt;SELECTION&lt;/cfoutput&gt;</code>
        </td>
    </tr>
    <tr>
        <td>
<kbd>Ctrl</kbd>+<kbd>⇧</kbd>+<kbd>#</kbd> <code>&lt;cfoutput&gt;#SELECTION#&lt;/cfoutput&gt;</code>
        </td>
        <td>
<kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>A</kbd> <code>&lt;cfabort /&gt;</code>
        </td>
    </tr>
    <tr>
        <td>
<kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>D</kbd> <code>&lt;cfdump var=&quot;#SELECTION#&quot;&gt;</code>
        </td>
        <td>
<kbd>Alt</kbd>+<kbd>⇧</kbd>+<kbd>R</kbd> <code>&lt;cfscript&gt;SELECTION&lt;/cfscript&gt;</code>
        </td>
    </tr>
    <tr>
        <td>
<kbd>Ctrl</kbd>+<kbd>⇧</kbd>+<kbd>/</kbd> <code>block comment (cfml/cfscript) </code>
        </td>
        <td>
<kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>⇧</kbd>+<kbd>/</kbd> <code>javadoc comment</code>
        </td>
    </tr>
    <tr>
        <td>
<kbd>Alt</kbd>+<kbd>↩</kbd> <code>terminates statement (cfscript)</code>
        </td>
        <td>
<kbd>Ctrl</kbd>+<kbd>⇧</kbd>+<kbd>=</kbd> <code>&lt;cfset SELECTION /&gt;</code>
        </td>
    </tr>
</table>


Many more key bindings are available via Sublime ```Preferences > Key Bindings - Default```

##Completions and Snippets
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

The following themes optimized for ColdFusion are made available by ColdFusion community members and can be installed with Package Control (http://wbond.net/sublime_packages/community)

* https://github.com/Siddley/Enhanced.HTML.CFML

If you'd like to customize your favorite theme for ColdFusion support, you can use the ```entity.name.tag.cf``` scope in your tmTheme file.
For example the following definition will use the color ```#C87551``` for all ColdFusion tags:
```
<dict>
    <key>name</key>
    <string>Meta</string>
    <key>scope</key>
    <string>meta.tag.block.cf, meta.tag.inline.cf</string>
    <key>settings</key>
    <dict>
        <key>fontStyle</key>
        <string></string>
        <key>foreground</key>
        <string>#C87551</string>
    </dict>
</dict>
<!-- this will color ColdFusion tag name -->
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
You can use <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>⇧</kbd>+<kbd>P</kbd> to get the scope name at the cursor position for more theme customizing .

##Development Branch
To help test the development branch you can install it by dowloading the zip and copying the contents to the Packages/ColdFusion folder.


Alternatively, you can use git to install the ColdFusion package as mentioned above and switch to the development tracking branch using:

```
git checkout development
```


##Additional Packages
Some additional packages you might want to check out  - they are all available through Package Control http://wbond.net/sublime_packages/community

* http://net.tutsplus.com/articles/news/introducing-nettuts-fetch/ (highly recommended)
* https://github.com/BoundInCode/AutoFileName (provides file auto-complete)
* https://github.com/weslly/ColorPicker (choose a color and get the hex code)
* https://github.com/xobb1t/Sublime-AdvancedNewFile (create new files faster)
* https://github.com/kemayo/sublime-text-2-git (git commands)
* https://github.com/facelessuser/ExportHtml (provides printing)
* https://github.com/dz0ny/LiveReload-sublimetext2 (live reload browser)
* https://github.com/bgreenlee/sublime-github (github gists and more)
* https://github.com/virtix/sublime-text-2-mxunit (mxunit testing)
* https://github.com/seancoyne/farcry-sublimetext (farcry snippets)

These packages require manual installation

* https://github.com/adampresley/sublime-cf-js-log-finder (debug output finder)
* https://github.com/timsayshey/Sublime-Text-CFWheels (cfwheels plugin)
* https://github.com/DominicWatson/SublimeText2CfQuickDocsLauncher (cfml documentation)

##License
Copyright (c) 2012

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
