# All permutations

Write `permutations(items)` that returns every ordering of the list of
distinct values, as a list of lists. Order of the results does not matter.

```static
permutations([1, 2, 3])  ->  [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
permutations([])         ->  [[]]
```

The point is to practise backtracking with a `used` marker that is undone
after each recursive call.

## Starter

```python
def permutations(items):
    ...
```

## Hints

1. When `partial` is as long as `items`, record a copy.
2. Otherwise for each index not yet used: mark it used, append, recurse, pop, unmark.
3. Check: `n` items give `n!` permutations, so 4 items give 24.

## Approach

Fill one slot at a time from the unused items. Both the partial list and the used markers are restored after the recursive call so the next choice starts clean.

## Reference

```python
def permutations(items):
    out = []
    partial = []
    used = [False] * len(items)

    def go():
        if len(partial) == len(items):
            out.append(partial[:])
            return
        for i in range(len(items)):
            if used[i]:
                continue
            used[i] = True
            partial.append(items[i])
            go()
            partial.pop()
            used[i] = False

    go()
    return out
```
