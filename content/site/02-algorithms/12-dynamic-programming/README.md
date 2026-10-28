---
title: Dynamic programming in Python: memoisation and tables, step by step
description: Remember answers to turn exponential recursion linear: Fibonacci, stairs, fewest coins, house robber and grid paths, from memo dictionary to table.
---
# Dynamic programming

The recursive Fibonacci from [Recursion](../02-recursion) made two and a
half million calls for `fib(30)` because it kept recomputing the same
subproblems. **Dynamic programming** is the name for fixing that: when a
problem breaks into overlapping smaller problems, solve each small problem
once, remember the answer, and build up. The name is historical and means
nothing; think "recursion plus a notebook".

It is the most feared topic in interviews and the most mechanical once
you see that every DP problem is answered by the same three questions.

## Memoisation: recursion plus a dictionary

Keep the recursive function, add a cache:

```python
memo = {}

def fib(n):
    if n in memo:
        return memo[n]
    if n < 2:
        return n
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]

print(fib(30), fib(90))
print(len(memo), "answers remembered")
```

Each `n` is computed once and looked up ever after, so `fib(90)` takes
about ninety calls instead of trillions. This is the
[remember answers](../05-hashing) pattern from hashing applied to a
function's own arguments. Python has it built in: put
`@functools.lru_cache(maxsize=None)` above a function and its results are
cached automatically.

Memoisation changes nothing about how you think; you write the natural
recursion and add three lines. Its only limit is recursion depth, which
for `fib(100000)` would overflow the stack.

## Tables: build up from the bottom

Instead of starting at `n` and recursing down, start at the base cases
and fill a list upwards. Same subproblems, same answers, no recursion:

```python
def fib(n):
    if n < 2:
        return n
    table = [0] * (n + 1)
    table[1] = 1
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]

print(fib(30), fib(90))
```

`table[i]` holds the answer to the subproblem "fib of i". The loop runs in
the order that guarantees the two entries each step needs are already
filled. Since only the last two entries are ever read, two variables would
do instead of the whole table; that space saving is a common follow-up.

Memoisation and tables are the same algorithm in different clothing. Start
with memoisation when thinking, because it follows the recursion; convert
to a table when depth or speed matters.

## The three questions

Every DP problem is set up by answering:

1. **What is the subproblem?** Define a function of a small number of
   parameters whose value you want, like `fib(n)`, `ways(n)`,
   `fewest(amount)`, `best(i)`. The parameters are usually "how much of
   the input is left".
2. **How does a subproblem's answer come from smaller ones?** This is the
   recursive case, and the whole difficulty of the problem lives here.
3. **What are the base cases?** The smallest inputs with obvious answers.

With those three in hand, the memoised version is a direct transcription
and the table version follows. The rest of the page is the three
questions answered for the classic starter problems.

## Climbing stairs

You can climb 1 or 2 steps at a time. How many different ways up `n`
steps? Subproblem: `ways(n)`. The last move was either a 1-step from
`n - 1` or a 2-step from `n - 2`, so `ways(n) = ways(n - 1) + ways(n - 2)`.
Base: `ways(0) = 1` (one way to stand still), `ways(1) = 1`.

```python
def ways(n):
    table = [1, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]

print([ways(n) for n in range(8)])
```

It is Fibonacci in disguise, which is common: many DP problems share a
recurrence and differ only in the story.

## Fewest coins, where greedy failed

The `30` with coins `25, 10, 1` from the [greedy](../11-greedy) page.
Subproblem: `fewest(amount)`, the fewest coins making exactly `amount`.
The last coin used was some `c`, so `fewest(amount) = 1 + fewest(amount - c)`
for the best `c`. Base: `fewest(0) = 0`; amounts that cannot be made are
infinite.

```python
def fewest_coins(amount, coins):
    INF = float("inf")
    table = [0] + [INF] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a and table[a - c] + 1 < table[a]:
                table[a] = table[a - c] + 1
    return table[amount] if table[amount] != INF else -1

print(fewest_coins(30, [25, 10, 1]))
print(fewest_coins(67, [25, 10, 5, 1]))
print(fewest_coins(3, [2]))
```

Trying every last coin is what greedy refused to do, and it is exactly
what makes this correct. The cost is `amount × len(coins)`, which for
realistic amounts is tiny.

## House robber: take or skip

A row of houses with cash in each; you cannot rob two adjacent ones. The
most you can take? Subproblem: `best(i)`, the most from the first `i`
houses. For house `i`, either skip it (`best(i - 1)`) or take it, in
which case house `i - 1` is out and you add `best(i - 2)`. Base: zero
houses give 0.

```python
def rob(houses):
    prev2, prev1 = 0, 0
    for cash in houses:
        prev2, prev1 = prev1, max(prev1, prev2 + cash)
    return prev1

print(rob([2, 7, 9, 3, 1]))
print(rob([1, 2, 3, 1]))
```

Written with two variables instead of a table, since only the previous
two answers are needed. The "take it or skip it" choice is the heart of a
large family: knapsack, subset sums, longest increasing subsequence.

## Two dimensions: paths through a grid

From the top-left of an `rows × cols` grid, moving only right or down,
how many routes reach the bottom-right? Subproblem: `paths(r, c)`, the
routes to cell `(r, c)`. You arrived from above or from the left, so
`paths(r, c) = paths(r - 1, c) + paths(r, c - 1)`. Base: the first row and
first column have one route each.

```python
def grid_paths(rows, cols):
    table = [[1] * cols for _ in range(rows)]
    for r in range(1, rows):
        for c in range(1, cols):
            table[r][c] = table[r - 1][c] + table[r][c - 1]
    return table[rows - 1][cols - 1]

print(grid_paths(3, 3), grid_paths(3, 7))
```

Two parameters, a two-dimensional table, and the fill order (row by row)
again makes sure what each cell needs is ready. Blocked cells are the
natural extension: set their entry to 0. Edit distance and longest common
subsequence between two strings are the same shape with `i` characters of
one string and `j` of the other as the two parameters.

## Spotting a DP problem

- The question asks for a **count** of ways, a **minimum or maximum**
  over many choices, or whether something is **possible**, and the
  choices interact.
- A greedy rule is tempting but you can break it with a small example.
- Brute force is "try every combination", which is exponential, and the
  combinations share sub-parts.

Then answer the three questions, write the memoised recursion, test it on
tiny inputs by hand, and only then convert to a table if you need to.

## Try it

:::problem a-fib-fast

:::problem a-climb-stairs

:::problem a-fewest-coins

:::problem a-house-robber

:::problem a-grid-paths

Next: [Backtracking](../13-backtracking).
