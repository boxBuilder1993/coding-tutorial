# A stack that knows its minimum

A normal stack can tell you its top instantly, but not its smallest item.
Keep a second stack alongside, holding the minimum so far: whenever you
push a value, also push the smaller of that value and the current minimum;
whenever you pop, pop both. The top of the second stack is always the
minimum of what is left.

Write `min_after(operations)` that applies a list of operations to an
empty stack and returns a list with the current minimum after **each**
operation, or `None` when the stack is empty. Operations are
`("push", value)` and `("pop",)`. A pop on an empty stack is ignored.

```static
min_after([("push", 5), ("push", 3), ("push", 7), ("pop",), ("pop",)])  ->  [5, 3, 3, 3, 5]
```

## Starter

```python
def min_after(operations):
    ...
```

## Hints

1. Two lists, `values` and `mins`, always the same length.
2. On push: `mins.append(min(value, mins[-1]) if mins else value)`. On pop: pop both. Record `mins[-1]` or `None`.

## Approach

The parallel stack records, for every position, the minimum of everything at or below it, so popping never requires searching.

## Reference

```python
def min_after(operations):
    values = []
    mins = []
    result = []
    for op in operations:
        if op[0] == "push":
            value = op[1]
            values.append(value)
            mins.append(min(value, mins[-1]) if mins else value)
        elif values:
            values.pop()
            mins.pop()
        result.append(mins[-1] if mins else None)
    return result
```
