# Flatten a nested list

Write `flatten(items)` that takes a list whose elements are either values
or further lists, nested to any depth, and returns one flat list of all
the values in order.

```static
flatten(["apple", ["bread", ["jam"]], "milk"])  ->  ["apple", "bread", "jam", "milk"]
flatten([1, [2, [3, [4]]]])                     ->  [1, 2, 3, 4]
flatten([])                                     ->  []
```

The point is to practise recursion: a loop over the items, and a recursive
call for each item that is itself a list.

## Starter

```python
def flatten(items):
    ...
```

## Hints

1. `isinstance(item, list)` tells you whether to recurse.
2. Build a result list. For a plain value, `append` it. For a list, `extend` the result with `flatten` of it.
3. The base case is any item that is not a list: it contributes itself and no further call.

## Approach

Loop over `items`. If an item is a list, the flattened version of it goes into the result via `extend`; otherwise the item itself goes in via `append`. Nested lists of any depth work because each level hands the next level down.

## Reference

```python
def flatten(items):
    result = []
    for item in items:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
```
