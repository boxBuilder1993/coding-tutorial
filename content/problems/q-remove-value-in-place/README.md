# Remove a value in place

Write `remove_value(items, target)` that moves every item that is not `target` to the
front of the list, keeping their order, and returns how many there are. What is left in
the list after that count does not matter. Change the list you are given.

```static
items = [3, 2, 2, 3];  k = remove_value(items, 3)  ->  k == 2 and items[:2] == [2, 2]
items = [0, 1, 2, 2, 3, 0, 4, 2];  k = remove_value(items, 2)  ->  k == 5 and items[:5] == [0, 1, 3, 0, 4]
```

The point is to practise slow and fast pointers writing in place.

## Starter

```python
def remove_value(items, target):
    ...
```

## Hints

1. `slow = 0`. For each `item` in the list (the fast pointer), if it is not the target, write it at `items[slow]` and `slow += 1`.
2. Return `slow`.

## Approach

The slow pointer marks where the next kept item goes; the fast pointer scans. Everything before `slow` is the answer. Linear, no extra list.

## Reference

```python
def remove_value(items, target):
    slow = 0
    for item in items:
        if item != target:
            items[slow] = item
            slow += 1
    return slow
```
