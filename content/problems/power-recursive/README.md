# Power, recursively

Write `power(base, exp)` that returns `base` raised to `exp`, where `exp`
is a whole number zero or more. Use the fact that `base ** exp` is
`base × base ** (exp - 1)`, and anything to the power `0` is `1`.

```static
power(2, 5)  ->  32
power(3, 0)  ->  1
power(5, 1)  ->  5
```

The point is to practise recursion, so write it without a loop and without
`**`.

## Starter

```python
def power(base, exp):
    ...
```

## Hints

1. Base case: `exp == 0` returns `1`.
2. Otherwise return `base * power(base, exp - 1)`.

## Approach

The base case is `exp == 0`. Each call multiplies by `base` once and asks for the power one lower. `power(2, 5)` makes six calls in all.

## Reference

```python
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)
```
