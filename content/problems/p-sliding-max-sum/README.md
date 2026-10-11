# Best stretch of days

`daily` is a list of daily sales. Write `best_window(daily, k)` that returns
the largest total over any `k` consecutive days. The list has at least `k` days.

```static
best_window([2, 1, 5, 1, 3, 2], 3)  ->  9     (5 + 1 + 3)
```

## Starter

```python
def best_window(daily, k):
    ...
```

## Hints

1. Sum every slice of length `k`, or slide a window adding the new day and subtracting the old.
2. `for i in range(len(daily) - k + 1): total = sum(daily[i:i + k])`

## Approach

The slicing version is fine here. The sliding version, `window += daily[i] - daily[i - k]`, keeps one running total instead of re-summing each window.

## Reference

```python
def best_window(daily, k):
    best = sum(daily[:k])
    window = best
    for i in range(k, len(daily)):
        window += daily[i] - daily[i - k]
        best = max(best, window)
    return best
```
