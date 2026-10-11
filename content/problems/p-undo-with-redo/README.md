# Undo and redo

`actions` is a list of strings: `"undo"` cancels the most recent action in
effect, `"redo"` restores the most recently undone action, and anything
else is a new action. A new action clears the redo history. Write
`final(actions)` that returns the actions in effect, in order. Undo or redo
with nothing to act on is ignored.

```static
final(["a", "b", "undo", "redo"])        ->  ["a", "b"]
final(["a", "b", "undo", "c", "redo"])   ->  ["a", "c"]
final(["undo", "redo", "a"])             ->  ["a"]
```

## Starter

```python
def final(actions):
    ...
```

## Hints

1. Two stacks: done and undone.
2. `undo` pops done and pushes undone; `redo` does the reverse; a new action pushes done and empties undone.

## Approach

Classic two-stack editor state. The "new action clears redo" rule is the detail most people miss.

## Reference

```python
def final(actions):
    done = []
    undone = []
    for action in actions:
        if action == "undo":
            if done:
                undone.append(done.pop())
        elif action == "redo":
            if undone:
                done.append(undone.pop())
        else:
            done.append(action)
            undone = []
    return done
```
