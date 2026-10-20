---
title: Counting steps: how much work does Python code do?
description: Measure how a loop's step count grows with the input, see why a loop inside a loop gets slow, and learn the names constant, linear, quadratic and O(n).
---
# Counting steps

Every practice problem so far ran on a handful of items, and any correct
answer passed. Real data is bigger: a million orders, a hundred thousand
words. Code that is fine on ten items can take hours on a million. This
page is about seeing that coming before you run it.

The tool is simple: **count the steps**, and watch how the count changes
when the input gets bigger.

## Counting a loop

Here is a search for a value in a list, with a counter added so we can see
how many items it looked at.

```python
def find(items, target):
    steps = 0
    for item in items:
        steps += 1
        if item == target:
            return steps
    return steps

for n in [10, 100, 1000]:
    items = list(range(n))
    print(n, "items, target absent:", find(items, -1), "steps")
```

Ten times more items, ten times more steps. When the step count grows in
step with the input like this, the work is **linear**. The worst case is
when the target is missing or last, so we count that one: a loop over `n`
items is `n` steps.

## A loop inside a loop

Does the list contain the same value twice? The obvious way checks every
pair.

```python
def has_duplicate(items):
    steps = 0
    n = len(items)
    for i in range(n):
        for j in range(i + 1, n):
            steps += 1
            if items[i] == items[j]:
                return True, steps
    return False, steps

for n in [10, 100, 1000]:
    items = list(range(n))
    found, steps = has_duplicate(items)
    print(n, "items:", steps, "steps")
```

Ten times more items, about a **hundred** times more steps. The inner loop
runs for every turn of the outer loop, so the total is roughly `n × n`,
halved because each pair is checked once. That shape is **quadratic**. At a
million items it is five hundred billion steps, which is a long wait.

## The same job in one pass

A set remembers what it has seen, and asking a set "is this in you?" takes
one step however big the set is. That turns the pair check into a single
loop.

```python
def has_duplicate(items):
    steps = 0
    seen = set()
    for item in items:
        steps += 1
        if item in seen:
            return True, steps
        seen.add(item)
    return False, steps

for n in [10, 100, 1000]:
    items = list(range(n))
    found, steps = has_duplicate(items)
    print(n, "items:", steps, "steps")
```

Linear again. The same answer, the same inputs, and at a million items
roughly a million steps instead of five hundred billion. Nothing about the
problem changed; only the way the work was organised.

## Measuring time

Step counts predict time. Here is the check, with a clock instead of a
counter, on two thousand items.

```python
import time

def pairs(items):
    n = len(items)
    for i in range(n):
        for j in range(i + 1, n):
            if items[i] == items[j]:
                return True
    return False

def with_set(items):
    seen = set()
    for item in items:
        if item in seen:
            return True
        seen.add(item)
    return False

items = list(range(2000))
for f in [pairs, with_set]:
    start = time.perf_counter()
    f(items)
    print(f.__name__, "took", round(time.perf_counter() - start, 4), "seconds")
```

Change `2000` to `4000`. The pair version takes about four times longer;
the set version is still too fast to see.

## Naming the shapes

Programmers name these shapes by how the step count grows with `n`, the
size of the input. The names drop exact counts and keep the shape: `n`
steps and `3n + 7` steps are both "linear", because tripling the input
triples both.

| Shape | Written as | Steps for a million items | Where it comes from |
|---|---|---|---|
| constant | O(1) | 1 | one lookup in a dict or set, `append`, `pop`, indexing a list |
| linear | O(n) | 1,000,000 | one loop over the data |
| n log n | O(n log n) | about 20,000,000 | `sorted` and `sort` |
| quadratic | O(n²) | 1,000,000,000,000 | a loop inside a loop over the same data |

The `O(…)` form is what you will see in books, interviews and other
people's code. Read it as "grows like". `O(n²)` means "grows like `n`
squared": ten times the data, a hundred times the work.

A few things that cost more than they look:

- `x in items` on a **list** is a loop. It walks the list, so it is linear.
  Inside another loop over the list it makes the whole thing quadratic.
  `x in items` on a **set** or **dict** is one step.
- `items.pop(0)` and `items.insert(0, x)` shift every element, so they are
  linear. `pop()` and `append` at the end are one step. That is why Module
  4 used `deque` for queues.
- `sorted` once is fine: n log n is close to linear in practice. Sorting
  inside a loop is not.

## Guessing before you run

You do not need the counter to know the shape. Look for loops:

- No loop, or a fixed number of steps: constant.
- One loop over the input: linear. Two loops one after the other: still
  linear.
- A loop with another loop over the same data inside it: quadratic.
- A loop whose body calls `sorted`, or does `in` on a list: a hidden loop
  inside a loop, so quadratic or worse.

Nothing here says quadratic is wrong. For twenty items it does not matter
and the pair version is easier to read. It matters when the input can be
big, and the first step is to notice.

## Try it

:::problem pair-count

:::problem steps-to-find

:::problem has-duplicate-fast

Next: [Recursion](../02-recursion).
