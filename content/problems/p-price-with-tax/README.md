# Price with tax

Tax is 10%. Write `with_tax(price)` that returns the price including tax,
rounded to two decimal places.

```static
with_tax(40)    ->  44.0
with_tax(2.55)  ->  2.81
```

## Starter

```python
def with_tax(price):
    ...
```

## Hints

1. Multiply, then `round` with two arguments.
2. `round(price * 1.1, 2)`

## Approach

`round(x, 2)` keeps two decimal places.

## Reference

```python
def with_tax(price):
    return round(price * 1.1, 2)
```
