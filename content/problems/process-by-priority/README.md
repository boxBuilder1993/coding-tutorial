# Process by priority

`orders` is a list of `(priority, name)` tuples, lower meaning more urgent,
with no two sharing a priority. Write `in_priority_order(orders)` that returns
the **names** in the order they should be processed, most urgent first, using
a heap: push them all, then pop until empty.

```static
in_priority_order([(3, "bread"), (1, "wedding cake"), (2, "sandwiches")])
    ->  ["wedding cake", "sandwiches", "bread"]
```

## Starter

```python
import heapq

def in_priority_order(orders):
    heap = []
    for order in orders:
        ...
    result = []
    while heap:
        ...
    return result
```

## Hints

1. `heapq.heappush(heap, order)` for each tuple.
2. `priority, name = heapq.heappop(heap)` then append `name`.

## Approach

Push everything, pop everything: the heap hands tuples back smallest priority first. `sorted(orders)` would give the same order; the drill is about the heap loop.

## Reference

```python
import heapq

def in_priority_order(orders):
    heap = []
    for order in orders:
        heapq.heappush(heap, order)
    result = []
    while heap:
        priority, name = heapq.heappop(heap)
        result.append(name)
    return result
```
