# Every other item

Write `every_other(items)` that returns a new list with the first item, the
third, the fifth, and so on.

```static
every_other(["a", "b", "c", "d", "e"])  ->  ["a", "c", "e"]
every_other([])                         ->  []
```

## Starter

```python
def every_other(items):
    ...
```

## Hints

1. A slice with a step.
2. `items[::2]`

## Approach

The third slice number is the step.

## Reference

```python
def every_other(items):
    return items[::2]
```
