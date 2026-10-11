# Remove duplicates in place

A sorted list has duplicates next to each other. Remove them without
making a new list, using two positions: a **reader** that visits every
item, and a **writer** that marks where the next kept item goes. Whenever
the reader sees a value different from the last kept one, copy it to the
writer's position and advance the writer. At the end, the first `writer`
items are the unique values.

Write `dedupe(sorted_nums)` that rearranges the list so its first part
holds the unique values in order, and returns how many there are. Do not
build a new list or use a set.

```static
nums = [1, 1, 2, 3, 3, 3]
dedupe(nums)  ->  3     and nums now starts [1, 2, 3, ...]
```

## Starter

```python
def dedupe(sorted_nums):
    ...
```

## Hints

1. `write = 1` if the list is non-empty; `for read in range(1, len(sorted_nums))`.
2. `if sorted_nums[read] != sorted_nums[write - 1]: sorted_nums[write] = sorted_nums[read]; write += 1`.

## Approach

The writer never overtakes the reader, so copying forward is safe. Everything beyond `write` is leftover and ignored.

## Reference

```python
def dedupe(sorted_nums):
    if not sorted_nums:
        return 0
    write = 1
    for read in range(1, len(sorted_nums)):
        if sorted_nums[read] != sorted_nums[write - 1]:
            sorted_nums[write] = sorted_nums[read]
            write += 1
    return write
```
