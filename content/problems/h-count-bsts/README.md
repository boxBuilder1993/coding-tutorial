# How many search trees?

Write `count_trees(n)` that returns how many structurally different binary search trees
hold the values `1` to `n`.

```static
count_trees(1)  ->  1
count_trees(3)  ->  5
count_trees(0)  ->  1
```

Pick the root: `i` as root leaves `i - 1` values on the left and `n - i` on the right, and
the two sides are independent. Sum over roots. These are the Catalan numbers.

## Starter

```python
def count_trees(n):
    ...
```

## Hints

1. `count[0] = 1`. `count[k] = sum(count[i] * count[k - 1 - i] for i in range(k))`.
2. Build up from 0 to `n`.

## Approach

A one-dimensional DP where each entry combines all splits of the smaller entries. Quadratic in `n`.

## Reference

```python
def count_trees(n):
    count = [1] + [0] * n
    for k in range(1, n + 1):
        count[k] = sum(count[i] * count[k - 1 - i] for i in range(k))
    return count[n]
```
