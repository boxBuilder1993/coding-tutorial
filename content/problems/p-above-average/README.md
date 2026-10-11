# Above average

Write `above_average(prices)` that returns how many prices in a non-empty
list are strictly greater than the average of the list.

```static
above_average([40, 25, 2.5, 60])  ->  2
above_average([5, 5, 5])          ->  0
```

## Starter

```python
def above_average(prices):
    ...
```

## Hints

1. Compute the average once, then count with a loop.
2. `avg = sum(prices) / len(prices)` then `if p > avg: count += 1`.

## Approach

Two passes: compute the average once, before the loop, then count.

## Reference

```python
def above_average(prices):
    avg = sum(prices) / len(prices)
    count = 0
    for p in prices:
        if p > avg:
            count += 1
    return count
```
