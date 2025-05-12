# Snail
A toy language developed as the semester project for DAT259: Compilers.

Snail is a Lua-like language designed to be embedded.
It uses tables and lists rather than objects to create any structure you want,
while still retaining relative simplicity for simple tasks.

The main selling point from lua is the addition of functional elements,
namely pattern matching.
(The first iteration is just switch/case with non-verbose syntax)

# Setup:
Read the report ;)

# State of features:

Lists and tables do not work,
they were simply not prioritized.

For each statements do not work.

Pattern matching only works in the interpreter, and only does assignments.
The type check is also not used, as there is no type checking implementation.

The require keyword does nothing.

Loops only work in the interpreter.

Block comments do not work, parsing them was hard.

Function declarations do not work,
and the only existing function is `print()`

## Compiler features
- If-statements with if-else and else-clauses.
- Assignments and scopes.
- Basic operators for arithmetics and comparisons.

## Interpreter features
- If-statements with if-else and else-clauses.
- Assignments and scopes.
- Basic operators for arithmetics and comparisons.
- Pattern matching, matches only on expressions, not types.
- For loops and while loops.

