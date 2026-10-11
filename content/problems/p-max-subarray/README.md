# Best run of days

Daily profits can be negative. Find the largest total over any run of
consecutive days (at least one day). One method: walk the days keeping a
running total of the current run. For each day, in this order: add the
day to the running total; if the running total is now the best seen so
far, remember it; then, if the running total is below zero, reset it to
zero, because a negative run can only hurt whatever comes next. Because a
run must have at least one day, start `best` at the first day's profit,
not at zero, so that an all-negative list still gives the least bad day.

Write `best_run(profits)` for a non-empty list.

```static
best_run([-2, 1, -3, 4, -1, 2, 1, -5, 4])  ->  6     (4 - 1 + 2 + 1)
best_run([-3, -1, -2])                     ->  -1
```

## Starter

```python
def best_run(profits):
    ...
```

## Hints

1. Two numbers, `best` and `current`, updated once per day in the order the description gives.
2. A shorter equivalent: `current = max(current + p, p)` then `best = max(best, current)`. Taking `p` on its own is the reset.

## Approach

One pass, two numbers. Updating `best` before the reset is what makes the
all-negative case work: the best single day is recorded before the running
total is thrown away.

## Reference

```python
def best_run(profits):
    best = profits[0]
    current = 0
    for p in profits:
        current = max(current + p, p)
        best = max(best, current)
    return best
```
