# Merge sort

Write `merge_sort(items)` that returns a new sorted list using merge
sort: split the list in half, sort each half with `merge_sort`, and merge
the two sorted halves. Do not change the list you were given.

```static
merge_sort([8, 3, 12, 5, 1, 9, 3])  ->  [1, 3, 3, 5, 8, 9, 12]
merge_sort([])                       ->  []
```

The point is to practise divide and conquer, so write the recursion and
the merge yourself rather than calling `sorted`. One check sorts fifty
thousand items, where a quadratic sort would not finish in the ten-second
limit.

## Starter

```python
def merge_sort(items):
    ...
```

## Hints

1. Base case: a list of length 0 or 1 is already sorted; return it.
2. `mid = len(items) // 2`, then `merge_sort(items[:mid])` and `merge_sort(items[mid:])`.
3. Merge with two indices, one per half, always appending the smaller front item; then extend with whatever is left of either half.

## Approach

A `merge(left, right)` helper that walks both lists with two indices and appends the smaller current item, then appends the remainder. `merge_sort` returns the input when it has fewer than two items, otherwise merges the sorted halves. Using `<=` in the merge keeps equal items in their original order.

## Reference

```python
def merge_sort(items):
    if len(items) <= 1:
        return list(items)
    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    out = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1
    out.extend(left[i:])
    out.extend(right[j:])
    return out
```
