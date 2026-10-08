# Fahrenheit to Celsius

Write a function `to_celsius(f)` that takes a temperature in Fahrenheit and
returns it in Celsius. The formula is `(f - 32) * 5 / 9`.

```static
to_celsius(212)  ->  100.0
to_celsius(32)   ->  0.0
```

## Starter

```python
def to_celsius(f):
    ...
```

## Hints

1. Subtract 32 first, then multiply by 5, then divide by 9.
2. The function must `return` the result, not `print` it.

## Approach

Translate the formula directly. Parentheses make the subtraction happen first.

## Reference

```python
def to_celsius(f):
    return (f - 32) * 5 / 9
```
