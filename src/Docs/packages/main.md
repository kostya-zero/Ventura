# Ventura // Package "main"
**"main"** is a main package for Ventura that's allows doing basic actions.
Include standard functions to output data, get it, executes commands ands work with memory.
All commands in **main** starts with **"&"** symbol.
## Functions
### &out
- **Type** - Basic Function
- **Description** - Function to output data.
- **Syntax:**
```ruby
&out: {text|var}
```

### &lnout
- **Type** - Basic Function
- **Description** - Function to output data and start new line.
- **Syntax:**
```ruby
&lnout: {text|var}
```

### &sv
- **Type** - Memory Managment
- **Description** - Sets value to variable.
- **Syntax:**
```ruby
&sv: {var}, {text|var|num}
```

### &exit
- **Type** - Basic Function
- **Description** - Ends session.
- **Syntax:**
```ruby
&exit
```

### &void
- **Type** - Memory Managment
- **Description** - Deletes variable from memory.
- **Syntax:**
```ruby
&void: {var}
```

### &zero
- **Type** - Memory Managment
- **Description** - Makes variable value empty.
- **Syntax:**
```ruby
&zero: {var}
```

### &wipe
- **Type** - Basic Function
- **Description** - Clears console window.
- **Syntax:**
```ruby
&wipe
```

### &get_in
- **Type** - Basic Function
- **Description** - Gets input and puts it to a variable.
- **Syntax:**
```ruby
&get_in: {var}
```

### &execute
- **Type** - Basic Function
- **Description** - Executes commands with OS shell.
- **Syntax:**
```ruby
&execute: {text|var}
```
