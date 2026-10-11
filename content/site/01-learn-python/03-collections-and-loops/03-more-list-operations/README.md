---
title: Python list methods: insert, remove, pop, sort, and copying lists
description: insert, remove, pop, index, count, sort and sorted, and the surprise when two names refer to one list.
---
# More list operations

Lists have a set of methods for adding, removing and rearranging. Most
change the list in place and return nothing.

## Adding and removing

```python
items = ["apple", "bread", "milk"]
items.insert(1, "eggs")
print(items)

last = items.pop()
print(last)
print(items)
```

`insert(position, value)` puts a value at a position, shifting the rest along.
`pop()` removes and **returns** the last item; `pop(0)` removes the first.

`remove(value)` deletes the **first** matching value only. If the value
appears twice, the second one stays. Removing a value that is not there is an
error.

```python
items = ["apple", "bread", "apple", "milk"]
items.remove("apple")
print(items)
```

## Finding and counting

`index` also stops at the first match. `count` looks at the whole list.

```python
items = ["apple", "bread", "apple", "milk"]
print(items.index("apple"))
print(items.index("apple", 1))
print(items.count("apple"))
```

`items.index("apple", 1)` starts searching from position 1, which is how you
find the second occurrence. Check with `in` first if the value might be
absent, because `index` raises an error when it is.

## Sorting and reversing

```python
prices = [40, 2.5, 25]
prices.sort()
print(prices)

prices.reverse()
print(prices)
```

`sort` and `reverse` change the list in place and return `None`, like
`append`. This is the same trap as before:

```python
prices = [40, 2.5, 25]
prices = prices.sort()
print(prices)
```

If you want a sorted copy and the original untouched, use the `sorted`
function, which returns a new list:

```python
prices = [40, 2.5, 25]
cheapest_first = sorted(prices)
print(cheapest_first)
print(prices)
```

Strings sort alphabetically, but every capital letter comes before every
lowercase one, so `"Milk"` sorts ahead of `"apple"`. `reverse=True` sorts
descending. That is an option passed by name, which is how Python handles
settings a function does not always need; `prices.sort(reverse=True)`
works the same way.

```python
items = ["bread", "Milk", "apple"]
print(sorted(items))
print(sorted(items, reverse=True))
```

A list that mixes numbers and strings cannot be sorted at all. Python has no
rule for whether `"apple"` is less than `40`, so it refuses:

```python expect-error
mixed = ["apple", 40, "bread"]
mixed.sort()
```

## Two names, one list

This surprises everyone once. Assigning a list to a second name does **not**
copy it. Both names refer to the same list, so a change through one shows
through the other.

```python
original = ["apple", "bread"]
alias = original
alias.append("milk")
print(original)
```

To get an independent copy, slice the whole thing with `[:]`, or pass the
list to `list()`, which builds a new list from anything you can loop over:

```python
original = ["apple", "bread"]
copy = original[:]
copy.append("milk")
print(original)
print(copy)

another = list(original)
another.append("eggs")
print(original)
print(another)
```

Strings and numbers never have this problem because they cannot be changed
in place. Lists can, so it matters which list a name points at.

## Try it

:::problem remove-sold-out

:::problem cheapest-first

:::problem copy-and-extend

Next: [While loops](../04-while-loops).
