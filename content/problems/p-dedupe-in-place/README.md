# Remove duplicates in place

A sorted list has duplicates next to each other. Remove them without
making a new list, using two positions: a **reader** that visits every
item, and a **writer** that marks where the next kept item goes. Whenever
the reader sees a value different from the last kept one, copy it to the
writer's position and advance the writer. At the end, the first `writer`
items are the unique values.

Write `dedupe(sorted_nums)` that rearranges the list so its first part
holds the unique values in order, and returns how many there are. The
point is to practise the reader-and-writer method rather than build a new
list or use a set.

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

1. Keep a `write` position that only moves forward when you keep a value. The first value is always kept, so `write` starts at 1 and the reader starts at position 1.
2. For each `read` position: if the value there differs from the last kept value, which is at `write - 1`, copy it to position `write` and add one to `write`.

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
