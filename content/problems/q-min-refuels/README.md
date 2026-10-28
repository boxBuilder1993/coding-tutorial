# Fewest fuel stops

A car starts with `fuel` units and must travel `target` units, using one unit per
distance. `stations` is a list of `(position, amount)` sorted by position. Write
`min_refuels(target, fuel, stations)` that returns the fewest stops needed to reach the
target, or `-1` if it cannot.

```static
min_refuels(100, 10, [(10, 60), (20, 30), (30, 30), (60, 40)])  ->  2
min_refuels(1, 1, [])  ->  0
min_refuels(100, 1, [(10, 100)])  ->  -1
```

The point is to practise a greedy with a heap: pass stations and remember their fuel, and
only when stuck, take the biggest amount you passed.

## Starter

```python
def min_refuels(target, fuel, stations):
    ...
```

## Hints

1. Max-heap of fuel amounts at stations already passed. `reach = fuel`.
2. Loop: while `reach < target`, if the heap is empty return -1; otherwise pop the largest, add it to `reach`, count a stop. Before that, push every station with position `<= reach`.

## Approach

Deferring the decision until stuck, and then taking the largest skipped amount, is the optimal greedy. Each station is pushed and popped at most once: n log n.

## Reference

```python
import heapq

def min_refuels(target, fuel, stations):
    heap = []
    reach = fuel
    stops = 0
    i = 0
    while reach < target:
        while i < len(stations) and stations[i][0] <= reach:
            heapq.heappush(heap, -stations[i][1])
            i += 1
        if not heap:
            return -1
        reach += -heapq.heappop(heap)
        stops += 1
    return stops
```
