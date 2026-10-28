# Knapsack

`items` is a list of `(weight, value)` pairs and the bag holds at most `capacity` weight.
Each item can be taken once or not at all. Write `best_value(items, capacity)` that
returns the largest total value that fits.

```static
best_value([(1, 1), (3, 4), (4, 5), (5, 7)], 7)  ->  9     (3 + 4)
best_value([(5, 10)], 4)                        ->  0
```

The point is to practise the 0/1 knapsack table, the take-or-skip recurrence over
capacities.

## Starter

```python
def best_value(items, capacity):
    ...
```

## Hints

1. `best[c]` = best value with capacity `c`, starting all zeros.
2. For each item, for `c` from `capacity` down to `weight`: `best[c] = max(best[c], best[c - weight] + value)`. Going downwards stops an item being used twice.

## Approach

Each item either improves some capacities or does not; iterating capacities downward ensures each item is counted at most once. `len(items) * capacity` steps.

## Reference

```python
def best_value(items, capacity):
    best = [0] * (capacity + 1)
    for weight, value in items:
        for c in range(capacity, weight - 1, -1):
            best[c] = max(best[c], best[c - weight] + value)
    return best[capacity]
```
