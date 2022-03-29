# Text Package
Text package need to work with text variables in Ventura.
With it, you can initialize, clear spaces, replace characters and more.

To import this package, you should type this before **;entry** function:
```ruby
;extend <text>
```
## Initialization
To initialize variable as **text**, use **init** function.
```ruby
;extend <text>
;prog_name "text_demo"
>> Creting variable for testing.
;new $test
;entry
    >> Warning: This function deletes all data of current variable.
    text.init: $test
    >> Now, we have text variable.
```