# Fibonacci, fast

Write `fib(n)` that returns the `n`-th Fibonacci number, with
`fib(0) = 0` and `fib(1) = 1`, for `n` up to a few thousand.

```static
fib(10)  ->  55
fib(90)  ->  2880067194370816120
```

The point is to practise replacing an exponential recursion with
memoisation or a table. The checks go to `n = 3000`; the plain recursive
version from the recursion page would never finish.

## Starter

```python
def fib(n):
    ...
```

## Hints

1. Table version: start `a, b = 0, 1` and repeat `a, b = b, a + b` `n` times; return `a`.
2. Memo version: a dictionary checked at the top of the recursive function and filled before returning. Watch the recursion depth for large `n`.

## Approach

Each Fibonacci number is computed once. The two-variable loop is the table with only the last two entries kept. Linear in `n`.

## Reference

```python
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```
