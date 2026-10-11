# Cheapest first

Write `cheapest_first(prices)` that returns a **new** list with the prices in
ascending order, leaving the original list unchanged.

```static
cheapest_first([40, 2.5, 25])  ->  [2.5, 25, 40]
```

## Starter

```python
def cheapest_first(prices):
    ...
```

## Hints

1. `sort()` changes the original, which this drill forbids.
2. `sorted(prices)` returns a new sorted list.

## Approach

`return sorted(prices)`. Copying with `prices[:]` and then `sort()` also works.

## Reference

```python
def cheapest_first(prices):
    return sorted(prices)
```
