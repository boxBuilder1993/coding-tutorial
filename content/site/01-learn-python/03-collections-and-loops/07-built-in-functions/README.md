---
title: Python built-in functions: range, sorted, enumerate, zip, any, all
description: The built-ins worth knowing by heart: abs, round, min, max, sum, int, float, str, range, sorted with key and lambda, enumerate, zip, any and all.
---
# Built-in functions

Python comes with a small set of functions that are always available, no
import needed. You have met `print`, `len`, `range`, `str` and `int`. Here
are the rest worth knowing by heart.

## Working with numbers

```python
print(abs(-7))
print(round(2.567, 2))
print(round(2.7))
print(round(2.5))
print(min(40, 25, 2.5))
print(max([40, 25, 2.5]))
print(sum([40, 25, 2.5]))
```

`min`, `max` and `sum` take a list, or several separate values for `min` and
`max`. `round` with one argument gives a whole number; with two, it rounds to
that many decimal places. One surprise: a value exactly halfway, like `2.5`,
rounds to the nearest **even** number, so `round(2.5)` is `2` and
`round(3.5)` is `4`. `sum` only works on numbers.

## Converting between types

Python has names for its kinds of value: a whole number is an `int`, a
number with a decimal point is a `float`, and text is a `str`. Each name is
also a function that converts to that kind.

```python
print(int("42") + 1)
print(float("2.5") * 2)
print(str(120) + " total")
print(int(3.9))
print(type(3.9))
print(type("milk"))
```

`int` on a decimal number drops the fraction rather than rounding. `type`
tells you what kind of value you have, printed as `<class 'float'>` and so
on, which is handy when something is not behaving as expected.

## range, properly

`range` produces a sequence of numbers on demand. One argument is the stop,
two are start and stop, three add a step.

```python
print(range(5))
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
argument tells it what to sort by: you hand it a function, and `sorted`
calls that function on each item and orders by the results. Notice there
are no parentheses after `len` below. You are passing the function itself,
not calling it; `sorted` does the calling.

```python
items = ["bread", "Apple", "milk"]
print(sorted(items))
print(sorted(items, key=str.lower))
print(sorted(items, key=len))
print(sorted([40, 25, 2.5], reverse=True))
```

`key=len` sorts shortest first. `key=str.lower` sorts ignoring capitals;
`str.lower` is the `lower` method looked up on the `str` type, so it can be
handed over like any function. The same `key` works for `min` and `max`:
`max(items, key=len)` is the longest. `heapq.nsmallest` and `nlargest`,
which you meet in the next section, accept `key` in the same way.

When no ready-made function does what you want, write a tiny one inline
with `lambda`. `lambda s: s.lower()` means "a function that takes `s` and
gives back `s.lower()`":

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

## any and all: a yes-or-no about a whole list

`any` returns `True` if at least one value in a list is true; `all` returns
`True` only if every value is. On their own they look pointless, because
lists of booleans are rare. They earn their place combined with a loop
written inside the brackets, which produces one boolean per item:

```python
quantities = [3, 0, 5]
print(any(q == 0 for q in quantities))
print(all(q > 0 for q in quantities))

prices = [40, 25, 2.5]
print(all(p > 0 for p in prices))
```

Read `any(q == 0 for q in quantities)` as "is `q == 0` for any `q` in
`quantities`?". The inside is a loop that produces `q == 0` for each
quantity, and `any` says whether one of them came out `True`. It stops as
soon as it knows, so `any` on a million items can finish after the first.

Without them you would write a loop with a flag variable. Compare:

```python
quantities = [3, 0, 5]
out_of_stock = False
for q in quantities:
    if q == 0:
        out_of_stock = True
        break
print(out_of_stock)
print(any(q == 0 for q in quantities))
```

Same answer, one line instead of six. `all` of an empty list is `True` and
`any` of an empty list is `False`, which is usually what you want: "every
item of nothing is in stock" is vacuously true.

## Try it

:::problem all-in-stock

:::problem total-with-sum

:::problem numbered-receipt

:::problem pair-up

Next: [Counting with Counter](../08-counting-with-counter).
