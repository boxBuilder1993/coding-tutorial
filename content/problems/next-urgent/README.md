# Next most urgent

`orders` is a list of `(priority, name)` tuples, lower number meaning more
urgent, in no particular order. Write `most_urgent(orders)` that returns the
**name** of the most urgent order without changing the list. The list has
at least one order and no two orders share a priority.

```static
most_urgent([(3, "bread"), (1, "wedding cake"), (2, "sandwiches")])  ->  "wedding cake"
```

## Starter

```python
import heapq

def most_urgent(orders):
    ...
```

## Hints

1. `heapq.nsmallest(1, orders)` gives a list with the one smallest tuple.
2. Take `[0]` of that for the tuple and `[1]` of the tuple for the name. Or use `min(orders)`, which compares tuples the same way.

## Approach

`min(orders)[1]` is the shortest answer; `heapq.nsmallest(1, orders)[0][1]` is the heap version. Both compare tuples by priority first.

## Reference

```python
import heapq

def most_urgent(orders):
    return heapq.nsmallest(1, orders)[0][1]
```
