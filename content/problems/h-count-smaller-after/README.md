# Count smaller items to the right

Write `smaller_to_right(nums)` that returns a list where entry `i` is how many items to the
right of position `i` are smaller than `nums[i]`.

```static
smaller_to_right([5, 2, 6, 1])  ->  [2, 1, 1, 0]
smaller_to_right([-1, -1])      ->  [0, 0]
```

The pairwise loop is quadratic and passes the small checks. The fast version is merge
sort on `(value, original index)` pairs, counting how many right-half items jump past each
left-half item during the merge. One check has forty thousand items.

## Starter

```python
def smaller_to_right(nums):
    ...
```

## Hints

1. Sort pairs `(value, index)` with merge sort. When merging, every time you take from the left half, add the number already taken from the right half to `result[index]`.
2. Take from the right only while `right_value < left_value` (strictly), so equal values are not counted.

## Approach

During the merge, the count of right-half items already emitted is exactly how many smaller items were to the right of the current left item. n log n.

## Reference

```python
def smaller_to_right(nums):
    result = [0] * len(nums)

    def sort(pairs):
        if len(pairs) <= 1:
            return pairs
        mid = len(pairs) // 2
        left = sort(pairs[:mid])
        right = sort(pairs[mid:])
        out = []
        i = j = 0
        while i < len(left) and j < len(right):
            if right[j][0] < left[i][0]:
                out.append(right[j])
                j += 1
            else:
                result[left[i][1]] += j
                out.append(left[i])
                i += 1
        while i < len(left):
            result[left[i][1]] += j
            out.append(left[i])
            i += 1
        out.extend(right[j:])
        return out

    sort([(v, i) for i, v in enumerate(nums)])
    return result
```
