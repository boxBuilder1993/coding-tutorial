# The missing number

`items` is sorted and contains every whole number from `0` to `len(items)` except one.
Write `missing(items)` that returns the missing number.

```static
missing([0, 1, 2, 4, 5])  ->  3
missing([1, 2, 3])        ->  0
missing([0, 1, 2])        ->  3
```

The point is to practise binary search on a property: before the gap `items[i] == i`,
after it `items[i] == i + 1`.

## Starter

```python
def missing(items):
    ...
```

## Hints

1. Find the first index `i` where `items[i] != i`; that index is the missing number.
2. If no such index exists, the missing number is `len(items)`. Use the boundary form: `low, high = 0, len(items)`.

## Approach

The condition `items[i] != i` is false up to the gap and true after it, so the boundary search finds the first mismatch. A linear scan also passes but takes a million steps on the big case rather than twenty.

## Reference

```python
def missing(items):
    low, high = 0, len(items)
    while low < high:
        mid = (low + high) // 2
        if items[mid] != mid:
            high = mid
        else:
            low = mid + 1
    return low
```
