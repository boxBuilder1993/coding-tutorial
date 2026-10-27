---
title: Python Counter and defaultdict: counting and grouping without the boilerplate
description: collections.Counter counts anything you can loop over and lists the most common; defaultdict groups items without checking for missing keys first.
---
# Counting with Counter

The [dictionaries](../05-dictionaries) page ended with the counting
pattern: look up the count with `get(item, 0)`, add one, store it back.
It comes up so often that Python ships a dictionary that does it for you.

```python
from collections import Counter

basket = ["apple", "bread", "apple", "milk", "apple", "bread"]
counts = Counter(basket)
print(counts)
print(counts["apple"])
print(counts["eggs"])
```

`Counter` takes anything you can loop over and counts each distinct value.
It is a dictionary, so `counts["apple"]` works as usual, with one
difference: a key that was never seen gives `0` instead of an error. That
removes the `get(item, 0)` dance entirely.

The `from collections import Counter` line brings the name in from the
standard library; `collections` is the same module `deque` came from. It
goes at the top of your code, once.

## Counting as you go

You can also start empty and add to it in a loop, which is useful when the
things to count are computed rather than already in a list:

```python
from collections import Counter

counts = Counter()
for line in ["apple x2", "bread x1", "apple x1"]:
    name = line.split()[0]
    counts[name] += 1
print(counts)
```

`counts[name] += 1` on a missing key works, because missing keys read as
`0`. `counts.update(["milk", "milk"])` adds a whole list at once.

## The most common

The reason to reach for `Counter` even when a plain dict would do:
`most_common` returns the items and counts ordered from most to least.

```python
from collections import Counter

counts = Counter("mississippi")
print(counts.most_common())
print(counts.most_common(2))
print(counts.most_common(1)[0][0])
```

Each entry is a `(value, count)` tuple. `most_common(2)` gives the top two.
When two values have the same count, the one seen first comes first. The
last line is the idiom for "the single most frequent thing": take the top
one, then its first element.

Strings count as a sequence of characters, which is what the example
shows. Counting words means splitting first: `Counter(text.split())`.

## Comparing two counts

Counters support arithmetic. Subtracting shows what one has that the other
does not; `&` keeps the smaller count for each key, which is "what both
have".

```python
from collections import Counter

needed = Counter(["apple", "apple", "bread"])
have = Counter(["apple", "bread", "bread", "milk"])
print(needed - have)
print(have - needed)
print(needed & have)
```

Subtraction drops anything that would go to zero or below, so `needed - have`
is exactly the shopping list. This is how anagram checks are usually
written: two words are anagrams when `Counter(a) == Counter(b)`.

## Grouping with defaultdict

The sibling of counting is grouping: every word by its first letter, every
order by its customer. With a plain dictionary you have to create the list
the first time a key appears:

```python
words = ["apple", "bread", "avocado", "milk", "butter"]
groups = {}
for word in words:
    if word[0] not in groups:
        groups[word[0]] = []
    groups[word[0]].append(word)
print(groups)
```

`defaultdict` takes a function that makes the default value, and calls it
for any missing key the moment you touch it:

```python
from collections import defaultdict

words = ["apple", "bread", "avocado", "milk", "butter"]
groups = defaultdict(list)
for word in words:
    groups[word[0]].append(word)
print(dict(groups))
```

`defaultdict(list)` means "a missing key becomes an empty list". `defaultdict(int)`
would give `0`, which is a `Counter` without `most_common`. The `dict(...)`
around it when printing is only to make the output look like a normal
dictionary; it already behaves like one.

## Try it

:::problem most-common-item

:::problem shopping-shortfall

:::problem group-by-length

Next: [Stacks](../../04-stacks-queues-and-priority-queues/01-stacks).
