# Total price

Write `total(prices)` that returns the sum of all the numbers in `prices`.
Use a loop. An empty list totals 0.

```static
total([40, 25, 2.5])  ->  67.5
total([])             ->  0
```

## Starter

```python
def total(prices):
    result = 0
    for price in prices:
        ...
    return result
```

## Hints

1. Each time round, add the current price to `result`.
2. `result += price`

## Approach

The accumulator shape: start at 0, add each item, return at the end. Python's built-in `sum` does this, and a later page covers it; this drill is about the loop.

## Reference

```python
def total(prices):
    result = 0
    for price in prices:
        result += price
    return result
```
