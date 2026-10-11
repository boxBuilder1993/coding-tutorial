# Count expensive items

Write `count_over(prices, limit)` that returns how many values in `prices`
are strictly greater than `limit`.

```static
count_over([40, 25, 60, 2.5], 30)  ->  2
count_over([40, 25, 60, 2.5], 60)  ->  0
```

## Starter

```python
def count_over(prices, limit):
    count = 0
    for price in prices:
        ...
    return count
```

## Hints

1. Put an `if` inside the loop, and only count when it is true.
2. `if price > limit:` then `count += 1`.

## Approach

Accumulate a count instead of a sum, guarded by the condition.

## Reference

```python
def count_over(prices, limit):
    count = 0
    for price in prices:
        if price > limit:
            count += 1
    return count
```
