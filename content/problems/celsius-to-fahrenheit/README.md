# Celsius to Fahrenheit

The shop's freezer shows temperatures in Celsius, but the supplier's paperwork
uses Fahrenheit. Write `to_fahrenheit(c)` that converts. The formula is
`c * 9 / 5 + 32`.

```static
to_fahrenheit(0)    ->  32.0
to_fahrenheit(100)  ->  212.0
to_fahrenheit(10)   ->  50.0
```

Some inputs give long decimals, such as `to_fahrenheit(-18)` printing
`-0.3999999999999986` rather than `-0.4`. That is how computers store
decimal numbers, and the checks allow for it.

## Starter

```python
def to_fahrenheit(c):
    ...
```

## Hints

1. The body is one line: `return` followed by the formula with `c` in it.
2. `return c * 9 / 5 + 32`

## Approach

Python does multiplication and division before addition, in the same way
as school arithmetic, so the formula needs no parentheses.

## Reference

```python
def to_fahrenheit(c):
    return c * 9 / 5 + 32
```
