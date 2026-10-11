# Cheapest price

`prices` maps item names to prices and is not empty. Write
`cheapest_price(prices)` that returns the lowest price.

```static
cheapest_price({"apple": 40, "milk": 2.5, "bread": 25})  ->  2.5
```

## Starter

```python
def cheapest_price(prices):
    ...
```

## Hints

1. `min` over the values.
2. `min(prices.values())`

## Approach

`values()` for the numbers, `min` for the smallest. `min(prices)` would give the alphabetically first key instead.

## Reference

```python
def cheapest_price(prices):
    return min(prices.values())
```
