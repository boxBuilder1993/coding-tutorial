# n-th node from the end

Write `nth_from_end(head, n)` that returns the value of the `n`-th node counting from
the end, where `n = 1` is the last node. `n` is at most the length.

```static
nth_from_end(1 -> 2 -> 3 -> 4 -> 5, 2)  ->  4
nth_from_end(1 -> 2 -> 3 -> 4 -> 5, 5)  ->  1
```

The point is to practise two pointers a fixed distance apart, in one pass.

## Starter

```python
def nth_from_end(head, n):
    ...
```

## Hints

1. Move a `lead` pointer `n` steps ahead of a `trail` pointer, both starting at `head`.
2. Advance both until `lead` is `None`; `trail` is then on the answer.

## Approach

Keeping the two pointers `n` apart means when the leader falls off the end the trailer is `n` from the end. Linear, one pass, no length count.

## Reference

```python
def nth_from_end(head, n):
    lead = trail = head
    for _ in range(n):
        lead = lead.next
    while lead is not None:
        lead = lead.next
        trail = trail.next
    return trail.val
```
