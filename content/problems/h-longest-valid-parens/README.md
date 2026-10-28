# Longest balanced bracket stretch

Write `longest_valid(text)` that returns the length of the longest stretch of `text`,
made only of `(` and `)`, that is a correctly balanced bracket string.

```static
longest_valid("(()")      ->  2
longest_valid(")()())")   ->  4
longest_valid("")         ->  0
```

A stack of indices with a sentinel: push on `(`, pop on `)`, and the length of the
current valid stretch is the distance from the current index to the top of the stack.

## Starter

```python
def longest_valid(text):
    ...
```

## Hints

1. `stack = [-1]`. On `(` push the index. On `)` pop; if the stack is now empty push the current index as the new base, else record `i - stack[-1]`.
2. The base index marks the last unmatched `)` or the start; everything after it up to `i` is balanced.

## Approach

Indices on a stack let each `)` compute how far back the balanced stretch reaches in one step. Linear.

## Reference

```python
def longest_valid(text):
    stack = [-1]
    best = 0
    for i, ch in enumerate(text):
        if ch == "(":
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                best = max(best, i - stack[-1])
    return best
```
