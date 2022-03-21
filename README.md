<p align="center">
    <img src="https://raw.githubusercontent.com/kostya-zero/Ventura/master/ventura-poster.png"/>
</p>

<p align="center">
    <img src="https://img.shields.io/github/downloads/kostya-zero/Ventura/total"/>
    <img src="https://img.shields.io/github/v/release/kostya-zero/Ventura"/>
    <img src="https://img.shields.io/github/license/kostya-zero/Ventura"/>
    <img src="https://img.shields.io/badge/support%20windows-7%20%7C%208%20%7C%208.1%20%7C%2010%20%7C%2011-green"/>
</p>

**Issues/Pull requests:**
![GitHub issues](https://img.shields.io/github/issues/kostya-zero/Ventura)
![GitHub issues](https://img.shields.io/github/issues-raw/kostya-zero/Ventura)
![GitHub closed issues](https://img.shields.io/github/issues-closed/kostya-zero/Ventura)
![GitHub pull requests](https://img.shields.io/github/issues-pr/kostya-zero/Ventura)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/kostya-zero/Ventura)

**Stats:**
[![GitHub stars](https://img.shields.io/github/stars/kostya-zero/Ventura)](https://github.com/kostya-zero/Ventura/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/kostya-zero/Ventura)](https://github.com/kostya-zero/Ventura/network)

**Languages**: 
![GitHub language count](https://img.shields.io/github/languages/count/kostya-zero/Ventura) 
![GitHub top language](https://img.shields.io/github/languages/top/kostya-zero/Ventura)

**Activity:**
![GitHub last commit](https://img.shields.io/github/last-commit/kostya-zero/Ventura)
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/kostya-zero/Ventura)

Ventura - interpreted programming language  developed on Python with Cython code.
Interpreter allows you to create and write scripts, execute it on 64-bit systems with installed Windows OS.
Scripts can be executed only with runtime, you don't need to download any third-party software.

Ventura have syntax like **Pascal** and **Python** (partially). 
Also, **"main"** package include basic commands. 
Below, example of syntax:
```ruby
;extend main
;prog_name "output"
;new $var
;entry
    &sv: $var,$__cpuarch
    &out: "CPU Arch - "
    &lnout: $var
```
Ventura developed on Python with Cython without any third-party packages. 
Build with **PyInstaller** and **EasyCython**.
Ventura have open source code and protected under **GNU GPL v3.0** license.

<p align="center">
    <h2 align="center">:computer: System requirements</h2>
</p>

To run Ventura on your system, your PC must match requirements:
- **OS** - Windows 8 or above, Windows 7 are **not** recommended.
- **CPU** - 64-bit CPU with AMD64 architecture.

<p align="center">
    <h2 align="center">:hammer_and_wrench:  Build Requirements</h2>
</p>

To build Ventura your environment must match requirements:
- **Python** - 3.9 or 3.10 (we dont recommend to build it with 3.11)
- **PIP** - Version 21.x.x and above.
- **Packages** - PyInstaller, EasyCython, Cython and PIP.
- **Other** - C++ compiler (G++ or VS Build Tools) and terminal.

<p align="center">
    <h2 align="center">:fast_forward: Getting started</h2>
</p>

To start working with Ventura, you need to install runtimes.
You can use installer or download portable version.
Go to "Releases" page and download the latest release (installer or portable).
If you pick installer, you need to download it and run.
Installer automatically adds Ventura folder to Path, assign file extensions and make integration with Windows.
If you pick portable, you need to download it and extract content.
But, you must start Ventura from folder where you extract it.

Lets test interpreter. Just type this to command prompt:
```commandline
ventura
```

You will get this response:
```text
Ventura Interpreter 1.1 Build 50

Usage of interpreter:
ventura [path_to_file]
or
ventura [option]

To show help, write "ventura -H" or "ventura --help" to the command line.
```

If you get response like this, interpreter works fine and ready for tasks.
But, you can get something like this:
```text
Ventura got an exceptions while starting, because args.pyd is missing.
```

Thats means Ventura havent one of important libraries to work correctly. 
To repair it, you can reinstall Ventura. 
If bug cause again, report about it to issues with your system information.

One small note.
We do not recommend to use Ventura on Windows 7. 
Why? 
In 14 January 2020 Microsoft ended support of Windows 7.
Text from official Microsoft Support portal:
> **Microsoft made a commitment to provide 10 years of product support for Windows 7 when it was released on October 22, 2009. 
> This 10-year period has now ended, and Microsoft has discontinued Windows 7 support so that we can focus our investment on supporting newer technologies and great new experiences. 
> The specific end of support day for Windows 7 was January 14, 2020. 
> Technical assistance and software updates from Windows Update that help protect your PC are no longer available for the product. 
> Microsoft strongly recommends that you move to Windows 11 to avoid a situation where you need service or support that is no longer available.**

> **Source:** https://support.microsoft.com/en-us/windows/windows-7-support-ended-on-january-14-2020-b75d4580-2cc7-895a-2c9c-1466d9a53962

<p align="center">
    <h2 align="center">:memo: Generate .vt files</h2>
</p>

Ventura works only with .vt files.
You can generate it with Ventura executable.
Just type this:
```ps
ventura -gvt
```
Now, you need to type an **absolute path** to file. 
Just type it in dialog:
```
Enter absolute path for new file: F:\script.vt
Success! Script file was created by this path: F:\script.vt
```
You can check directory for this file. Its include a very, very simple script.
```ruby
;extend main
;prog_name "script"
;entry
    &out: "Hello World!"
```

<p align="center">
    <h2 align="center">:chart_with_downwards_trend: Current status of Project</h2>
</p>

At this moment we are trying to add new features to Ventura and update old.
The second task is make code executes faster and rewrites the part of code on Cython.
Also, docs are not finished. 
Its important part of thi project.
And, if you are using Ventura, we need your feedback!
Create issue and tell us how you feels while developing on Ventura.

<p align="center">
    <h2 align="center">:information_source: Other Information</h2>
</p>
Remember, this language made to create scripts. Main executable of Ventura is interpreter. Good luck! 
