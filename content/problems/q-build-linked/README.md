# Build a linked list

Write `build(items)` that creates a linked list of `ListNode`s holding the values of
`items` in order and returns its head, or `None` for an empty list. Import `ListNode`
from `checker`.

```static
build([1, 2, 3])  ->  1 -> 2 -> 3
build([])         ->  None
```

The point is to practise creating and linking nodes with a tail reference, or with a dummy head.

## Starter

```python
def build(items):
    ...
```

## Hints

1. `from checker import ListNode`. Make a dummy node and a `tail` pointing at it.
2. For each value: `tail.next = ListNode(value)`, then `tail = tail.next`. Return `dummy.next`.

## Approach

Appending at a remembered tail is constant time per node. The dummy avoids a special case for the first node.

## Reference

```python
from checker import ListNode

def build(items):
    dummy = ListNode()
    tail = dummy
    for v in items:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next
```
