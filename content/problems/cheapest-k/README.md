# Cheapest k

Write `cheapest(prices, k)` that returns the `k` smallest numbers in
`prices`, smallest first. If `k` is larger than the list, return everything
sorted; if `k` is 0, return an empty list. Do not change `prices`.

```static
cheapest([40, 25, 2.5, 60, 15], 2)  ->  [2.5, 15]
cheapest([40, 25], 5)               ->  [25, 40]
cheapest([40, 25], 0)               ->  []
```

## Starter

```python
import heapq

def cheapest(prices, k):
    ...
```

## Hints

1. `heapq` has a function that returns the k smallest items of a list; it was the last example on the page.
2. `heapq.nsmallest(k, prices)`. `sorted(prices)[:k]` gives the same result by a different route.

## Approach

`nsmallest` already handles `k` larger than the list and `k` equal to 0, and it leaves the list alone.

## Reference

```python
import heapq

def cheapest(prices, k):
    return heapq.nsmallest(k, prices)
```
