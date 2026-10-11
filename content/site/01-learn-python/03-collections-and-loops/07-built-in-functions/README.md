# Built-in functions

Python comes with a small set of functions that are always available, no
import needed. You have met `print`, `len`, `range`, `str` and `int`. Here
are the rest worth knowing by heart.

## Working with numbers

```python
print(abs(-7))
print(round(2.567, 2))
print(round(2.5))
print(min(40, 25, 2.5))
print(max([40, 25, 2.5]))
print(sum([40, 25, 2.5]))
```

`min`, `max` and `sum` take a list, or several separate values for `min` and
`max`. `round` with one argument gives a whole number; with two, it rounds to
that many decimal places. `sum` only works on numbers.

## Converting between types

```python
print(int("42") + 1)
print(float("2.5") * 2)
print(str(120) + " total")
print(int(3.9))
print(type(3.9))
```

`int` on a decimal number drops the fraction rather than rounding. `type`
tells you what kind of value you have, which is handy when something is not
behaving as expected.

## range, properly

`range` produces a sequence of numbers on demand. One argument is the stop,
two are start and stop, three add a step.

```python
print(list(range(5)))
print(list(range(2, 6)))
print(list(range(0, 20, 5)))
print(list(range(10, 0, -3)))
```

`range` is not a list; it only produces each number when the loop asks for
it, which is why `print(range(5))` shows `range(0, 5)` and `list(...)` is
needed to see the values.

## sorted, with a twist

`sorted` returns a new sorted list from anything you can loop over. A `key`
argument tells it what to sort by.

```python
items = ["bread", "Apple", "milk"]
print(sorted(items))
print(sorted(items, key=str.lower))
print(sorted(items, key=len))
print(sorted([40, 25, 2.5], reverse=True))
```

`key=str.lower` sorts ignoring capitals; `key=len` sorts shortest first. The
same `key` works for `min` and `max`: `max(items, key=len)` is the longest.

The `key` is a function that is called on each item, and the results decide
the order. When no ready-made function does what you want, write a tiny one
inline with `lambda`. `lambda s: s.lower()` means "a function that takes `s`
and gives back `s.lower()`":

```python
items = ["bread", "Apple", "milk"]
print(sorted(items, key=lambda s: s.lower()))

pairs = [("bread", 25), ("apple", 40), ("milk", 2.5)]
print(sorted(pairs, key=lambda p: p[1]))
print(max(pairs, key=lambda p: p[1]))
```

Sorting the pairs by price is the case where `lambda` earns its place: there
is no built-in function that picks out the second value of a tuple.

## enumerate: position and value together

When you need both the position and the item, `enumerate` gives them as a
pair you can unpack.

```python
items = ["apple", "bread", "milk"]
for i, item in enumerate(items):
    print(i, item)

for i, item in enumerate(items, start=1):
    print(f"{i}. {item}")
```

## zip: walking two lists side by side

`zip` pairs up the items of two lists, position by position. It stops at the
shorter one.

```python
items = ["apple", "bread", "milk"]
prices = [40, 25, 2.5]
for item, price in zip(items, prices):
    print(f"{item}: {price}")

print(dict(zip(items, prices)))
```

That last line builds a dictionary from two lists in one step.

## Try it

:::problem total-with-sum

:::problem numbered-receipt

:::problem pair-up

Next: [Stacks](../../04-stacks-queues-and-priority-queues/01-stacks).
