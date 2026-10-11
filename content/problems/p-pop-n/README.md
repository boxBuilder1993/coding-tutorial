# Pop several

Write `pop_n(stack, n)` that pops up to `n` items off a stack (a list) and
returns them as a list in the order they were popped. Stop early if the
stack runs out.

```static
pop_n(["a", "b", "c"], 2)  ->  ["c", "b"]     (stack is now ["a"])
pop_n(["a"], 3)            ->  ["a"]
```

## Starter

```python
def pop_n(stack, n):
    ...
```

## Hints

1. A loop that stops on either the count or an empty stack.
2. `while n > 0 and stack:` then `popped.append(stack.pop())`.

## Approach

Two stopping conditions in one `while`. Popping an empty list raises, so the `and stack` matters.

## Reference

```python
def pop_n(stack, n):
    popped = []
    while n > 0 and stack:
        popped.append(stack.pop())
        n -= 1
    return popped
```
