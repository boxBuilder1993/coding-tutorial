# Price difference

Write `difference(a, b)` that returns how far apart two prices are, always
as a positive number (or zero).

```static
difference(40, 25)  ->  15
difference(25, 40)  ->  15
```

## Starter

```python
def difference(a, b):
    ...
```

## Hints

1. Subtract, then `abs`.
2. `abs(a - b)`

## Approach

`abs` removes the sign.

## Reference

```python
def difference(a, b):
    return abs(a - b)
```
