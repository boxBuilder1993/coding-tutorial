# Range sums with a prefix table

Many questions of the form "what is the total of items `i` to `j`" can be
answered from one precomputed table. Build `prefix` where `prefix[0]` is 0
and `prefix[i]` is the sum of the first `i` items. Then the sum of items
from position `i` up to and including `j` is `prefix[j + 1] - prefix[i]`.

Write `range_sums(nums, queries)` where each query is a tuple `(i, j)`.
Return the list of answers. Build the prefix table once; do not re-add the
items for every query.

```static
range_sums([2, 4, 6, 8], [(0, 1), (1, 3), (2, 2)])  ->  [6, 18, 6]
```

## Starter

```python
def range_sums(nums, queries):
    ...
```

## Hints

1. `prefix = [0]`; for each item, `prefix.append(prefix[-1] + x)`.
2. Each answer is `prefix[j + 1] - prefix[i]`.

## Approach

The table has one extra entry at the front so the formula needs no special case for `i == 0`.

## Reference

```python
def range_sums(nums, queries):
    prefix = [0]
    for x in nums:
        prefix.append(prefix[-1] + x)
    return [prefix[j + 1] - prefix[i] for i, j in queries]
```
