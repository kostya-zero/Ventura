# Main Package
Package "main" is default package in Ventura. 
Package include standard functions to out, receive data and manage it. 
Also, there's include a console tools.
Every function in this package starts with "&" character. 

## Basics
Basic function of this package is **&out** and **&lnout**. 
**&out** outputs data to the console. 
**&lnout** outputs data to the console and starts a new line.
Function can output only text type.
Also, you can type name of variable, but it must have text type value.

```
;entry main
;prog_name "output_demo"
;entry
    >> Outputs data on current line
    &out: "Hello World!"
    >> Outputs data on current line and starts a new one
    &lnout: "Ventura is cool!"
```

In this example we had printed text to console window.
By the way, Ventura **supports comment strings**. 
To identify this like a comment string, add **">>"** prefix, like in example below:

```
;entry main
;prog_name "comments_demo"
;entry
    >> This is a comment string.
    >> Interpreter doesn't execute this.
    >> You can write here what you want!
```
## Inputs and set values
Package include functions to manage variable value.
**&sv** sets a new value to variable.
It works for every type of variables, text or number.

```
;entry main
;prog_name "set_demo"
;new $word
;entry
    &sv: $word, "Hello!"
    &out: $word
```

And, you can receive value from user.
**&get_in** made for it.
It receives data from user and adds it to variable of text type.

```
;entry main
;prog_name "input_demo"
;new $word
;entry
    &get_in: $word
    &out: $word
```