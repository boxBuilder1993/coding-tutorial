---
title: Recursion in Python: functions that call themselves
description: How a function can call itself, why it needs a base case, what the call stack does, and the problems where recursion is simpler than a loop.
---
# Recursion

A function can call itself. That sounds like it should loop forever, and
it does unless the function also knows when to stop. Used with care it
solves a kind of problem that loops handle badly: problems whose parts look
like smaller copies of the whole.

## A function that calls itself

```python
def count_down(n):
    if n == 0:
        print("done")
        return
    print(n)
    count_down(n - 1)

count_down(3)
```

`count_down(3)` prints `3` and calls `count_down(2)`, which prints `2` and
calls `count_down(1)`, and so on until `count_down(0)` prints `done` and
returns without calling anything. Two parts make it work:

- A **base case**: an input so small the answer is immediate. Here, `n == 0`.
- A **smaller call**: the function calls itself with an input closer to the
  base case. Here, `n - 1`.

Remove the base case and the calls never stop. Python gives up after a few
thousand nested calls:

```python expect-error
def forever(n):
    return forever(n + 1)

forever(0)
```

That error, `RecursionError`, almost always means a missing or unreachable
base case.

## Where the calls wait

When `count_down(3)` calls `count_down(2)`, the first call is not finished:
it is paused, waiting for the inner call to return. Python keeps the paused
calls on a **stack**, the same last-in-first-out pile from
[Module 4](../../01-learn-python/04-stacks-queues-and-priority-queues/01-stacks).
Each new call goes on top; when it returns, it comes off and the call below
resumes.

You can see the stack grow and shrink by printing after the recursive call
too:

```python
def show(n, depth=0):
    pad = "  " * depth
    print(pad + "enter", n)
    if n > 0:
        show(n - 1, depth + 1)
    print(pad + "leave", n)

show(3)
```

Every `enter` happens on the way down, every `leave` on the way back up,
in reverse order. Whatever a function does after its recursive call happens
once the deeper calls are all finished.

## Returning values

The useful form returns something. The sum of a list is the first item plus
the sum of the rest, and the sum of an empty list is zero:

```python
def total(items):
    if not items:
        return 0
    return items[0] + total(items[1:])

print(total([3, 5, 7]))
print(total([]))
```

Trace it: `total([3, 5, 7])` is `3 + total([5, 7])`, which is
`3 + (5 + total([7]))`, which is `3 + (5 + (7 + total([])))`, which is
`3 + (5 + (7 + 0))`. The base case supplies the first concrete number and
the additions happen on the way back up.

Factorial has the same shape. `5!` is `5 × 4!`, and `0!` is `1`:

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
```

Every recursive function you write will have this outline:

```python static
def solve(problem):
    if problem is trivial:
        return the immediate answer
    smaller = solve(a smaller version of problem)
    return combine(problem, smaller)
```

## When a loop is not enough

The examples so far could be loops, and as loops they would be fine. The
case for recursion is data that is nested, where "the rest" is not a
shorter list but a list inside a list.

A shopping list might contain sub-lists: a list for the bakery, a list for
the dairy aisle, each possibly containing further lists. To count every
item, a single loop cannot look inside the inner lists, and a loop inside a
loop only goes one level deeper. Recursion goes as deep as the data does:

```python
def count_items(items):
    count = 0
    for item in items:
        if isinstance(item, list):
            count += count_items(item)
        else:
            count += 1
    return count

shopping = ["apple", ["bread", "rolls", ["jam"]], "milk", ["eggs"]]
print(count_items(shopping))
```

`isinstance(item, list)` asks whether `item` is a list. If it is, the
function hands it to itself; if not, it is one item. The base case is
hidden in the loop: an item that is not a list contributes one and
causes no further call.

This is the shape of most real recursion: folders inside folders, replies
to replies, parts made of parts. Trees and graphs, later in this section,
are built on it.

## Counting the calls

Recursion is code, so the previous page applies. The Fibonacci numbers are
defined by each being the sum of the two before it: `0, 1, 1, 2, 3, 5, 8,
…`. Written straight from the definition:

```python
calls = 0

def fib(n):
    global calls
    calls += 1
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

for n in [10, 15, 20, 25]:
    calls = 0
    print("fib(", n, ") =", fib(n), "after", calls, "calls")
```

Five more in `n` means about eleven times the calls. `fib(40)` would take
minutes. The waste is visible in the trace: `fib(5)` calls `fib(3)` twice,
`fib(2)` three times, and so on, recomputing answers it already had. The
fix is to remember answers, which has its own page later. For now the
lesson is that a recursive function calling itself twice per step can be
far more expensive than it looks.

## Recursion or a loop?

- If the data is flat, a list or a range, a loop is usually clearer and
  cannot hit the recursion limit.
- If the data is nested, or the problem is "do this, then do the same to
  each part", recursion is clearer and a loop gets awkward fast.
- Either way, find the base case first. If you cannot say when it stops,
  it will not.

## Try it

The point of these is to practise recursion, so write each one as a
function that calls itself, even where a loop would do.

:::problem sum-recursive

:::problem power-recursive

:::problem flatten-list

:::problem fib-recursive

Next: [Searching](../03-searching).
