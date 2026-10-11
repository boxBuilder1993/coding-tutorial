# Top of the stack

Write `push_and_peek(stack, item)` that pushes `item` onto the stack (a
list) and returns whatever is now on top.

```static
push_and_peek(["a", "b"], "c")  ->  "c"
```

## Starter

```python
def push_and_peek(stack, item):
    ...
```

## Hints

1. `append`, then look at the last position.
2. `stack.append(item)` then `return stack[-1]`

## Approach

Push, then peek with `[-1]`. Returning `item` directly would also be correct but misses the point.

## Reference

```python
def push_and_peek(stack, item):
    stack.append(item)
    return stack[-1]
```
