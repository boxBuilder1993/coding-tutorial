---
title: Binary search in Python: halving the search space
description: Why linear search costs n steps and binary search about log n, how to write binary search without off-by-one errors, bisect, and searching on an answer.
---
# Searching

Finding a value in a list is the first problem where organisation beats
effort. Unsorted, there is nothing to do but look at every item. Sorted,
you can throw away half the list with each look.

## Linear search

The search from [Counting steps](../01-counting-steps): walk the list, stop
when you see the target. `n` steps in the worst case, and the only option
when the data is in no particular order.

```python
def linear_search(items, target):
    for i, item in enumerate(items):
        if item == target:
            return i
    return -1

print(linear_search([8, 3, 12, 5], 12))
print(linear_search([8, 3, 12, 5], 7))
```

Python's `items.index(target)` and `target in items` do exactly this walk.
Both are linear.

## Binary search

If the list is sorted, look at the middle. The target is either there,
or in the left half (if it is smaller than the middle), or in the right
half (if larger). Either way half the list is gone after one comparison.
Repeat on the half that remains.

```python
def binary_search(items, target):
    low, high = 0, len(items) - 1
    steps = 0
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        if items[mid] == target:
            return mid, steps
        if items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, steps

items = list(range(0, 2000, 2))
print(binary_search(items, 1234))
print(binary_search(items, 1235))
print(len(items), "items, about", len(items) // 2, "steps for linear search")
```

A thousand items, ten steps. A million items would take twenty, because
each step halves what is left and a million halves to one in twenty
halvings. That growth has a name, **logarithmic**, written O(log n), and
it is as close to free as searching gets. The n log n cost of `sorted` is
"n things, each costing a binary search's worth".

`low` and `high` mark the stretch of the list that could still hold the
target. Everything else about the loop follows from keeping that true:

- Start with the whole list, `0` to `len - 1`.
- Loop while the stretch is not empty, `low <= high`. With `<` instead, a
  stretch of one item is never examined, and that item is the classic
  missed case.
- After looking at `mid`, exclude it: `mid + 1` or `mid - 1`. Setting
  `low = mid` can loop forever when `low` and `high` are one apart.

Those three lines are where every binary search bug lives. If one
misbehaves, print `low`, `mid` and `high` each turn and watch the stretch
shrink.

The [practice problem](problem:p-binary-search) in the Hard band is this
exact function. Do it again from memory now if you used a hint then.

## Finding the first of many

With repeated values, `binary_search` returns *some* match, not the first.
To find the first, keep going left even after a match: treat a match like
"too big", record it, and shrink `high`.

```python
def first_index(items, target):
    low, high = 0, len(items) - 1
    found = -1
    while low <= high:
        mid = (low + high) // 2
        if items[mid] == target:
            found = mid
            high = mid - 1
        elif items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return found

print(first_index([1, 2, 2, 2, 3, 5], 2))
```

The same idea with `low = mid + 1` on a match finds the last one. Count of
a value in a sorted list is `last - first + 1`, in two binary searches,
which is how the Hard-band [count occurrences](problem:p-count-occurrences-sorted)
is meant to go.

## bisect: the library version

Python has binary search built in, in the `bisect` module. `bisect_left`
returns the position where `target` would be inserted to keep the list
sorted, which is the index of the first item `>= target`.

```python
import bisect

items = [1, 2, 2, 2, 3, 5]
print(bisect.bisect_left(items, 2))
print(bisect.bisect_right(items, 2))
print(bisect.bisect_left(items, 4))
```

`bisect_right` gives the position after the last `2`. The difference is
the count. To test whether a value is present: `i = bisect_left(items, x)`
and then `i < len(items) and items[i] == x`. In real code use `bisect`;
in interviews, be ready to write the loop.

## Searching for an answer, not an item

The trick that makes binary search useful far beyond lists: it works on any
question of the form "what is the smallest `x` for which this is true",
as long as the answer flips from false to true once and never back.

Integer square root, say: the largest whole number whose square is at
most `n`. The candidates are `0` to `n`, and "`x * x <= n`" is true for
small `x` and false for large ones. Binary search over the candidates:

```python
def isqrt(n):
    low, high = 0, n
    best = 0
    while low <= high:
        mid = (low + high) // 2
        if mid * mid <= n:
            best = mid
            low = mid + 1
        else:
            high = mid - 1
    return best

print(isqrt(16), isqrt(17), isqrt(99), isqrt(10 ** 12))
```

No list anywhere. The "items" are the numbers from `0` to `n` and the
comparison is a condition. Any problem that says "find the minimum
capacity, speed or size that still works" is this pattern: guess, check
whether the guess works, halve.

## Try it

:::problem a-first-occurrence

:::problem a-insert-position

:::problem a-smallest-enough

Next: [Sorting](../04-sorting).
