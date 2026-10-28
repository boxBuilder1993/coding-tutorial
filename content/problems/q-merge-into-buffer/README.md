# Merge into the back of a buffer

`a` is a list whose first `m` items are sorted and whose remaining `len(b)` slots are
zeros, used as spare room. `b` is a sorted list. Write `merge_into(a, m, b)` that merges
`b` into `a` in place so that all of `a` is sorted, and returns `a`.

```static
merge_into([1, 2, 3, 0, 0, 0], 3, [2, 5, 6])  ->  [1, 2, 2, 3, 5, 6]
merge_into([0], 0, [1])                       ->  [1]
merge_into([2, 0], 1, [1])                    ->  [1, 2]
```

The point is to practise filling from the back so that nothing is overwritten before it is used.

## Starter

```python
def merge_into(a, m, b):
    ...
```

## Hints

1. Three indices: `i = m - 1` into the real part of `a`, `j = len(b) - 1` into `b`, `k = len(a) - 1` for where to write.
2. Write the larger of `a[i]` and `b[j]` at `a[k]`, moving the matching index and `k` down.
3. If `b` runs out first, stop; whatever is left of `a` is already in place. If `a` runs out, copy the rest of `b`.

## Approach

Merging from the back uses the free slots first, so no live value is ever overwritten. Linear.

## Reference

```python
def merge_into(a, m, b):
    i, j, k = m - 1, len(b) - 1, len(a) - 1
    while j >= 0:
        if i >= 0 and a[i] > b[j]:
            a[k] = a[i]
            i -= 1
        else:
            a[k] = b[j]
            j -= 1
        k -= 1
    return a
```
