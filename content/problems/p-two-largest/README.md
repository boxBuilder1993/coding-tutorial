# Two largest

Write `top_two(prices)` that returns the two largest numbers from a list of
at least two, largest first, using `heapq`.

```static
top_two([40, 25, 2.5, 60])  ->  [60, 40]
```

## Starter

```python
import heapq

def top_two(prices):
    ...
```

## Hints

1. `nlargest` with k = 2.
2. `heapq.nlargest(2, prices)`

## Approach

`nlargest` returns them in descending order already.

## Reference

```python
import heapq

def top_two(prices):
    return heapq.nlargest(2, prices)
```
