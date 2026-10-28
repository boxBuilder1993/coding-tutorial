# Climbing stairs

You climb a staircase of `n` steps taking 1 or 2 steps at a time. Write
`ways(n)` that returns how many distinct sequences of steps reach the top.
`ways(0)` is `1` (do nothing).

```static
ways(1)  ->  1
ways(2)  ->  2      (1+1, 2)
ways(3)  ->  3      (1+1+1, 1+2, 2+1)
ways(4)  ->  5
```

The point is to practise the three DP questions: the subproblem is
`ways(k)`, the recurrence is `ways(k - 1) + ways(k - 2)`, and the bases are
`ways(0) = ways(1) = 1`.

## Starter

```python
def ways(n):
    ...
```

## Hints

1. The last step was a 1 from `n - 1` or a 2 from `n - 2`, so add those two counts.
2. Build up from 0 with two variables or a list; do not recurse without a memo, since `ways(40)` is checked.

## Approach

Fibonacci shifted by one. A loop keeping the previous two answers gives linear time and constant space.

## Reference

```python
def ways(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```
