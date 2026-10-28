# Count inversions

An inversion is a pair of positions `i < j` with `items[i] > items[j]`: two items that
are out of order relative to each other. Write `count_inversions(items)` that returns
how many there are. A sorted list has zero.

```static
count_inversions([2, 4, 1, 3, 5])  ->  3     (2,1) (4,1) (4,3)
count_inversions([1, 2, 3])        ->  0
count_inversions([3, 2, 1])        ->  3
```

The point is to practise seeing that merge sort can count while it sorts: whenever the
merge takes from the right half, every remaining item in the left half is an inversion
with it. A pairwise loop also passes, but one check has twenty thousand items.

## Starter

```python
def count_inversions(items):
    ...
```

## Hints

1. In the merge, when `right[j]` is taken before `left[i]`, add `len(left) - i` to the count: all those left items are bigger and come earlier.
2. Return the count along with the merged list from each recursive call, or keep a running total in an outer variable.

## Approach

Merge sort with a counter. Each time the merge chooses from the right, the untaken left items are exactly the inversions involving that right item. n log n.

## Reference

```python
def count_inversions(items):
    def sort(xs):
        if len(xs) <= 1:
            return xs, 0
        mid = len(xs) // 2
        left, a = sort(xs[:mid])
        right, b = sort(xs[mid:])
        out = []
        i = j = 0
        count = a + b
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                out.append(left[i])
                i += 1
            else:
                out.append(right[j])
                j += 1
                count += len(left) - i
        out.extend(left[i:])
        out.extend(right[j:])
        return out, count

    return sort(list(items))[1]
```
