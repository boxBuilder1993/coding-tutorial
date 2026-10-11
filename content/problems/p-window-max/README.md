# Largest in every window

Given a list and a window size `k`, find the largest value in each window
of `k` consecutive items. A direct way is to take `max` of every slice.
Another way uses a `deque` of positions: before adding a new position,
drop positions from the back whose values are smaller than the new value,
since they can never be the maximum while the new one is in the window;
then add the new position at the back. Drop the position at the front if
it has fallen out of the window. The front is always the window's maximum.

Write `window_max(nums, k)` that returns the list of maximums. `k` is at
least 1 and at most the length of the list. Either method is acceptable.

```static
window_max([1, 3, -1, -3, 5, 3, 6, 7], 3)  ->  [3, 3, 5, 5, 6, 7]
```

## Starter

```python
from collections import deque

def window_max(nums, k):
    ...
```

## Hints

1. Simplest: `for i in range(len(nums) - k + 1): result.append(max(nums[i:i + k]))`.
2. Deque version: pop from the back while `nums[dq[-1]] < nums[i]`; pop from the front if `dq[0] <= i - k`; record `nums[dq[0]]` once `i >= k - 1`.

## Approach

The deque holds candidate positions in decreasing value order. Both the slicing version and the deque version pass; the deque one is the technique the description teaches.

## Reference

```python
from collections import deque

def window_max(nums, k):
    dq = deque()
    result = []
    for i, x in enumerate(nums):
        while dq and nums[dq[-1]] < x:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:
            dq.popleft()
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result
```
