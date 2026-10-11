# Balanced brackets, two kinds

Write `balanced(text)` that returns `True` if every `(` and `[` is closed
by the matching `)` or `]` in the right order, and no closer appears
without an opener before it. Other characters are ignored.

```static
balanced("([])")   ->  True
balanced("([)]")   ->  False
balanced("((")     ->  False
balanced("())")    ->  False
```

## Starter

```python
def balanced(text):
    ...
```

## Hints

1. A stack of openers, and a dictionary mapping each closer to its opener.
2. On a closer: fail if the stack is empty or `stack.pop()` is not the matching opener.

## Approach

Push every opener. On a closer, pop and compare with the opener it needs; an empty stack or a mismatch means unbalanced. Balanced only if the stack is empty at the end.

## Reference

```python
def balanced(text):
    pairs = {")": "(", "]": "["}
    stack = []
    for ch in text:
        if ch in "([":
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
    return len(stack) == 0
```
