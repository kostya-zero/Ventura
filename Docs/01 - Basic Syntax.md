<p align="center">
    <h1 align="center">~/Ventura/Docs/</h1>
    <h2 align="center">Part 01 // Basic Syntax</h2>
</p>

Ventura have syntax like Pascal, but, its not easy to learn.
Unfourtanetely, Ventura have a bad syntax.
We are trying to rewrite our syntax to make it better to read and write.

## Basics of the basics
Every script in Ventura must starts with **;entry** command.
But, not so fast! We need to **import necessary packages** to start writing scripts on Ventura.
For initialization before script starts you must use **internal commands**.
Every internal command starts with **";"**.
- **;extend <[package_name]>** - Imports Ventura package.
- **;prog_name** - Sets name for current program. Not necessary.
- **;new $[name]** - Initialize new variable in memory.
- **;entry** - Starts program.

> **Important Notice**: 
> You cant start program without **;entry** command. Interpreter will throw error about this.
> Internal commands can be executed before **;entry**.

So, firstly, we need to import main package named **vio**.
To import this package, we need to use **;extend** command. 
So, lets try!
```ruby
;extend <vio>
```
> **Important Notice**: 
> Name of package must be in **<>** characters. Example: <*hello*>

Great! We have imported main package!
So, lets type entry point for our script.
```ruby
;extend <vio>
;entry
```
Oh, we miss something! 
If you need to set name for your script you can use **;prog_name** command and type script name.
Name of script must be in double quotes.
if you type in without it, you will get an error.
Lets name script **"hello_world"**, because we are trying to output **"Hello world!"** phrase.
```ruby
;extend <vio>
;prog_name "hello_world"
;entry
```
> **Important Notice**: 
> Program name cant have spaces in name. If you type "hello world", you will get an error.

So, we imported main package, sets name for our script and typed entry point.
Lets try to output **"Hello world!"**.
To do this, we need a fucntion to output data to console.
So, we have it in main package.
**&out**.
> **Important Notice**: 
> If you want to know more about main package functions, go to https://github.com/kostya-zero/Ventura/blob/master/Docs/00%20-%20Getting%20Started.md .

This will output text. 
But, we are trying output a text value. 
Text value must have double quotes at start and end. 
Like this:
```ruby
"Ventura is cool!"
```
Ventura does not supports any symbols in text. 
You need to use **format symbols** to put it.
Lets try it now!
```ruby
;extend <vio>
;prog_name "hello_world"
;entry
    &out: "Hello world!"
```

Now we need to test it. 
Open terminal, and type: 
```
ventura [path_to_file]
```
Hit enter, and look at result:
```
Hello world!
```
If you get result like this, you doing well! 
Look, Ventura syntax is not so hard. Its easy to learn!