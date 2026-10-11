# Names by priority

`orders` is a list of `(priority, name)` tuples with distinct priorities.
Write `names_by_priority(orders)` that returns the names ordered from
lowest priority number to highest, using `sorted`.

```static
names_by_priority([(3, "bread"), (1, "cake"), (2, "rolls")])  ->  ["cake", "rolls", "bread"]
```

## Starter

```python
def names_by_priority(orders):
    ...
```

## Hints

1. `sorted` on tuples orders by the first value; then pull out the names.
2. `for priority, name in sorted(orders): names.append(name)`

## Approach

Tuples sort by their first element, so plain `sorted` gives priority order. Then collect the second elements.

## Reference

```python
def names_by_priority(orders):
    names = []
    for priority, name in sorted(orders):
        names.append(name)
    return names
```
