# All positions of a value

Write `positions(items, value)` that returns a list of every index where
`value` appears in `items`.

```static
positions(["a", "b", "a", "c", "a"], "a")  ->  [0, 2, 4]
positions(["a"], "z")                      ->  []
```

## Starter

```python
def positions(items, value):
    ...
```

## Hints

1. `enumerate` gives index and item together.
2. `for i, item in enumerate(items): if item == value: result.append(i)`

## Approach

`index` only finds the first; `enumerate` with an `if` finds them all.

## Reference

```python
def positions(items, value):
    result = []
    for i, item in enumerate(items):
        if item == value:
            result.append(i)
    return result
```
