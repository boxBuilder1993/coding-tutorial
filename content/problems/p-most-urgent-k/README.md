# Most urgent few

`orders` is a list of `(priority, name)` tuples with distinct priorities.
Write `urgent(orders, k)` that returns the names of the `k` most urgent
orders, most urgent first. `k` may exceed the number of orders.

```static
urgent([(3, "bread"), (1, "cake"), (2, "rolls")], 2)  ->  ["cake", "rolls"]
```

## Starter

```python
import heapq

def urgent(orders, k):
    ...
```

## Hints

1. `nsmallest(k, orders)` then take the names.
2. `for priority, name in heapq.nsmallest(k, orders): names.append(name)`

## Approach

`nsmallest` returns the k smallest tuples in ascending order; strip the priorities.

## Reference

```python
import heapq

def urgent(orders, k):
    names = []
    for priority, name in heapq.nsmallest(k, orders):
        names.append(name)
    return names
```
