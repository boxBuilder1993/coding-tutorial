---
title: Hashing in Python: why dict and set lookups are constant time
description: What a hash table does under dict and set, what can be a key, and the patterns it enables: seen-sets, grouping by a computed key, and complement lookup.
---
# Hashing

`dict` and `set` have appeared on nearly every page since Module 3, and
[Counting steps](../01-counting-steps) claimed that looking something up
in them takes one step however big they are. This page explains why, and
names the handful of patterns that turn a quadratic loop into a linear one.

## What a hash table does

A list finds a value by walking. A dictionary finds a key by
**computing where it must be**. Every key is run through a function called
a hash, which turns it into a number; that number, reduced to the size of
the table, is the slot the key lives in. Looking up `prices["bread"]`
hashes `"bread"`, goes straight to the slot, and checks. No walk.

```python
print(hash("bread"))
print(hash("bread") == hash("bread"))
print(hash(42), hash(42.0))
print(hash((1, 2)))
```

The actual numbers are not meaningful and change between runs; what
matters is that the same value always hashes to the same number in one
run, and different values almost always hash differently. When two keys
do land in the same slot, the table keeps both and checks each, which is
rare enough that lookups stay constant on average.

This is why `in` on a set is one step and `in` on a list is a walk, and
why every "find duplicates" or "have I seen this" problem wants a set.

## What can be a key

A key must not change after it is stored, or its hash would no longer
point at its slot. So keys must be **immutable**: numbers, strings,
tuples of immutables, `None`, booleans. Lists, dictionaries and sets
cannot be keys.

```python expect-error
seen = set()
seen.add([1, 2])
```

The error says `unhashable type: 'list'`. The fix is to convert: a list
becomes a tuple, `tuple(items)`; a set becomes `frozenset(items)`; a
string you want to compare ignoring order becomes `"".join(sorted(word))`.
That last conversion is the key to a whole family of problems.

## Pattern 1: the seen set

Have I met this before? One set, one loop.

```python
def first_repeat(items):
    seen = set()
    for item in items:
        if item in seen:
            return item
        seen.add(item)
    return None

print(first_repeat(["apple", "bread", "milk", "bread", "apple"]))
```

Variations: return all items that appear more than once (a second set for
"reported"), items in one list but not another (`set(a) - set(b)`),
items common to both (`set(a) & set(b)`). All linear. All quadratic
without the set.

## Pattern 2: group by a computed key

Two words are anagrams when their sorted letters match. So sort the
letters, use the result as a dictionary key, and every anagram of a word
lands in the same group:

```python
from collections import defaultdict

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
groups = defaultdict(list)
for word in words:
    key = "".join(sorted(word))
    groups[key].append(word)
print(dict(groups))
print(list(groups.values()))
```

The computed key is the whole idea. Group points by which quadrant they
fall in, orders by customer, numbers by remainder when divided by `k`,
words by length: decide what "the same" means, write a function that
returns the same value for things that are the same, and the dictionary
does the grouping.

## Pattern 3: look up the complement

Which two numbers add up to a target? The pairwise loop is quadratic. The
linear version asks, for each number, "have I already seen the number
that would complete it?"

```python
def two_sum(nums, target):
    index_of = {}
    for i, x in enumerate(nums):
        if target - x in index_of:
            return [index_of[target - x], i]
        index_of[x] = i
    return []

print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
```

Storing the index as the value, not just the number, means the answer is
ready when the complement is found. You wrote this one in the practice
band as [two sum with a dict](problem:p-two-sum-dict). The same shape
answers "is there a pair with difference `k`" (look up `x - k` and
`x + k`), "two words that together use every letter", and any problem
where each item has one partner you can compute.

## Pattern 4: remember answers

A dictionary from inputs to results makes a slow function fast when the
same inputs recur. This is the fix for the recursive Fibonacci from
[Recursion](../02-recursion), and the page on dynamic programming makes a
whole method of it. For now, the shape:

```python
cache = {}
calls = 0

def fib(n):
    global calls
    calls += 1
    if n in cache:
        return cache[n]
    result = n if n < 2 else fib(n - 1) + fib(n - 2)
    cache[n] = result
    return result

print(fib(30), "with", calls, "calls")
```

Thirty-odd calls instead of two and a half million.

## When a dict is the wrong tool

- Order by value: a dictionary cannot tell you the smallest key without
  looking at all of them. Sorted list plus binary search, or a heap.
- Range questions, "how many between 10 and 20": same problem. Sort.
- Small fixed alphabets: a list of 26 counts indexed by letter is a
  hash table with the hash function `ord(ch) - ord("a")`, and faster.
- Memory: a dictionary of a million entries is tens of megabytes. Fine on
  a laptop, worth knowing.

## Try it

:::problem a-group-anagrams

:::problem a-common-items

:::problem a-pairs-with-difference

Next: [Two pointers, sliding windows and prefix sums](../06-two-pointers-windows-prefix-sums).
