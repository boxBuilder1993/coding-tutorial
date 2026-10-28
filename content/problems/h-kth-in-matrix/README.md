# k-th smallest in a sorted matrix

`matrix` is a list of rows where every row and every column is sorted ascending. Write
`kth_smallest(matrix, k)` that returns the `k`-th smallest value overall, counting repeats.

```static
kth_smallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8)  ->  13
kth_smallest([[-5]], 1)                                   ->  -5
```

Two good routes: a heap merging the rows (k log n), or binary search on the value with a
linear count of how many entries are at most the guess. Flattening and sorting also passes.

## Starter

```python
def kth_smallest(matrix, k):
    ...
```

## Hints

1. Heap route: push `(matrix[r][0], r, 0)` for each row; pop `k` times, pushing the next item in the same row.
2. Value route: `low, high = matrix[0][0], matrix[-1][-1]`. For a guess, count entries `<= guess` by walking from the bottom-left corner. Find the smallest value with count `>= k`.

## Approach

The matrix is `n` sorted lists, so the k-way merge applies; or exploit the sorted columns to count below a threshold in linear time and binary search the threshold.

## Reference

```python
import heapq

def kth_smallest(matrix, k):
    heap = [(row[0], r, 0) for r, row in enumerate(matrix) if row]
    heapq.heapify(heap)
    for _ in range(k):
        value, r, c = heapq.heappop(heap)
        if c + 1 < len(matrix[r]):
            heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))
    return value
```
