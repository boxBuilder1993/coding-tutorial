# Move the zeros to the end

Rearrange a list so every zero is at the end and the other values keep
their order, without making a new list. Use a writer position: walk the
list with a reader, and every time the reader finds a non-zero value, put
it at the writer's position and advance the writer. When the reader is
done, fill from the writer to the end with zeros.

Write `move_zeros(nums)` that modifies the list in place and returns it.

```static
move_zeros([0, 1, 0, 3, 12])  ->  [1, 3, 12, 0, 0]
```

## Starter

```python
def move_zeros(nums):
    ...
```

## Hints

1. `write = 0`; `for x in nums: if x != 0: nums[write] = x; write += 1`.
2. Then `for i in range(write, len(nums)): nums[i] = 0`.

## Approach

Reader and writer again. The second loop overwrites whatever is left with zeros.

## Reference

```python
def move_zeros(nums):
    write = 0
    for x in nums:
        if x != 0:
            nums[write] = x
            write += 1
    for i in range(write, len(nums)):
        nums[i] = 0
    return nums
```
