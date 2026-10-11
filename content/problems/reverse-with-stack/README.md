# Reverse with a stack

Write `reverse_items(items)` that returns a new list with the items in
reverse order, by pushing every item onto a stack and then popping them all
off. Do not use slicing or `reverse` for this one; the point is the stack.

```static
reverse_items(["apple", "bread", "milk"])  ->  ["milk", "bread", "apple"]
reverse_items([])                          ->  []
```

## Starter

```python
def reverse_items(items):
    stack = []
    for item in items:
        ...
    result = []
    while stack:
        ...
    return result
```

## Hints

1. First loop: `stack.append(item)`.
2. Second loop: `result.append(stack.pop())`.

## Approach

Push everything, then pop until empty. The pops come out in the opposite order to the pushes.

## Reference

```python
def reverse_items(items):
    stack = []
    for item in items:
        stack.append(item)
    result = []
    while stack:
        result.append(stack.pop())
    return result
```
