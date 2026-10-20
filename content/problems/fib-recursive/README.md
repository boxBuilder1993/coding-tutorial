# Fibonacci, recursively

The Fibonacci numbers start `0, 1` and each one after that is the sum of
the two before it: `0, 1, 1, 2, 3, 5, 8, 13, …`. Write `fib(n)` that
returns the `n`-th one, counting from `fib(0) = 0`.

```static
fib(0)   ->  0
fib(1)   ->  1
fib(7)   ->  13
fib(20)  ->  6765
```

The point is to practise recursion with two base cases and two recursive
calls. The checks stay at `n` of 25 or less, where the straightforward
version is still quick.

## Starter

```python
def fib(n):
    ...
```

## Hints

1. Two base cases: `fib(0)` is `0` and `fib(1)` is `1`. `if n < 2: return n` covers both.
2. Otherwise return `fib(n - 1) + fib(n - 2)`.

## Approach

Three lines: the base case for `n < 2`, then the sum of the two smaller calls. This version makes about 250,000 calls for `fib(25)`; the previous page explains why, and a later page shows how to fix it.

## Reference

```python
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```
