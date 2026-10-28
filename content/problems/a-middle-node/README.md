# Middle node

Write `middle(head)` that returns the middle node of a linked list. When
the list has an even number of nodes, return the second of the two middle
nodes. The list has at least one node.

```static
middle(1 -> 2 -> 3 -> 4 -> 5)  ->  the node 3    (shown as 3 -> 4 -> 5)
middle(1 -> 2 -> 3 -> 4)       ->  the node 3    (shown as 3 -> 4)
```

The point is to practise fast and slow pointers, so find it in one pass
without counting the length first.

## Starter

```python
def middle(head):
    ...
```

## Hints

1. `slow = fast = head`.
2. While `fast is not None and fast.next is not None`: `slow = slow.next`, `fast = fast.next.next`.
3. Return `slow`.

## Approach

The fast reference moves two nodes per turn and the slow one moves one, so when fast runs out, slow has covered half the list. The loop condition guards against stepping off the end on both odd and even lengths.

## Reference

```python
def middle(head):
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow
```
