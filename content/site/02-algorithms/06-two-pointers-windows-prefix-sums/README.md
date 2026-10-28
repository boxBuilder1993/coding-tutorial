---
title: Two pointers, sliding windows and prefix sums in Python
description: Three ways to answer questions about stretches of a list in one pass: two pointers on sorted data, a sliding window, and prefix sums.
---
# Two pointers, sliding windows and prefix sums

Many problems ask about a **stretch** of a list: a pair of positions, a run
of consecutive items, the sum between two indices. The obvious answer is a
loop inside a loop, one for each end of the stretch, which is quadratic.
These three techniques replace that with a single pass by moving the ends
cleverly.

## Two pointers on sorted data

In a sorted list, find two numbers that add up to a target. Put one
finger on the smallest and one on the largest. If their sum is too small,
the only way to make it bigger is to move the left finger right. Too big,
move the right finger left. Each step rules out one position for good.

```python
def pair_with_sum(items, target):
    left, right = 0, len(items) - 1
    while left < right:
        total = items[left] + items[right]
        if total == target:
            return [left, right]
        if total < target:
            left += 1
        else:
            right -= 1
    return []

print(pair_with_sum([1, 2, 4, 7, 11, 15], 15))
print(pair_with_sum([1, 2, 4, 7, 11, 15], 30))
```

Each finger moves at most `n` times, so the whole thing is linear. You
wrote this as [two sum, sorted](problem:p-two-sum-sorted); it is also
behind [most water](problem:p-most-water) and the three-sum family.

The other two-pointer shape is **slow and fast**: both start at the left,
the fast one scans, the slow one marks where the next kept item goes.
That is how you remove duplicates from a sorted list in place or move all
zeros to the end without a second list:

```python
def dedupe_sorted(items):
    if not items:
        return 0
    slow = 0
    for fast in range(1, len(items)):
        if items[fast] != items[slow]:
            slow += 1
            items[slow] = items[fast]
    return slow + 1

items = [1, 1, 2, 3, 3, 3, 5]
n = dedupe_sorted(items)
print(n, items[:n])
```

`slow` always points at the last unique value written; everything before
it is the answer so far.

## A window that slides

"The largest total over any three consecutive days" invites summing every
window of three, which costs `3n`, or `kn` for a window of `k`. A sliding
window keeps a running total: when the window moves one step right, add
the item that entered and subtract the item that left.

```python
def best_window(daily, k):
    total = sum(daily[:k])
    best = total
    for i in range(k, len(daily)):
        total += daily[i] - daily[i - k]
        best = max(best, total)
    return best

print(best_window([2, 1, 5, 1, 3, 2], 3))
```

One pass, however large `k` is. This was [best stretch of days](problem:p-sliding-max-sum).

The window does not have to be a fixed size. For "the longest run with no
repeated character", the right end advances one character at a time and
the left end jumps forward only when a repeat appears:

```python
def longest_unique(text):
    last_seen = {}
    start = 0
    best = 0
    for i, ch in enumerate(text):
        if ch in last_seen and last_seen[ch] >= start:
            start = last_seen[ch] + 1
        last_seen[ch] = i
        best = max(best, i - start + 1)
    return best

print(longest_unique("abcabcbb"))
print(longest_unique("bbbbb"))
print(longest_unique("pwwkew"))
```

The window is `text[start:i + 1]`, and the rule that keeps it valid is
"when `ch` was seen inside the window, move `start` past that sighting".
Both ends only ever move right, so the total work is linear. Variable
windows all follow this outline: grow from the right, shrink from the
left until the window is valid again, record the best.

## Prefix sums

Asked many times "what is the sum from index `i` to index `j`?", summing
each time is linear per question. Instead compute once a list of running
totals, where `prefix[k]` is the sum of the first `k` items. Then any
range sum is one subtraction:

```python
def prefix_sums(items):
    prefix = [0]
    for x in items:
        prefix.append(prefix[-1] + x)
    return prefix

sales = [3, 1, 4, 1, 5, 9, 2]
prefix = prefix_sums(sales)
print(prefix)

def range_sum(i, j):
    return prefix[j + 1] - prefix[i]

print(range_sum(2, 4), sum(sales[2:5]))
print(range_sum(0, 6), sum(sales))
```

`prefix` has one more entry than `sales`, starting with `0`, so that the
sum of `sales[i..j]` is `prefix[j + 1] - prefix[i]` with no special case
for `i == 0`. Building it is linear once; every question after that is
constant. You met it as [prefix sums](problem:p-prefix-sums).

Prefix sums also turn "how many stretches sum to exactly `k`" into a
hashing problem: a stretch ending at `j` sums to `k` when
`prefix[j + 1] - k` has appeared as an earlier prefix, so count earlier
prefixes in a dictionary while walking.

## Choosing between them

- Sorted input and a question about pairs: two pointers from the ends.
- Rearranging in place, keeping some items: slow and fast pointers.
- A question about consecutive items with a fixed length: fixed window.
- "Longest" or "shortest" consecutive run satisfying a condition: a
  variable window, if making the window bigger only makes the condition
  harder (or only easier). If the condition can flip back and forth as
  the window grows, a window does not work.
- Many sum queries over ranges: prefix sums.

## Try it

:::problem a-range-sums

:::problem a-shortest-window-sum

:::problem a-closest-pair-sum

Next: [Linked lists](../07-linked-lists).
