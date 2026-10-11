# Smallest with a heap

Write `smallest(nums)` that returns the smallest number in a non-empty
list using `heapq`, without changing the list.

```static
smallest([40, 25, 2.5])  ->  2.5
```

## Starter

```python
import heapq

def smallest(nums):
    ...
```

## Hints

1. `nsmallest` returns a list of the k smallest.
2. `heapq.nsmallest(1, nums)[0]`

## Approach

`nsmallest(1, ...)` gives a one-item list; take `[0]`. `min(nums)` is the everyday answer; this one is practice with the module.

## Reference

```python
import heapq

def smallest(nums):
    return heapq.nsmallest(1, nums)[0]
```
