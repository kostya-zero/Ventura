<p align="center">
    <h1 align="center">VENTURA</h1>
</p>

<p align="center">
    <img src="https://img.shields.io/github/downloads/kostya-zero/Ventura/total"/>
    <img src="https://img.shields.io/github/issues/kostya-zero/Ventura"/>
    <img src="https://img.shields.io/github/v/release/kostya-zero/Ventura"/>
    <img src="https://img.shields.io/github/license/kostya-zero/Ventura"/>
    <img src="https://img.shields.io/github/stars/kostya-zero/Ventura"/>
    <img src="https://img.shields.io/github/forks/kostya-zero/Ventura"/>
    <img src="https://img.shields.io/badge/support%20windows-7%20%7C%208%20%7C%208.1%20%7C%2010%20%7C%2011-green"/>
</p>

- **Languages** - ![GitHub language count](https://img.shields.io/github/languages/count/kostya-zero/Ventura)
    
Ventura is a scripting programing language that's allows you to make small scripts and execute it. 
Language are interpreted, and you can use it only on Windows platforms.
No compilers, only runtime.

Ventura have syntax like **Pascal**. 
Also, **"main"** package include basic commands. Below, example of syntax:
```ruby
;extend main
;prog_name "output"
;new $var
;entry
    &sv: $var,$__cpuarch
    &out: "CPU Arch - "
    &lnout: $var
```
Ventura developed on Python without any third-party packages. 
Build with **PyInstaller** and **EasyCython**.
Ventura have open source code and protected under **GNU GPL v3.0** license.

## System requirements
To run Ventura on your system, your PC must match requirements:
- **OS** - Windows 8 or above, Windows 7 are **not** recommended.
- **CPU** - 64-bit CPU with AMD64 architecture.

## Build Requirements 
To build Ventura your environment must match requirements:
- **Python** - 3.9 or 3.10 (we dont recommend to build it with 3.11)
- **PIP** - Version 21.x.x and above.
- **Packages** - PyInstaller, EasyCython, Cython and PIP.
- **Other** - C++ compiler (G++ or VS Build Tools) and terminal.

## How to use it
You can use installer or download portable version. 
Installer, by default, set up your interpreter at Program Files directory. 
Default directory:
```
C:\Program Files\ZERO\Ventura\Ventura09b
```
Portable version you can place where you want.

To check if it works correctly, try to execute it with command prompt:
```
ventura
```
If you use installer, you can call Ventura from terminal.
Installer adds Ventura folder to "Path" variable.
You must have this output:
```
Ventura Interpreter
```

## Generate .vt files
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

## Other Information
Remember, this programing language made to create scripts. Main executable of Ventura is interpreter. Good luck! 
