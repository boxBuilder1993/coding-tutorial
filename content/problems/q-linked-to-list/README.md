# Read a linked list into a Python list

Write `values(head)` that returns the values of the linked list starting at `head` as a
Python list, in order. `head` is a `ListNode` or `None`.

```static
values(1 -> 2 -> 3)  ->  [1, 2, 3]
values(None)         ->  []
```

The point is to practise the walk. The checker has a helper that does this; write your own.

## Starter

```python
def values(head):
    ...
```

## Hints

1. Start with an empty list and `current = head`.
2. While `current is not None`: append `current.val`, move to `current.next`.

## Approach

The standard walk collecting values. Linear.

## Reference

```python
def values(head):
    out = []
    current = head
    while current is not None:
        out.append(current.val)
        current = current.next
    return out
```
