---
title: Sorting algorithms in Python: insertion, merge sort, and when to just call sorted
description: Why the simple sorts are quadratic, how merge sort reaches n log n by recursion, timing them, and getting the most from sorted with key, tuples and stability.
---
# Sorting

Sorted data is what makes binary search possible, lets you find duplicates
by looking at neighbours, and makes "the top ten" a slice. You will almost
always call `sorted`. This page is about what it costs, what the
alternatives cost, and the one sort worth being able to write.

## The simple sorts are quadratic

You built [selection sort](problem:p-selection-sort) and
[insertion sort](problem:p-insertion-sort) in the practice band. Both have
a loop inside a loop over the same list, so both are O(n²). Here is
insertion sort with a comparison counter to make that concrete:

```python
def insertion_sort(items):
    items = list(items)
    steps = 0
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j - 1] > items[j]:
            steps += 1
            items[j - 1], items[j] = items[j], items[j - 1]
            j -= 1
    return items, steps

import random
for n in [100, 1000]:
    data = [random.randint(0, 10 ** 6) for _ in range(n)]
    result, steps = insertion_sort(data)
    print(n, "items:", steps, "swaps")
```

Ten times the items, about a hundred times the work. Insertion sort has
one redeeming feature: on data that is already nearly sorted it does very
little, because the inner loop stops immediately. That is why it is used
inside faster sorts to finish off small pieces.

## Merge sort: split, sort the halves, merge

The fast sorts all use the same move: do not sort `n` items, sort two
halves of `n/2` and combine. Merge sort combines by **merging**, which you
also built in the practice band as [merge sorted](problem:p-merge-sorted):
walk two sorted lists with one finger on each, always taking the smaller
front item.

```python
def merge(left, right):
    out = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1
    out.extend(left[i:])
    out.extend(right[j:])
    return out

print(merge([1, 4, 9], [2, 3, 10, 11]))
```

Merging is linear: every item is looked at once. The sort is then a short
recursive function, and the halves get sorted by the same function:

```python
def merge(left, right):
    out = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1
    out.extend(left[i:])
    out.extend(right[j:])
    return out

def merge_sort(items):
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    return merge(merge_sort(items[:mid]), merge_sort(items[mid:]))

print(merge_sort([8, 3, 12, 5, 1, 9, 3]))
```

The base case is a list of one item, which is already sorted. Why is this
n log n? Halving a list of `n` down to single items takes about log n
levels of splitting, and at each level the merges together touch all `n`
items once. `n` work per level, log n levels.

Watch it against insertion sort on real data:

```python
import random, time

def insertion_sort(items):
    items = list(items)
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j - 1] > items[j]:
            items[j - 1], items[j] = items[j], items[j - 1]
            j -= 1
    return items

def merge(left, right):
    out = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    out.extend(left[i:]); out.extend(right[j:])
    return out

def merge_sort(items):
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    return merge(merge_sort(items[:mid]), merge_sort(items[mid:]))

data = [random.randint(0, 10 ** 6) for _ in range(3000)]
for f in [insertion_sort, merge_sort, sorted]:
    start = time.perf_counter()
    f(data)
    print(f"{f.__name__:<15}{time.perf_counter() - start:.4f} s")
```

`sorted` wins by a distance because it is written in C and uses a
refinement of the same idea (Timsort, merge sort plus insertion sort on
small runs). Merge sort is the one to be able to write, because it is the
cleanest example of divide and conquer and the shape of many other
algorithms.

## Counting instead of comparing

When the values come from a small known set, you need not compare at all:
count how many of each, then write them out. Sorting a list of grades
`"A"` to `"F"`, or a list of `0`, `1`, `2`:

```python
def sort_small_values(items, values):
    counts = {v: 0 for v in values}
    for item in items:
        counts[item] += 1
    out = []
    for v in values:
        out.extend([v] * counts[v])
    return out

print(sort_small_values([2, 0, 1, 2, 1, 0, 0], [0, 1, 2]))
```

Two linear passes, so this is O(n), faster than any comparison sort can
be. It only works because the possible values were known in advance.

## Getting the most out of sorted

For everything else, `sorted` or `list.sort()`. What is worth knowing:

```python
orders = [("bread", 25), ("apple", 40), ("milk", 25), ("eggs", 60)]

print(sorted(orders, key=lambda o: o[1]))
print(sorted(orders, key=lambda o: o[1], reverse=True))
print(sorted(orders, key=lambda o: (o[1], o[0])))
print(sorted(orders, key=lambda o: (-o[1], o[0])))
```

- **`key` returns what to compare.** A tuple as the key sorts by its first
  element, then breaks ties with the second, and so on. That is how you
  sort by price then name.
- **Negate a number to reverse one field only.** `(-o[1], o[0])` is price
  descending, name ascending. `reverse=True` would reverse both.
- **`sorted` is stable.** Items that compare equal keep their original
  order. In the first line, `bread` stays before `milk` because it came
  first. Sorting by one key and then by another therefore works as you
  would hope: sort by the minor key first, then by the major one.
- **`items.sort()` sorts in place and returns `None`.** `sorted(items)`
  returns a new list and leaves the original alone. Writing
  `items = items.sort()` loses the list.

## Try it

:::problem a-merge-sort

:::problem a-sort-by-price-then-name

:::problem a-sort-grades

Next: [Hashing](../05-hashing).
