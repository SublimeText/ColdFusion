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
&nbsp;
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
