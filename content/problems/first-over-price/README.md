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

1. Inside the loop, if `prices[i] > limit`, you have the answer: return `i` right away.
2. If the loop finishes without returning, nothing matched, so `-1` is returned after it.

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
