# A queue made of two stacks

A queue serves the oldest item first; a stack gives the newest. You can
build a queue out of two stacks. Call them `inbox` and `outbox`. To add an
item, push it onto `inbox`. To take the oldest item: if `outbox` is empty,
pop every item from `inbox` and push each onto `outbox`, which reverses
their order so the oldest is now on top; then pop from `outbox`. If
`outbox` already has items, just pop from it.

Write `drain(operations)` that starts with two empty stacks (plain lists),
applies a list of operations, and returns the list of items taken out, in
order. Each operation is `("add", item)` or `("take",)`. A take on an empty
queue is ignored. Do not use `pop(0)` or a `deque`: the point is the two
stacks.

```static
drain([("add", "a"), ("add", "b"), ("take",), ("add", "c"), ("take",), ("take",)])  ->  ["a", "b", "c"]
```

## Starter

```python
def drain(operations):
    ...
```

## Hints

1. Two lists. `add` is `inbox.append`. `take` moves everything across only when `outbox` is empty.
2. Moving across: `while inbox: outbox.append(inbox.pop())`. Then `outbox.pop()` if it has anything.

## Approach

Items wait in `inbox` in arrival order and get reversed into `outbox` only when it runs dry, so the oldest surfaces on top. Moving across only when empty keeps the order right across interleaved adds and takes.

## Reference

```python
def drain(operations):
    inbox = []
    outbox = []
    taken = []
    for op in operations:
        if op[0] == "add":
            inbox.append(op[1])
        else:
            if not outbox:
                while inbox:
                    outbox.append(inbox.pop())
            if outbox:
                taken.append(outbox.pop())
    return taken
```
