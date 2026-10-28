# Burst balloons

`nums` lists the numbers on a row of balloons. Bursting balloon `i` earns
`left * nums[i] * right` coins, where `left` and `right` are the nearest unburst neighbours
(treat the edges as 1), and then the row closes up. Write `max_coins(nums)` that returns
the most coins you can earn by bursting all of them.

```static
max_coins([3, 1, 5, 8])  ->  167
max_coins([1, 5])        ->  10
max_coins([])            ->  0
```

Think about the **last** balloon burst in a range: its neighbours are the range's fixed
borders. Interval DP over `(left border, right border)` with padding 1s at both ends.

## Starter

```python
def max_coins(nums):
    ...
```

## Hints

1. Pad: `vals = [1] + nums + [1]`. `best[i][j]` = most coins from bursting everything strictly between `i` and `j`.
2. `best[i][j] = max over k in (i, j) of vals[i] * vals[k] * vals[j] + best[i][k] + best[k][j]`, where `k` is the last balloon burst in that range.
3. Fill by increasing gap `j - i`. Answer `best[0][len(vals) - 1]`.

## Approach

Choosing the last balloon in a range makes both sub-ranges independent, which is what the naive 'first balloon' choice does not do. Cubic, fine for a few dozen balloons.

## Reference

```python
def max_coins(nums):
    vals = [1] + list(nums) + [1]
    n = len(vals)
    best = [[0] * n for _ in range(n)]
    for gap in range(2, n):
        for i in range(n - gap):
            j = i + gap
            best[i][j] = max(vals[i] * vals[k] * vals[j] + best[i][k] + best[k][j] for k in range(i + 1, j))
    return best[0][n - 1]
```
