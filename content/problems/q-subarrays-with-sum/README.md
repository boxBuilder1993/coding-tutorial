# Count runs that sum to k

Write `count_runs(nums, k)` that returns how many runs of consecutive items (of length
at least one) sum to exactly `k`. Values may be negative.

```static
count_runs([1, 1, 1], 2)        ->  2
count_runs([1, 2, 3], 3)        ->  2     ([1, 2] and [3])
count_runs([1, -1, 1, -1], 0)   ->  4
```

The point is to practise prefix sums in a dictionary: a run ending here sums to `k` when
an earlier prefix equals the current prefix minus `k`. One check has a hundred thousand
items.

## Starter

```python
def count_runs(nums, k):
    ...
```

## Hints

1. Keep `prefix` (sum so far) and a `Counter` of prefix values seen, starting with `{0: 1}`.
2. For each item, update `prefix`, add `seen[prefix - k]` to the answer, then `seen[prefix] += 1`.

## Approach

Every run is the difference of two prefix sums. Counting earlier prefixes lets each position ask how many runs end here in one lookup. Linear.

## Reference

```python
from collections import Counter

def count_runs(nums, k):
    seen = Counter({0: 1})
    prefix = 0
    total = 0
    for x in nums:
        prefix += x
        total += seen[prefix - k]
        seen[prefix] += 1
    return total
```
