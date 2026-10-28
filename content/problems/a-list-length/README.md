# Length of a linked list

Write `length(head)` that returns how many nodes are in the linked list
starting at `head`. `head` is a `ListNode` with fields `val` and `next`,
or `None` for an empty list.

```static
length(1 -> 2 -> 3)  ->  3
length(None)         ->  0
```

The point is to practise walking a linked list with a `while` loop.

## Starter

```python
def length(head):
    ...
```

## Hints

1. `count = 0`, `current = head`, and loop `while current is not None`.
2. Each turn: `count += 1` and `current = current.next`.

## Approach

The standard walk: move a reference along `next` until it is `None`, counting as you go. Linear in the length.

## Reference

```python
def length(head):
    count = 0
    current = head
    while current is not None:
        count += 1
        current = current.next
    return count
```
