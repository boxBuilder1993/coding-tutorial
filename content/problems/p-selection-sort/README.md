# Selection sort

Another way to sort: find the smallest value in the whole list and swap it
into the first position. Then find the smallest among the remaining
positions and swap it into the second. Continue until every position has
been filled with the smallest of what was left.

Write `selection_sort(nums)` that sorts the list in place using this method
and returns it. Do not use `sort`, `sorted` or `min`.

```static
selection_sort([5, 1, 4, 2])  ->  [1, 2, 4, 5]
```

## Starter

```python
def selection_sort(nums):
    ...
```

## Hints

1. Outer loop over the position to fill; inner loop finds the index of the smallest from there on.
2. Track `smallest = i`, update it when `nums[j] < nums[smallest]`, then swap `nums[i]` and `nums[smallest]`.

## Approach

The inner loop is a find-the-smallest loop over a shrinking suffix. One swap per outer iteration.

## Reference

```python
def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        smallest = i
        for j in range(i + 1, n):
            if nums[j] < nums[smallest]:
                smallest = j
        nums[i], nums[smallest] = nums[smallest], nums[i]
    return nums
```
