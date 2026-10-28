# The peak of a mountain

`heights` strictly increases up to one peak and then strictly decreases, with at least
three values. Write `peak_index(heights)` that returns the index of the peak.

```static
peak_index([1, 3, 5, 4, 2])  ->  2
peak_index([0, 10, 5])       ->  1
```

The point is to practise binary search where the comparison is between a value and its
neighbour rather than against a target.

## Starter

```python
def peak_index(heights):
    ...
```

## Hints

1. If `heights[mid] < heights[mid + 1]` you are on the rising side: the peak is to the right.
2. Otherwise you are on the peak or the falling side: the peak is at `mid` or to the left. Use `low, high = 0, len - 1` and `while low < high`.

## Approach

Compare the middle with its right neighbour to learn which slope you are on, and discard the other side. `high = mid` (not `mid - 1`) because `mid` might be the peak. Logarithmic.

## Reference

```python
def peak_index(heights):
    low, high = 0, len(heights) - 1
    while low < high:
        mid = (low + high) // 2
        if heights[mid] < heights[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return low
```
