# Do and undo

`actions` is a list of strings. `"undo"` cancels the most recent action
that has not already been undone; anything else is an action to do. Write
`final(actions)` that returns the list of actions still in effect, in order.
An `"undo"` with nothing to undo is ignored.

```static
final(["add bread", "add milk", "undo", "add eggs"])  ->  ["add bread", "add eggs"]
final(["undo", "add milk"])                           ->  ["add milk"]
```

## Starter

```python
def final(actions):
    ...
```

## Hints

1. A stack: push actions, pop on undo.
2. `if action == "undo": if stack: stack.pop()` else push.

## Approach

The stack is the answer itself once the loop finishes.

## Reference

```python
def final(actions):
    stack = []
    for action in actions:
        if action == "undo":
            if stack:
                stack.pop()
        else:
            stack.append(action)
    return stack
```
