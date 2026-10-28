# Does the list loop?

A linked list may have a cycle: some node's `next` points back to an earlier node, so
walking it never ends. Write `has_cycle(head)` that returns whether it does, without
using extra memory proportional to the length.

```static
has_cycle(1 -> 2 -> 3 -> back to 2)  ->  True
has_cycle(1 -> 2 -> 3)               ->  False
```

The point is to practise fast and slow pointers: in a cycle, the fast one laps the slow one.

## Starter

```python
def has_cycle(head):
    ...
```

## Hints

1. `slow = fast = head`. Each turn, slow moves one and fast moves two.
2. If `fast` or `fast.next` becomes `None`, there is no cycle. If `slow is fast` after moving, there is.

## Approach

Without a cycle the fast pointer reaches the end. With one, both end up inside the loop and the fast pointer gains one step per turn until they coincide. Linear time, constant space. A set of seen nodes also works but uses linear memory.

## Reference

```python
def has_cycle(head):
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
```
