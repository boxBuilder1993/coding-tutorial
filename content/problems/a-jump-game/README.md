# Can you reach the end?

`jumps` is a list where each value is the furthest you can jump forward
from that position. You start at index 0. Write `can_reach_end(jumps)`
that returns whether the last index can be reached. A list of one item
counts as reached.

```static
can_reach_end([2, 3, 1, 1, 4])  ->  True
can_reach_end([3, 2, 1, 0, 4])  ->  False
can_reach_end([0])              ->  True
```

The point is to practise a greedy pass that tracks one summary value, the
furthest reachable position.

## Starter

```python
def can_reach_end(jumps):
    ...
```

## Hints

1. `furthest = 0`. For each index `i`, if `i > furthest` you are stuck: return `False`.
2. Otherwise `furthest = max(furthest, i + jumps[i])`.
3. If the loop finishes, return `True`.

## Approach

Walk left to right. The only fact about the past that matters is how far it lets you reach; if the current index is beyond that, nothing can get you there. Linear.

## Reference

```python
def can_reach_end(jumps):
    furthest = 0
    for i, jump in enumerate(jumps):
        if i > furthest:
            return False
        furthest = max(furthest, i + jump)
    return True
```
