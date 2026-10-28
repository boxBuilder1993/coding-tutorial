# Common items

Write `common_items(a, b)` that returns the values that appear in both
lists, each once, in the order they first appear in `a`.

```static
common_items([3, 1, 4, 1, 5], [5, 1, 9])  ->  [1, 5]
common_items([1, 2], [3])                 ->  []
```

The point is to practise using a set for membership. One check uses two
lists of a hundred thousand items each; `x in b` on a list inside a loop
over `a` is ten billion steps and will not finish in time.

## Starter

```python
def common_items(a, b):
    ...
```

## Hints

1. `in_b = set(b)` once, before the loop.
2. Walk `a`; if an item is in `in_b` and you have not already added it, append it. A second set tracks what has been added.

## Approach

Convert `b` to a set so each membership test is one step. Loop over `a` once, keeping a `seen` set to avoid repeats and appending items that are in both. Linear in the two lengths.

## Reference

```python
def common_items(a, b):
    in_b = set(b)
    seen = set()
    out = []
    for x in a:
        if x in in_b and x not in seen:
            seen.add(x)
            out.append(x)
    return out
```
