# Add two numbers stored in reverse

Two non-negative numbers are stored as linked lists of digits, least significant digit
first: `342` is `2 -> 4 -> 3`. Write `add(a, b)` that returns their sum as a new linked
list in the same form.

```static
add(2 -> 4 -> 3, 5 -> 6 -> 4)  ->  7 -> 0 -> 8       (342 + 465 = 807)
add(9 -> 9, 1)                 ->  0 -> 0 -> 1       (99 + 1 = 100)
```

The point is to practise walking two lists together with a carry, and building the
result with a tail pointer.

## Starter

```python
def add(a, b):
    ...
```

## Hints

1. Loop while either list has nodes or `carry` is non-zero. Take each list's digit as 0 when it has run out.
2. `total = x + y + carry`; append `total % 10`; `carry = total // 10`.
3. Build onto a dummy head with a tail reference.

## Approach

Column addition from the right, which is the order the lists already store. Linear in the longer list.

## Reference

```python
from checker import ListNode

def add(a, b):
    dummy = ListNode()
    tail = dummy
    carry = 0
    while a is not None or b is not None or carry:
        x = a.val if a is not None else 0
        y = b.val if b is not None else 0
        total = x + y + carry
        tail.next = ListNode(total % 10)
        tail = tail.next
        carry = total // 10
        a = a.next if a is not None else None
        b = b.next if b is not None else None
    return dummy.next
```
