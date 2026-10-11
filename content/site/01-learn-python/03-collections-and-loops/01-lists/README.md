---
title: Python lists: create, index, slice, append
description: Make a list, read items by position, slice it like a string, test membership with in, and change it with append.
---
# Lists

A **list** holds many values in order. You write one with square brackets and
commas.

```python
items = ["apple", "bread", "milk"]
print(items)
print(len(items))
```

A list can hold numbers, strings, booleans, even other lists. Usually all the
values in a list are the same kind of thing, but Python does not insist.

```python
prices = [40, 25, 2.5]
mixed = ["bread", 25, True]
empty = []
print(prices)
print(mixed)
print(len(empty))
```

## Indexing and slicing work exactly like strings

Positions start at 0, negatives count from the end, and slices use
`[start:stop]` with the stop left out.

```python
items = ["apple", "bread", "milk", "eggs", "flour"]
print(items[0])
print(items[-1])
print(items[1:3])
print(items[:2])
print(items[2:])
```

A slice of a list is a new, smaller list. All the string tricks carry over:
`items[:-1]` is everything but the last, `items[::2]` is every second item,
and `items[::-1]` is the list reversed.

```python
items = ["apple", "bread", "milk", "eggs", "flour"]
print(items[:-1])
print(items[::2])
print(items[::-1])
```

## Is it in there?

`in` checks whether a value is one of the items.

```python
items = ["apple", "bread", "milk"]
print("milk" in items)
print("eggs" in items)
```

## Lists can change

Unlike strings, lists can be changed after you make them, without making a
new list. `append` adds an item at the end. Assigning to a position replaces
what is there.

```python
items = ["apple", "bread"]
items.append("milk")
print(items)

items[0] = "pear"
print(items)
```

`append` returns nothing, which Python shows as `None`; it changes the list it was called on. A common
mistake is `items = items.append("milk")`, which sets `items` to `None`.

## Try it

:::problem last-item

:::problem add-to-list

:::problem is-on-the-list

Next: [For loops](../02-for-loops).
