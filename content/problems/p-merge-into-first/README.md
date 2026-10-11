# Merge into the first list

`a` is a sorted list that has extra zeros at the end: exactly enough room
for all of `b`, another sorted list. Merge `b` into `a` so that `a` ends
up sorted, without making a new list. Filling from the **front** would
overwrite values of `a` not yet placed, so fill from the back: compare the
last real value of `a` with the last value of `b`, put the larger in the
last slot, and move inward.

Write `merge_into(a, m, b)` where `m` is how many real values `a` has at
the start, so `len(a)` is always `m + len(b)`. Modify `a` in place and
return it.

```static
merge_into([1, 3, 5, 0, 0], 3, [2, 4])  ->  [1, 2, 3, 4, 5]
```

## Starter

```python
def merge_into(a, m, b):
    ...
```

## Hints

1. Three positions: `i = m - 1`, `j = len(b) - 1`, `fill = len(a) - 1`.
2. While `j >= 0`: if `i >= 0 and a[i] > b[j]` take `a[i]`, else take `b[j]`. Only `b` needs to be exhausted; leftover `a` values are already in place.

## Approach

Working backwards means every slot written is one that has already been read, so nothing is lost. Once `b` is used up, what remains of `a` is already in the right place.

## Reference

```python
def merge_into(a, m, b):
    i = m - 1
    j = len(b) - 1
    fill = len(a) - 1
    while j >= 0:
        if i >= 0 and a[i] > b[j]:
            a[fill] = a[i]
            i -= 1
        else:
            a[fill] = b[j]
            j -= 1
        fill -= 1
    return a
```
