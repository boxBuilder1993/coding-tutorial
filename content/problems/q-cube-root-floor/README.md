# Whole cube root

Write `cube_root_floor(n)` that returns the largest whole number whose cube is at most
`n`, for `n` zero or more.

```static
cube_root_floor(27)  ->  3
cube_root_floor(30)  ->  3
cube_root_floor(0)   ->  0
cube_root_floor(10 ** 18)  ->  1000000
```

The point is to practise binary search on an answer. Floating-point `n ** (1/3)` is off
by one for large `n`, so search over whole numbers.

## Starter

```python
def cube_root_floor(n):
    ...
```

## Hints

1. The answer is between 0 and `n`. Guess the middle, cube it, compare.
2. Record the guess when `mid ** 3 <= n` and search higher; otherwise search lower.

## Approach

The condition `x ** 3 <= n` is true for small `x` and false for large, so binary search finds the last true. About sixty steps for `n` up to ten to the eighteen.

## Reference

```python
def cube_root_floor(n):
    low, high = 0, n
    best = 0
    while low <= high:
        mid = (low + high) // 2
        if mid ** 3 <= n:
            best = mid
            low = mid + 1
        else:
            high = mid - 1
    return best
```
