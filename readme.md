# ColdFusion Package for Sublime Text 2

### What's New
* Added Command ```ColdFusion: Insert UDF``` (6/2/12)

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

###### Overridden Sublime Key bindings

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

##Additional Packages
Some additional packages you might want to check out (these packages are all available through Package Control):

* https://github.com/BoundInCode/AutoFileName
* https://github.com/weslly/ColorPicker
* https://github.com/xobb1t/Sublime-AdvancedNewFile
* https://github.com/kemayo/sublime-text-2-git
* https://github.com/dz0ny/LiveReload-sublimetext2
* https://github.com/virtix/sublime-text-2-mxunit

These packages require manual installation

* https://github.com/DominicWatson/SublimeText2CfQuickDocsLauncher

##License
Copyright (c) 2012

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
