# Three sum, distinct triplets

Write `three_sum(nums)` that returns every distinct triplet `[a, b, c]` with `a <= b <= c`
from the list that sums to zero, each triplet using three different positions. Order of
the output does not matter.

```static
three_sum([-1, 0, 1, 2, -1, -4])  ->  [[-1, -1, 2], [-1, 0, 1]]
three_sum([0, 0, 0, 0])           ->  [[0, 0, 0]]
three_sum([1, 2])                 ->  []
```

Sort, fix the first element, two pointers for the other two, and skip duplicates on all
three. Quadratic; a triple loop will not finish the largest check.

## Starter

```python
def three_sum(nums):
    ...
```

## Hints

1. Sort. For each `i`, skip if `nums[i] == nums[i - 1]`. Then `left = i + 1`, `right = n - 1`.
2. On a match, record and advance both pointers past any duplicates. On a small sum move left; on a large sum move right.
3. Stop the outer loop once `nums[i] > 0`: three positives cannot sum to zero.

## Approach

Fixing one element reduces the problem to two-sum on a sorted suffix with two pointers. Duplicate skipping on each pointer keeps triplets distinct. Quadratic.

## Reference

```python
def three_sum(nums):
    nums = sorted(nums)
    out = []
    n = len(nums)
    for i in range(n - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                out.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return out
```
