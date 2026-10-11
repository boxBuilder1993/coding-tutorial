# Cheapest k

Write `cheapest(prices, k)` that returns the `k` smallest numbers in
`prices`, smallest first. If `k` is larger than the list, return everything
sorted.

```static
cheapest([40, 25, 2.5, 60, 15], 2)  ->  [2.5, 15]
cheapest([40, 25], 5)               ->  [25, 40]
```

## Starter

```python
import heapq

def cheapest(prices, k):
    ...
```

## Hints

1. `heapq.nsmallest(k, prices)` does exactly this.
2. `sorted(prices)[:k]` is the same result by a different route.

## Approach

`nsmallest` already handles `k` larger than the list. For small `k` it is faster than sorting everything.

## Reference

```python
import heapq

def cheapest(prices, k):
    return heapq.nsmallest(k, prices)
```
