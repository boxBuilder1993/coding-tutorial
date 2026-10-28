# Closest pair sum

`items` is a sorted list of at least two whole numbers. Write
`closest_pair_sum(items, target)` that returns the sum of the two
different items whose sum is closest to `target`. If two sums are equally
close, return the smaller sum.

```static
closest_pair_sum([1, 3, 5, 8, 12], 10)   ->  9      (1 + 8; 11 is equally close but larger)
closest_pair_sum([1, 3, 5, 8, 12], 20)   ->  20     (8 + 12)
closest_pair_sum([-4, -1, 2, 6], 0)      ->  1      (-1 + 2)
```

The point is to practise two pointers from both ends of a sorted list.

## Starter

```python
def closest_pair_sum(items, target):
    ...
```

## Hints

1. `left, right = 0, len(items) - 1`; while `left < right`, look at `total = items[left] + items[right]`.
2. Keep the best total seen: closer wins; on a tie the smaller total wins.
3. If `total < target`, move `left` right; otherwise move `right` left. Returning early on an exact match is fine.

## Approach

Each step moves the pointer that can bring the sum closer to the target, ruling out one position for good, so the loop is linear. Track the best sum by comparing `abs(total - target)` to the best distance so far.

## Reference

```python
def closest_pair_sum(items, target):
    left, right = 0, len(items) - 1
    best = items[0] + items[1]
    while left < right:
        total = items[left] + items[right]
        if abs(total - target) < abs(best - target) or (abs(total - target) == abs(best - target) and total < best):
            best = total
        if total < target:
            left += 1
        else:
            right -= 1
    return best
```
