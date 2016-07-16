# Lucario
> The best colorful flat theme for [Vim](http://www.vim.org/), [Atom](https://atom.io/), [Sublime Text](http://www.sublimetext.com/3), [Xcode](https://developer.apple.com/xcode/), [Terminal.app](http://en.wikipedia.org/wiki/Terminal_%28OS_X%29), [XTerm](https://en.wikipedia.org/wiki/Xterm) and [iTerm](http://www.iterm2.com/).

![Logo](https://raw.githubusercontent.com/raphamorim/lucario/master/images/lucario.png)

## Summary
* Editors
  * [Atom](#atom)
  * [Brackets](#brackets)
  * [Sublime Text](#sublime-text)
  * [TextMate](#textmate)
  * [Vim](#vim)
  * [Xcode](#xcode)
* Terminal
  * [iTerm](#iterm)
  * [Terminal.app](#terminalapp)
  * [XTerm](#xterm)
* [Color Palette](#color-palette)
* [Contributing](#contributing)
* [About](#about)


## Atom
![Atom Example](https://raw.githubusercontent.com/raphamorim/lucario/master/images/atom.png)

1.	Go to **Atom -> Preferences...**
2.	Then select the **Install** tab
3.	Switch to the **Themes** 
4.	Type **Lucario** in the search box

See Lucario in [atom.io page](https://atom.io/themes/lucario)

## Brackets

Not available yet.

## Sublime Text
![Sublime Example](https://raw.githubusercontent.com/raphamorim/lucario/master/images/sublime_text.png)

### Install using Package Control

If you are using [Package Control](https://sublime.wbond.net/), you can easily
install Lucario via the **Package Control: Install Package**. The package theme as
Lucario Color Scheme in the packages list. After this you should be able to select lucario color scheme
by browsing **Preferences -> Color Scheme -> Lucario Color Scheme -> Lucario**

See Lucario in [package control web page](https://sublime.wbond.net/packages/Lucario%20Color%20Scheme)

### Manually install

1.    Use `git clone git@github.com:raphamorim/lucario.git` and then take the **Lucario.tmTheme**
2.	Open Sublime text and click on **Preferences -> Browse Packages**
3.	Then put the **Lucario.tmTheme** there
4.	Now you should be able to select lucario theme by browsing **Preferences -> Color Scheme -> Lucario**

## TextMate

Not available yet.

## Vim
![Vim Example](https://raw.githubusercontent.com/raphamorim/lucario/master/images/vim.png)

Put `lucario.vim` file in your `~/.vim/colors/` directory and add the following line to your vimrc file:

    syntax enable
    set number
    colorscheme lucario


OS X Hint: `vim /usr/share/vim/vimrc`

## Xcode
![xcode Example](https://raw.githubusercontent.com/raphamorim/lucario/master/images/xcode.png)

1.  Use `git clone git@github.com:raphamorim/lucario.git` (or use [.zip download][zip] option)
2.  Copy the `xcode/Lucario.dvtcolortheme` file to your **Xcode FontAndColorThemes** directory
3. Reopen your Xcode and click on **Xcode -> preferences**
4. Open **Fonts & Colors** tab and select lucario as your theme

**Hint**: run this command to copy and paste `Lucario.dvtcolortheme` file to your **Xcode FontAndColorThemes** directory:

```sh
$ cp Lucario.dvtcolortheme ~/Library/Developer/Xcode/UserData/FontAndColorThemes/
```

## iTerm
![iTerm Example](https://raw.githubusercontent.com/raphamorim/lucario/master/images/iterm.png)

1.  Use `git clone git@github.com:raphamorim/lucario.git` (or use [.zip download][zip] option)
2.  iTerm > Settings Tab
3.  Go to "Profiles > Colors" tab
4.  Click "Load Presets..." to import and select the **iterm/Lucario.itermcolors** file

## Terminal.app
![Terminal Example](https://raw.githubusercontent.com/raphamorim/lucario/master/images/terminal.png)

1.  Use `git clone git@github.com:raphamorim/lucario.git` (or use [.zip download][zip] option)
2.  Terminal > Settings Tab
3.  Click "Gear" icon
4.  Click Import and select the **terminal/Lucario.terminal** file
5.  Click Default

[zip]: https://github.com/raphamorim/lucario/archive/master.zip

## XTerm
![xterm Example](https://raw.githubusercontent.com/raphamorim/lucario/master/images/xterm.png)

1.  Use `git clone git@github.com:raphamorim/lucario.git` (or use [.zip download][zip] option)
2.  Copy the **xterm/.Xresources** file to your home directory
3.  (optional for some cases) Add `xrdb -merge ~/.Xresources` to your init scripts (e.g. `.xinitrc`)

## Color Palette

Palette      | Hex       | RGB           | HSL
---          | ---       | ---           | ---
Background   | `#2b3e50` | `43 62 80`    | `209.2° 30.1% 24.1%`
Current Line | `#243443` | `36 52 67`    | `209° 30.1% 20.2%`
Selection    | `#19242f` | `25 36 47`    | `210° 30.6% 14.1%`
Foreground   | `#f8f8f2` | `248 248 242` | `60° 30% 96%`
Comment      | `#5c98cd` | `92 152 205`  | `208.1° 53.1% 58.2%`
String       | `#E6DB74` | `230 219 116` | `54.2° 69.5% 67.8%`

## Contributing

Why not use lucario color scheme in your favorite editor? does not exist?
So what about creating one, is very simple \o/

1.  Fork it!
2.  Create your feature branch: `git checkout -b my-new-feature`
3.  Commit your changes: `git commit -m 'Add some feature'``
4.  Push to the branch: `git push origin my-new-feature`
5.  Submit a pull request :)

## About

**Credits**: Project inspired by [@zenorocha's](https://twitter.com/zenorocha) [Dracula Theme](https://github.com/zenorocha/dracula-theme).

**License**: MIT ® [Raphael Amorim](https://github.com/raphamorim).
