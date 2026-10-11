# Merge overlapping intervals

Each delivery slot is an interval `[start, end]`. Overlapping or touching
slots should be merged into one. Sort the slots by start. Walk through
them keeping the current merged slot: if the next slot starts at or before
the current one ends, extend the current end to the larger of the two
ends; otherwise the current slot is finished, so record it and start a new
one from the next slot.

Write `merge_slots(slots)` that returns the merged slots as a list of
`[start, end]` lists, sorted by start. Do not change the input.

```static
merge_slots([[1, 3], [2, 6], [8, 10], [15, 18]])  ->  [[1, 6], [8, 10], [15, 18]]
merge_slots([[1, 4], [4, 5]])                     ->  [[1, 5]]
```

## Starter

```python
def merge_slots(slots):
    ...
```

## Hints

1. `for start, end in sorted(slots):` with a `merged` list of results.
2. `if merged and start <= merged[-1][1]: merged[-1][1] = max(merged[-1][1], end)` else append `[start, end]`.

## Approach

After sorting, only the most recently merged slot can overlap the next one. Appending a fresh `[start, end]` list keeps the input unchanged.

## Reference

```python
def merge_slots(slots):
    merged = []
    for start, end in sorted(slots):
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
```
