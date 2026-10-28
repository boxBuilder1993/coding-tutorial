# Count in a sorted list

Write `count_sorted(items, target)` that returns how many times `target` appears in
the sorted list `items`.

```static
count_sorted([1, 2, 2, 2, 3, 5], 2)  ->  3
count_sorted([1, 2, 3], 4)           ->  0
```

The point is to practise combining two boundary searches. One check uses a million
items and ten thousand targets; `items.count(target)` for each is ten billion steps.

## Starter

```python
def count_sorted(items, target):
    ...
```

## Hints

1. Find the first index with `items[i] >= target` and the first with `items[i] > target`; the count is their difference.
2. `bisect.bisect_left` and `bisect.bisect_right` are exactly those two searches, or write them by hand.

## Approach

Two half-open binary searches give the left and right boundary of the run of equal values. Their difference is the count, even when it is zero.

## Reference

```python
import bisect

def count_sorted(items, target):
    return bisect.bisect_right(items, target) - bisect.bisect_left(items, target)
```
