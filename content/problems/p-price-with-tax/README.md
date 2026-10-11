# Price with tax

Write `with_tax(price)` that returns the price plus 10% tax, rounded to two
decimal places.

```static
with_tax(40)     ->  44.0
with_tax(2.5)    ->  2.75
with_tax(19.99)  ->  21.99
```

## Starter

```python
def with_tax(price):
    ...
```

## Hints

1. Work out the price with tax, then `round` with two arguments.
2. `round(price * 1.1, 2)`, or `round(price + price * 0.1, 2)`; both are fine.

## Approach

`round(x, 2)` keeps two decimal places. The last example needs it: without
rounding, `19.99 * 1.1` is `21.989000000000004`.

## Reference

```python
def with_tax(price):
    return round(price * 1.1, 2)
```
