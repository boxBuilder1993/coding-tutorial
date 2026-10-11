# First item over a price

Write `first_over(prices, limit)` that returns the **position** of the first
value in `prices` that is greater than `limit`, or `-1` if there is none.

```static
first_over([40, 25, 60, 2.5], 50)  ->  2
first_over([40, 25], 50)           ->  -1
```

## Starter

```python
def first_over(prices, limit):
    i = 0
    while i < len(prices):
        ...
        i += 1
    return -1
```

## Hints

1. Inside the loop, compare `prices[i]` with `limit`. The first time the comparison is true, you have the answer, and nothing after that matters.
2. `if prices[i] > limit: return i`. A `return` inside the loop ends the function at once. If the loop finishes without returning, nothing matched, and the `-1` after the loop is returned.

## Approach

Return from inside the loop on the first match; the `return -1` after the loop is only reached when there was none. `for i in range(len(prices))` is the equivalent `for` version.

## Reference

```python
def first_over(prices, limit):
    i = 0
    while i < len(prices):
        if prices[i] > limit:
            return i
        i += 1
    return -1
```
