# Distinct orderings with repeats

Write `unique_permutations(items)` that returns every distinct ordering of a list that
may contain repeated values. Order of the output does not matter.

```static
unique_permutations([1, 1, 2])  ->  [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
unique_permutations([])         ->  [[]]
```

The point is to practise the duplicate-skip rule in the permutation template: at each
slot, do not place a value equal to one you already tried in that slot.

## Starter

```python
def unique_permutations(items):
    ...
```

## Hints

1. Sort. In the loop over candidates for the next slot, skip `i` if `used[i]`, or if `i > 0 and items[i] == items[i - 1] and not used[i - 1]`.
2. That second rule means: use equal values in left-to-right order only.

## Approach

Sorting plus the rule that an equal value may only be placed after its left twin has been placed gives each distinct ordering exactly once.

## Reference

```python
def unique_permutations(items):
    items = sorted(items)
    out = []
    partial = []
    used = [False] * len(items)

    def go():
        if len(partial) == len(items):
            out.append(partial[:])
            return
        for i in range(len(items)):
            if used[i] or (i > 0 and items[i] == items[i - 1] and not used[i - 1]):
                continue
            used[i] = True
            partial.append(items[i])
            go()
            partial.pop()
            used[i] = False

    go()
    return out
```
