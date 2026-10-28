# Rooms needed

`meetings` is a list of `(start, end)` pairs. A meeting ending at time `t` frees its room
for one starting at `t`. Write `rooms_needed(meetings)` that returns the fewest rooms so
that no two overlapping meetings share one.

```static
rooms_needed([(0, 30), (5, 10), (15, 20)])  ->  2
rooms_needed([(7, 10), (2, 4)])             ->  1
rooms_needed([])                            ->  0
```

The point is to practise a heap of end times: the root is the room that frees up soonest.

## Starter

```python
def rooms_needed(meetings):
    ...
```

## Hints

1. Sort by start. Keep a min-heap of end times of meetings in progress.
2. For each meeting, if the earliest end is at or before its start, pop it (reuse that room). Push the new end. The heap's largest size is the answer.

## Approach

Sorted by start, the heap of end times holds exactly the meetings in progress; its size peaks at the maximum overlap. n log n.

## Reference

```python
import heapq

def rooms_needed(meetings):
    ends = []
    best = 0
    for start, end in sorted(meetings):
        if ends and ends[0] <= start:
            heapq.heappop(ends)
        heapq.heappush(ends, end)
        best = max(best, len(ends))
    return best
```
