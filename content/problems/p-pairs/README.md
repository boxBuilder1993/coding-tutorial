# Pair them up

Write `pairs(items)` that groups a list with an even number of items into
consecutive pairs, as a list of tuples.

```static
pairs(["a", "b", "c", "d"])  ->  [("a", "b"), ("c", "d")]
pairs([])                    ->  []
```

## Starter

```python
def pairs(items):
    ...
```

## Hints

1. `range` with a step of 2, then index `i` and `i + 1`.
2. `for i in range(0, len(items), 2):` append `(items[i], items[i + 1])`.

## Approach

Step through the positions two at a time.

## Reference

```python
def pairs(items):
    result = []
    for i in range(0, len(items), 2):
        result.append((items[i], items[i + 1]))
    return result
```
