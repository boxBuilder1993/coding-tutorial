# Merge three sorted lists

Write `merge_three(a, b, c)` that merges three sorted lists into one sorted list.

```static
merge_three([1, 4], [2, 3], [0, 5])  ->  [0, 1, 2, 3, 4, 5]
merge_three([], [], [7])             ->  [7]
```

The point is to practise the merge step, so build it from merges rather than
concatenating and calling `sorted`. Merging the first two and then merging the result
with the third is fine.

## Starter

```python
def merge_three(a, b, c):
    ...
```

## Hints

1. Write `merge(x, y)` with two indices as on the sorting page.
2. Return `merge(merge(a, b), c)`.

## Approach

Two linear merges. The general version with k lists is the heap-based merge from the heaps page.

## Reference

```python
def merge_three(a, b, c):
    def merge(x, y):
        out = []
        i = j = 0
        while i < len(x) and j < len(y):
            if x[i] <= y[j]:
                out.append(x[i])
                i += 1
            else:
                out.append(y[j])
                j += 1
        out.extend(x[i:])
        out.extend(y[j:])
        return out

    return merge(merge(a, b), c)
```
