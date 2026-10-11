---
title: Python dictionaries: keys, values, get, and counting
description: Look values up by key, add and change entries, handle missing keys with get, loop with items(), and count things.
---
# Dictionaries

A list finds things by position. A **dictionary** finds things by a **key**
you choose. It is the right structure whenever you want to look something up:
the price of an item, the stock for a code, the count for a word.

```python
prices = {"apple": 40, "bread": 25, "milk": 2.5}
print(prices["bread"])
print(len(prices))
```

Curly braces, and each entry is `key: value`. `prices["bread"]` looks up the
value stored under the key `"bread"`. Keys are usually strings or numbers;
values can be anything.

## Adding and changing

Assigning to a key adds the entry if it is new and replaces it if it exists.

```python
prices = {"apple": 40}
prices["bread"] = 25
prices["apple"] = 45
print(prices)
```

## Missing keys

Looking up a key that is not there is a `KeyError`. Check first with `in`, or
use `get`, which returns a default instead of failing.

```python
prices = {"apple": 40, "bread": 25}
print("milk" in prices)
print(prices.get("milk"))
print(prices.get("milk", 0))
```

`in` checks the keys, not the values: `40 in prices` is `False` here. `get`
with no default returns `None`. `get(key, 0)` returns 0 when the key is
missing, which is exactly what counting needs.

## Removing

```python
prices = {"apple": 40, "bread": 25}
del prices["apple"]
print(prices)
```

## Looping over a dictionary

Looping over a dict gives its keys. `items()` gives key and value pairs
together, which is the form you almost always want.

```python
prices = {"apple": 40, "bread": 25, "milk": 2.5}
for item in prices:
    print(item)

for item, price in prices.items():
    print(f"{item} costs {price}")
```

Each round of the second loop hands over one `(key, value)` pair, and
writing two names after `for` splits the pair into them. The next page
covers this splitting, called unpacking, in full. `keys()` and `values()`
give just one side. Entries come out in the order they were added.

## Counting things

The classic dictionary pattern. For each thing, look up its count with a
default of 0, add one, store it back.

```python
basket = ["apple", "bread", "apple", "milk", "apple"]
counts = {}
for item in basket:
    counts[item] = counts.get(item, 0) + 1
print(counts)
```

## Try it

:::problem price-lookup

:::problem apply-price-change

:::problem count-items

Next: [Tuples and sets](../06-tuples-and-sets).
