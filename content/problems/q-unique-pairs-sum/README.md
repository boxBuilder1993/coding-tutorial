# All distinct pairs with a sum

`items` is sorted and may contain repeats. Write `pairs_with_sum(items, target)` that
returns every distinct pair `[a, b]` with `a <= b` and `a + b == target`, in increasing
order of `a`. Each distinct pair appears once even if the values repeat.

```static
pairs_with_sum([1, 1, 2, 3, 3, 4, 5], 6)  ->  [[1, 5], [2, 4], [3, 3]]
pairs_with_sum([1, 2], 10)                ->  []
```

The point is to practise two pointers with a skip past repeated values after a match.

## Starter

```python
def pairs_with_sum(items, target):
    ...
```

## Hints

1. Standard inward two pointers. On a match, record the pair, then advance `left` past all copies of its value and `right` past all copies of its value.
2. `[3, 3]` needs `left < right` at the time of the match, which the loop condition already provides.

## Approach

Two pointers find each matching sum once in increasing order of the left value; skipping duplicates after a match prevents repeats. Linear.

## Reference

```python
def pairs_with_sum(items, target):
    out = []
    left, right = 0, len(items) - 1
    while left < right:
        total = items[left] + items[right]
        if total == target:
            out.append([items[left], items[right]])
            a, b = items[left], items[right]
            while left < right and items[left] == a:
                left += 1
            while left < right and items[right] == b:
                right -= 1
        elif total < target:
            left += 1
        else:
            right -= 1
    return out
```
