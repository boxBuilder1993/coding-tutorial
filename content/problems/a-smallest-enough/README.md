# Smallest box that fits

A shop packs `weights` (a list of positive whole numbers, in order) into
boxes that each hold at most `capacity`, filling each box with consecutive
items until the next one would not fit. Write `smallest_capacity(weights, boxes)`
that returns the smallest capacity for which everything fits into at most
`boxes` boxes.

```static
smallest_capacity([1, 2, 3, 4, 5], 2)      ->  9     (boxes: [1, 2, 3] and [4, 5])
smallest_capacity([1, 2, 3, 4, 5], 5)      ->  5     (each item alone; the heaviest sets the floor)
smallest_capacity([7, 2, 5, 10, 8], 2)     ->  18
```

The point is to practise binary search on an answer. A capacity either
works or it does not, and if a capacity works so does every larger one.
Search the range from the heaviest single item to the total weight.

## Starter

```python
def smallest_capacity(weights, boxes):
    ...
```

## Hints

1. Write a helper `fits(capacity)` that walks the weights, starting a new box whenever the next item would overflow, and returns whether the box count stayed within `boxes`.
2. The answer lies between `max(weights)` (anything smaller cannot hold the heaviest item) and `sum(weights)` (one box holds everything).
3. Binary search that range: if `fits(mid)`, record `mid` and try smaller; otherwise try larger.

## Approach

Two parts. A linear check: greedily pack items in order, counting boxes. A binary search over capacities from `max(weights)` to `sum(weights)`, moving `high` down whenever the check passes and `low` up when it fails. About log(total) checks, each linear.

## Reference

```python
def smallest_capacity(weights, boxes):
    def fits(capacity):
        used, load = 1, 0
        for w in weights:
            if load + w > capacity:
                used += 1
                load = 0
            load += w
        return used <= boxes

    low, high = max(weights), sum(weights)
    best = high
    while low <= high:
        mid = (low + high) // 2
        if fits(mid):
            best = mid
            high = mid - 1
        else:
            low = mid + 1
    return best
```
