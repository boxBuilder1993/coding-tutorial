# Most meetings in one room

`meetings` is a list of `(start, end)` pairs. Two meetings clash if one
starts before the other ends; a meeting may start exactly when another
ends. Write `most_meetings(meetings)` that returns the largest number of
meetings that can be held in one room.

```static
most_meetings([(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11)])  ->  3
most_meetings([])  ->  0
```

The point is to practise the earliest-end greedy rule.

## Starter

```python
def most_meetings(meetings):
    ...
```

## Hints

1. Sort by end time.
2. Walk the sorted list keeping `last_end`; take a meeting if its start is at least `last_end`, and update `last_end` to its end.
3. Count the ones taken.

## Approach

Sort by end, one pass, take whatever fits. The earliest-ending compatible meeting leaves the most room for the rest, which is why this is optimal.

## Reference

```python
def most_meetings(meetings):
    count = 0
    last_end = float("-inf")
    for start, end in sorted(meetings, key=lambda m: m[1]):
        if start >= last_end:
            count += 1
            last_end = end
    return count
```
