# Rotate a linked list

Write `rotate_right(head, k)` that moves the last `k` nodes to the front, returning the
new head. `k` may be larger than the length, in which case it wraps around.

```static
rotate_right(1 -> 2 -> 3 -> 4 -> 5, 2)  ->  4 -> 5 -> 1 -> 2 -> 3
rotate_right(1 -> 2, 3)                 ->  2 -> 1
rotate_right(None, 4)                   ->  None
```

The point is to practise finding a split point and relinking the ends.

## Starter

```python
def rotate_right(head, k):
    ...
```

## Hints

1. Count the length and find the tail. Reduce `k` with `k % length`; if it is 0, return `head`.
2. The new tail is the node at position `length - k - 1` from the start. The new head is its `next`. Point the old tail at the old head and cut after the new tail.

## Approach

Three steps: measure, locate the new tail, and swap two links. Linear.

## Reference

```python
def rotate_right(head, k):
    if head is None:
        return None
    length = 1
    tail = head
    while tail.next is not None:
        tail = tail.next
        length += 1
    k %= length
    if k == 0:
        return head
    new_tail = head
    for _ in range(length - k - 1):
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None
    tail.next = head
    return new_head
```
