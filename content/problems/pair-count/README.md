# Count the pairs

Write `pair_count(n)` that returns how many times the inner line runs in
this loop, for a list of `n` items:

```static
for i in range(n):
    for j in range(i + 1, n):
        compare(items[i], items[j])     # this line
```

That is the number of distinct pairs among `n` items. You can count with
loops or find the formula; both are fine. The point is to see how the
number grows.

```static
pair_count(4)    ->  6
pair_count(100)  ->  4950
```

## Starter

```python
def pair_count(n):
    ...
```

## Hints

1. Copy the loop shape and add a counter instead of comparing anything.
2. The inner loop runs `n - 1` times, then `n - 2`, down to `0`. That adds up to `n × (n - 1) / 2`.

## Approach

Either run the two loops with a counter, or return `n * (n - 1) // 2`. Use `//` so the result is an integer.

## Reference

```python
def pair_count(n):
    return n * (n - 1) // 2
```
