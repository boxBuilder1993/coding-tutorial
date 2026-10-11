# Undo the last change

`history` is a list of changes, most recent last. Write `undo(history)` that
removes the most recent change and returns it. If there is nothing to undo,
return `None` and leave the list alone.

```static
undo(["add bread", "add milk"])  ->  "add milk"    (history is now ["add bread"])
undo([])                         ->  None
```

## Starter

```python
def undo(history):
    ...
```

## Hints

1. `pop()` removes and returns the last item, but fails on an empty list.
2. Check `if history:` first; return `None` when it is empty.

## Approach

Guard with an emptiness check, then `return history.pop()`.

## Reference

```python
def undo(history):
    if history:
        return history.pop()
    return None
```
