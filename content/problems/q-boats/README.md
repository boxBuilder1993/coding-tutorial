# Boats to carry everyone

`weights` lists people's weights; each boat carries at most two people and at most `limit`
total weight, and nobody weighs more than `limit`. Write `boats(weights, limit)` that
returns the fewest boats.

```static
boats([1, 2], 3)        ->  1
boats([3, 2, 2, 1], 3)  ->  3
boats([3, 5, 3, 4], 5)  ->  4
```

The point is to practise the pairing greedy: the heaviest person goes with the lightest
if they fit, otherwise alone.

## Starter

```python
def boats(weights, limit):
    ...
```

## Hints

1. Sort. Two pointers, lightest and heaviest.
2. Each boat takes the heaviest; if the lightest also fits, take them too. Count boats until the pointers cross.

## Approach

The heaviest person must take a boat; pairing them with the lightest is never worse than any other pairing. Sort plus one pass.

## Reference

```python
def boats(weights, limit):
    people = sorted(weights)
    left, right = 0, len(people) - 1
    count = 0
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        count += 1
    return count
```
