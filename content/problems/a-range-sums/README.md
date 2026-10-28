# Range sums

Write `range_sums(items, queries)` where `queries` is a list of `(i, j)`
pairs with `i <= j`. Return a list with, for each query, the sum of
`items[i]` through `items[j]` inclusive.

```static
range_sums([3, 1, 4, 1, 5], [(0, 2), (1, 3), (4, 4)])  ->  [8, 6, 5]
range_sums([3, 1, 4, 1, 5], [])                        ->  []
```

The point is to practise prefix sums. One check has a hundred thousand
items and a hundred thousand queries; summing each range directly is
billions of steps and will not finish in time.

## Starter

```python
def range_sums(items, queries):
    ...
```

## Hints

1. Build `prefix` with `prefix[0] = 0` and `prefix[k]` the sum of the first `k` items. One loop.
2. The sum of `items[i..j]` is `prefix[j + 1] - prefix[i]`.
3. Answer each query with that subtraction and collect the results in a list.

## Approach

One linear pass to build the running totals, then one constant-time subtraction per query. The extra leading zero in `prefix` means a query starting at index 0 needs no special case.

## Reference

```python
def range_sums(items, queries):
    prefix = [0]
    for x in items:
        prefix.append(prefix[-1] + x)
    return [prefix[j + 1] - prefix[i] for i, j in queries]
```
