# Bubble sort

One way to sort a list is to repeatedly walk along it comparing each pair
of neighbours, and swapping them whenever the left one is bigger. After one
full walk the largest value has "bubbled" to the end. Walk again, and the
second largest settles next to it. After enough walks nothing needs
swapping, and the list is sorted.

Write `bubble_sort(nums)` that sorts the list in place using this method
and returns it. Do not use `sort` or `sorted`.

```static
bubble_sort([5, 1, 4, 2])  ->  [1, 2, 4, 5]
```

## Starter

```python
def bubble_sort(nums):
    ...
```

## Hints

1. Two nested loops: the outer counts walks, the inner compares `nums[i]` and `nums[i + 1]`.
2. Swap with `nums[i], nums[i + 1] = nums[i + 1], nums[i]`. Stopping early when a walk makes no swaps is a nice touch but not required.

## Approach

`n - 1` walks at most, each comparing adjacent pairs. The early-exit flag turns an already-sorted list into a single walk.

## Reference

```python
def bubble_sort(nums):
    n = len(nums)
    for walk in range(n - 1):
        swapped = False
        for i in range(n - 1 - walk):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        if not swapped:
            break
    return nums
```
