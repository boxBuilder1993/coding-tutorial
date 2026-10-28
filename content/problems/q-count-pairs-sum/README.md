# Count pairs with a sum

Write `count_pairs(nums, target)` that returns how many pairs of positions `i < j` have
`nums[i] + nums[j] == target`. Repeated values make separate pairs.

```static
count_pairs([1, 5, 7, -1, 5], 6)  ->  3     (1,5) (7,-1) (1,5)
count_pairs([1, 1, 1, 1], 2)      ->  6
```

The point is to practise counting complements with a dictionary as you go. One check
has a hundred thousand numbers.

## Starter

```python
def count_pairs(nums, target):
    ...
```

## Hints

1. Walk the list keeping a `Counter` of values seen so far.
2. For each `x`, add `seen[target - x]` to the answer, then record `x`. Counting before recording means `x` never pairs with itself.

## Approach

Each number pairs with every earlier occurrence of its complement, and the counter of earlier values gives that number in one lookup. Linear.

## Reference

```python
from collections import Counter

def count_pairs(nums, target):
    seen = Counter()
    total = 0
    for x in nums:
        total += seen[target - x]
        seen[x] += 1
    return total
```
