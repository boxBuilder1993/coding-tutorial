# Celsius to Fahrenheit

The shop's freezer shows temperatures in Celsius, but the supplier's paperwork
uses Fahrenheit. Write `to_fahrenheit(c)` that converts. The formula is
`c * 9 / 5 + 32`.

```static
to_fahrenheit(0)    ->  32.0
to_fahrenheit(100)  ->  212.0
to_fahrenheit(-18)  ->  -0.4
```

## Starter

```python
def to_fahrenheit(c):
    ...
```

## Hints

1. Translate the formula directly, then return it.
2. `return c * 9 / 5 + 32`

## Approach

Multiplication and division happen before addition, so the formula needs no parentheses.

## Reference

```python
def to_fahrenheit(c):
    return c * 9 / 5 + 32
```
