# A day at the bakery

All of the day's orders are waiting when the bakery opens, as
`(priority, name)` tuples with distinct priorities, where a smaller number
means more urgent. The bakery makes one order per hour, always the most
urgent one still waiting. Write `schedule(orders, hours)` that returns the
names made in the first `hours` hours, in order. If the bakery runs out of
orders early, the list is shorter.

```static
schedule([(3, "bread"), (1, "cake"), (2, "rolls")], 2)  ->  ["cake", "rolls"]
schedule([(1, "cake")], 5)                              ->  ["cake"]
```

## Starter

```python
import heapq

def schedule(orders, hours):
    ...
```

## Hints

1. Push everything on a heap, then pop up to `hours` times.
2. `while hours > 0 and heap:` then `heappop`, append the name, `hours -= 1`.

## Approach

A heap holds the waiting orders; each hour pops the smallest priority. The loop has two stop conditions: the hours are used up, or the heap is empty.

## Reference

```python
import heapq

def schedule(orders, hours):
    heap = []
    for order in orders:
        heapq.heappush(heap, order)
    made = []
    while hours > 0 and heap:
        priority, name = heapq.heappop(heap)
        made.append(name)
        hours -= 1
    return made
```
