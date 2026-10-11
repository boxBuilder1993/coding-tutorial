# Best run of days

Daily profits can be negative. Find the largest total over any run of
consecutive days (at least one day). One method: walk the days keeping a
running total of the current run. If the running total ever drops below
zero, it can only hurt whatever comes next, so reset it to zero before
adding the next day. Track the best total seen at any point. Because a run
must have at least one day, start `best` at the first day's profit, not at
zero.

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

1. `best = profits[0]`, `current = 0`; for each `p`: `current = max(current + p, p)`, `best = max(best, current)`.
2. The `max(current + p, p)` form is the reset: starting fresh at `p` whenever the old run is a burden.

## Approach

One pass, two numbers. The all-negative case is why `best` starts at the first value.

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
