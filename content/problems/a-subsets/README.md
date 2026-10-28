# All subsets

Write `subsets(items)` that returns every subset of the list of distinct
values, as a list of lists. The empty subset counts. Order does not matter.

```static
subsets([1, 2])     ->  [[], [1], [2], [1, 2]]    (in any order)
subsets([])         ->  [[]]
```

The point is to practise the include-or-exclude recursion with a shared
partial list that is copied when recorded.

## Starter

```python
def subsets(items):
    ...
```

## Hints

1. An inner function `go(i)`: when `i == len(items)`, record `partial[:]`.
2. Otherwise call `go(i + 1)` once without `items[i]`, then append `items[i]`, call `go(i + 1)` again, and pop.
3. Check: a list of `n` items should produce `2 ** n` subsets.

## Approach

Each item is either in or out, decided one at a time. The copy on record matters: the same `partial` list is reused for every branch.

## Reference

```python
def subsets(items):
    out = []
    partial = []

    def go(i):
        if i == len(items):
            out.append(partial[:])
            return
        go(i + 1)
        partial.append(items[i])
        go(i + 1)
        partial.pop()

    go(0)
    return out
```
