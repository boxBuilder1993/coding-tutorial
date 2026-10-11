# Longest streak

`daily` is a list of how many loaves were sold each day. Write
`longest_streak(daily, target)` that returns the length of the longest run of
consecutive days with sales of at least `target`.

```static
longest_streak([5, 12, 14, 3, 10, 11, 15], 10)  ->  3
longest_streak([1, 2], 10)                      ->  0
```

## Starter

```python
def longest_streak(daily, target):
    ...
```

## Hints

1. Track the current run and the best run; reset the current run to 0 when a day misses.
2. `current = current + 1 if x >= target else 0`, then `best = max(best, current)`.

## Approach

A single pass keeping two counters. The reset is the whole trick.

## Reference

```python
def longest_streak(daily, target):
    best = 0
    current = 0
    for x in daily:
        if x >= target:
            current += 1
            best = max(best, current)
        else:
            current = 0
    return best
```
