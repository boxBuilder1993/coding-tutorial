# Balanced parentheses

Write `balanced(text)` that returns `True` if every `(` in `text` is closed
by a later `)` in the right order, and `False` otherwise. Only round
brackets count; every other character, including `[` and `{`, is ignored.

```static
balanced("(a + b) * (c)")  ->  True
balanced("(()")            ->  False
balanced("())(")           ->  False
balanced("")               ->  True
```

## Starter

```python
def balanced(text):
    stack = []
    for ch in text:
        ...
    return ...
```

## Hints

1. Push on `(`. On `)`, if the stack is empty the text is already unbalanced, so return `False`; otherwise pop.
2. After the loop, the text is balanced only if the stack is empty: `return len(stack) == 0`.

## Approach

Two ways to fail: a `)` with nothing to match, caught inside the loop, and leftover `(` at the end, caught after it.

## Reference

```python
def balanced(text):
    stack = []
    for ch in text:
        if ch == "(":
            stack.append(ch)
        elif ch == ")":
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0
```
