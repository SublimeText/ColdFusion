# ColdFusion Package for Sublime Text 2

### Features

* ColdFusion cfml, and script-based CFCs syntax highlighting. (see tmLanguage files)
* Auto inserts closing hash # (see Default (platform).sublime-keymap)
* Provides completions that match just after typing an opening angle bracket (see cfml_completions.py)
* Exhaustive library of snippet bindings (see ColdFusion.sublime-completions)
* ColdFusion specific keybindings (see Default (platform).sublime-keymap)

## Installation

The recommmended method of installation is via Package Control.

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

## Keybindings

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
<kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>a</kbd> <code>&lt;cfabort /&gt;</code>
        </td>
    </tr>
    <tr>
        <td>
<kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>r</kbd> <code>&lt;cfscript&gt;SELECTION&lt;/cfscript&gt;</code>
        </td>
        <td>
<kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>d</kbd> <code>&lt;cfdump var=&quot;#SELECTION#&quot;&gt;</code>
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

###### Overidden Sublime Keybindings

<table>
    <tr>
        <td>
<kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>d</kbd> <code>duplicate line</code>
        </td>
        <td>
<kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>a</kbd> <code>expand selection to tag</code>
        </td>
    </tr>
</table>

##Completions and Snippets
Completions in order of priority are:

* Snippets (first and foremost)
* API-injected completions
* ```.sublime-completions``` files
* Finally, words in the current buffer

Although, this package includes CFScript completions (```.sublime-completions```) and ColdFusion tag completions (API-injected), it's recommended that you create your own custom snippets using code that fits your particular coding style.
To create a new snippet select ```Tools > New Snippet...```

You can disable the default cfml tag completion by setting ```"disable_default_tag_completions"``` to ```true``` in your settings file.

Snippets repositories made available by ColdFusion community members:

* https://github.com/indynagpal/sublime-stuff
* https://github.com/bittersweetryan/ColdFusion-Script-Sublime-Snippets

To install snippets just put the ```.sublime-snippet``` files in your Packages/User folder or subfolder (to get to your Packages/User folder select the ```Preferences>Browse Packages...``` menu).

##Recommmended Packages

These following packages are all available through Package Control

* https://github.com/BoundInCode/AutoFileName
* https://github.com/weslly/ColorPicker
* https://github.com/xobb1t/Sublime-AdvancedNewFile
* https://github.com/kemayo/sublime-text-2-git
* https://github.com/dz0ny/LiveReload-sublimetext2
* https://github.com/virtix/sublime-text-2-mxunit

These packages require manual installation
* https://github.com/DominicWatson/SublimeText2CfQuickDocsLauncher

Alternative completions:
https://github.com/bbluemel/ColdFusionTagCompletions

##License
Copyright (c) 2012

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
