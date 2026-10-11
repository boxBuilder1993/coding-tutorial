# Lowest and highest

Write `price_range(prices)` that returns a tuple `(lowest, highest)` from
a non-empty list of prices.

```static
price_range([40, 2.5, 25])  ->  (2.5, 40)
```

## Starter

```python
def price_range(prices):
    ...
```

## Hints

1. `min` and `max`, returned together.
2. `return min(prices), max(prices)`

## Approach

Two built-ins and a tuple return.

## Reference

```python
def price_range(prices):
    return min(prices), max(prices)
```
