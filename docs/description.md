# Exercise 1: Define a programming language

# Name: Snail

**Idea: Lua-like with pattern matching.**
**Use case: Embedded scripting.**

## Types:
- String : "", '', """
- Integer : 0
- Float : 0.0, 0f
- Boolean : true, false
- Function (is a value)
- Table / list : []
- Comment : --
- nil : Unassigned. Used to free variables.

## Control structures:
- If / Else
  - Uses {brackets} around the code
  - Allows for else if by typing `else if condition {}`
  - If statement continues until non-if-statement code appears.
- For loop
  - For each in list: `for each x in table {}`
  - For each in map: `for each x, y in table {}`
  - For each in range: `for i = 0, 1 {}`
  - For each in range backwards: `for i = 100, 1, -1 {}`

## Operators:
- Numbers
  - Addition : +
  - Subtraction : -
  - Multiplication : *
  - Division : /
- Strings
  - Concatenation : ++
- Tables
  - Concatenation : ++
- Booleans
  - Equals : ==
  - Not : not
  - And : and
  - Or : or

## Miscellaneous:
(...) -> unpack arguments as list.
{ } -> functions, if statements, etc. No "end" keyword needed.
Whitespace is ignored.

# Design ideas:
0-based indexing. I am not trying to prove a point.
Index -1 is the last element.
Mechanisms > policies

# Examples:

## Comments
```snail
---
A
multi
line
comment
---

-- A comment
```

## If conditions
```snail
if condition {
    Callback()
}
else if condition {
    Callback()
}
else {
    Callback()
}
```
## Functions
```snail
function greet(name) {
    print("Pleased to meet you, " ++ name ++ "!")
}

local function greet(name) {
    name? -> local callback :
    string:name ->
        function() { print("Pleased to meet you, " ++ name ++ "!") },
    int:name ->
        function() { print("Your name is a number. Hello " ++ string:name ++ ".") },
    _:name ->
        function() { print("I do not know how to greet someone whose name is a " ++ name.type ++ ".") },
    .
    callback()
}
```

## Fibonacci
```snail
function fib(n) {
    --- 
    Initialize a pattern match for n.
    Think of the question mark as "What is n?"
    You could also not specify the type, but this may error.

    The Arrow after the question mark tells snail what to do with the value returned.
    It can be assigned to a variable, or put as an argument in a function.
    --- 
    int:n? -> function(ans) { return ans } :
    0 -> 1,
    1 -> 1,
    --- 
    Underscore means any match, but takes a type.
    Whitespace is ignored, so you can easiliy make the code readable and pretty.
    ---
    _ -> 
    fib(n - 1) + fib(n - 2)
    --- 
    A period signifies that the pattern match is done.
    Think of it as a sentence that answers the question from before.

    If nothing follows the period, it may be omitted.
    ---
    .
}

-- Without the comments.
function fib(n) {
    int:n? -> function(ans) { return ans } :
    0 -> 1,
    1 -> 1,
    _ -> 
    fib(n - 1) + fib(n - 2)
    .
}

-- With assignment instead of callback
function fib(n) {
    int:n? -> local ans :
    0 -> 1,
    1 -> 1,
    _ -> 
    fib(n - 1) + fib(n - 2)
    .
    return ans
}
---
What happens if someone passes a non-int?
You can make more cases using periods!
There can even be code between if you like,
as it is just a separate pattern match block.
---
function fib(n) {
    int:n? -> local ans :
    0 -> 1,
    1 -> 1,
    _ -> 
    fib(n - 1) + fib(n - 2)
    .
    --- 
    A pattern pointing to a value like this acts as a shorthand for "return 0".
    --- 
    _:n? -> 0
    .
    return ans
}
---
Or do the non-int pattern match first!
---
function fib(n) {
    !int:n? -> function(){ return 0 } .
    int:n? -> function(ans){ return ans }  :
    0 -> 1,
    1 -> 1,
    _ -> 
    fib(n - 1) + fib(n - 2)
}
```

## Pattern match syntax
```snail
---
Explanation:
{Brackets} means optional.
---

-- Tell snail where to put the result from this pattern match.
{type:}var? -> returned_value :

-- Use a specific pattern, such as a constant value
{type:}pattern -> returned_value_in_this_case,

-- Or use the variable name from earlier.
{type:}var -> returned_value_in_this_case,

---
To run evaluations on the pattern,
simply return a function with the pattern as argument.
The return value inside this function is the result of the pattern match.
---
{type:}pattern -> 
function(pattern){
    local something = evaluate(pattern)
    return something
}
, -- A trailing comma is allowed.
.
-- After the period, the function continues to execute as imperative code.
{Regular code}
```
