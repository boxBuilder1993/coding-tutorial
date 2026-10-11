# Just the number

Product codes mix letters, dashes and digits. Write `code_number(code)` that
returns the digits of the code, in order, as a single whole number. Every
code has at least one digit. Leading zeros disappear, as they do for any
number.

```static
code_number("BRD-1042-A")  ->  1042
code_number("x7y")         ->  7
code_number("A007")        ->  7
```

## Starter

```python
def code_number(code):
    ...
```

## Hints

1. Collect characters that are in `"0123456789"`, then `int` the result.
2. Build a string of digits with `+=`, then `return int(digits)`.

## Approach

Filter the characters to digits, join them, convert once with `int`.

## Reference

```python
def code_number(code):
    digits = ""
    for ch in code:
        if ch in "0123456789":
            digits += ch
    return int(digits)
```
