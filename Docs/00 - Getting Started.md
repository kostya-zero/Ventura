<p align="center">
    <h1 align="center">~/Ventura/Docs/</h1>
    <h2 align="center">Part 00 // Getting Started</h2>
</p>

Ventura is an interpreted programming language developed in Python along with Cython. 
If you have worked with Python or Pascal in the past, then the syntax of this language will seem familiar to you. 
The language requires an interpreter on the computer to execute scripts.

Before you start, if you are going to learn and using the Ventura language, you should know the following things:
- Ventura is an interpreted programing language.
- Ventura haven't a compiler, it require runtime on computer.
- At this moment, you can use Ventura only on systems with installed Windows OS.

If in the past you work with Python or Pascal you will adaptive faster.
In the begining, we need to install an interpreter of Ventura. 
In this tutorial we use installer.

## Installing Ventura

You can install Ventura on your computer in two ways:
- **Portable** - Portable version of Ventura. Suitable if you don't want to install it or you need it for a while.
- **Installer** - Standard installation using the Ventura installer. The installer installs the file extension interpreter and adds the path to Ventura to the Path.

Go to releases and choose version of Ventura.
Download setup and run it.
After readme, you need to choose a components to install.
This window must looks like this:

> ![In this case, we use installer of 1.2 version.](https://raw.githubusercontent.com/kostya-zero/Ventura/master/Docs/images/00-01.png)
> _In this case, we use installer of 1.2 version._

The check mark on "Interpreter" must be set. This is a important step during installation.
After a few steps and acceptance of the license agreement, the installation will begin. 
It lasts an average of 15 - 30 seconds, it all depends on the performance of your device.

## Final steps
After installation, we need to check that everything is working well. 
To do this, we will need a terminal. 
There we write the word "ventura" and adds the option "-H". 
This option is responsible for displaying help about using Ventura.

> ```commandline
> ventura -H
> ```
> 
> _The command that you need to enter into the terminal to output help._

> ```text
> Usage of interpreter:
> ventura [path_to_file]
> or
> ventura [option]
> 
> Options:
> -H, --help: Shows help.
> -V, --version: Version of Ventura.
> -A, --authors: Shows authors of Ventura.
> -S, --system: Shows info about current machine.
> -gvt, --generate-vt: Generates .vt file at location.
> 
> If you have questions about acting with Ventura Interpreter, go
> to official GitHub repository to the issues page and create
> a new issue with your questions. Or, go to check documentation
> for more information.
> ```
> 
> _The text that we will receive in response to the entered command._

If you got the same answer as above, then everything is fine. 
If you get an error, then you need to try reinstalling Ventura. 
If, even after reinstalling, you still get an error, contact support on GitHub for help.

> ```text
> Ventura got an exceptions while starting, because arch.pyd is missing.
> ```
> 
> _An error that you will get if some important file is missing. In our case, arch.pyd._

## Ending
In this guide, we installed the Ventura interpreter and tested it for performance. 
In the next guide, we will study the basic functionality and syntax.