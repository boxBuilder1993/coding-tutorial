# More list operations

Lists have a set of methods for adding, removing and rearranging. Most
change the list in place and return nothing.

## Adding and removing

```python
items = ["apple", "bread", "milk"]
items.insert(1, "eggs")
print(items)

items.remove("bread")
print(items)

last = items.pop()
print(last)
print(items)
```

`insert(position, value)` puts a value at a position, shifting the rest along.
`remove(value)` deletes the first matching value, and raises an error if it is
not there. `pop()` removes and **returns** the last item; `pop(0)` removes the
first.

## Finding and counting

```python
items = ["apple", "bread", "milk", "apple"]
print(items.index("bread"))
print(items.count("apple"))
```

`index` gives the position of the first match. Check with `in` first if the
value might be absent, because `index` raises an error when it is.

## Sorting and reversing

```python
prices = [40, 2.5, 25]
prices.sort()
print(prices)

prices.reverse()
print(prices)
```

`sort` and `reverse` change the list in place. If you want a sorted copy and
the original untouched, use the `sorted` function, which returns a new list:

```python
prices = [40, 2.5, 25]
cheapest_first = sorted(prices)
print(cheapest_first)
print(prices)
```

Sorting strings puts them in alphabetical order, with capitals before
lowercase. `sorted(items, reverse=True)` sorts descending.

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

To get an independent copy, slice the whole thing or call `list()`:

```python
original = ["apple", "bread"]
copy = original[:]
copy.append("milk")
print(original)
print(copy)
```

Strings and numbers never have this problem because they cannot be changed
in place. Lists can, so it matters which list a name points at.

## Try it

:::problem remove-sold-out

:::problem cheapest-first

:::problem copy-and-extend

Next: [While loops](../04-while-loops).
