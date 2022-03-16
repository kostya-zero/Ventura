# Ventura
Ventura is a scripting programing language that's allows you to make small scripts and execute it. 
Language are interpreted, and you can use it only on Windows platforms.
No compilers, only runtime.

Ventura have syntax like **Pascal**. 
Also, **"main"** package include basic commands. Below, example of syntax:
```
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

## How to use it
You can use installer or download portable version. 
Installer, by default, set up your interpreter at Program Files directory. 
Portable version you can place where you want.

To check if it works correctly, try to execute it with command prompt:
```
ventura.exe
```
You must have this output:
```
Ventura Interpreter
```

# Generate .vt files
Ventura works only with .vt files.
You can generate it with Ventura executable.
Just type this:
```
ventura.py -generate-vt
```
Now, you need to type an **absolute path** to file. 
Just type it in dialog:
```
Enter absolute path for new file: F:\script.vt
Success! Script file was created by this path: F:\script.vt
```
You can check directory for this file. Its include a very, very simple script.
```
;extend main
;prog_name "script"
;entry
    &out: "Hello World!"
```

# Other Information
Remember, this programing language made to create scripts. Main executable of Ventura is interpreter. Good luck! 