# Clamp a quantity

Orders must be for at least 1 and at most 20 of an item. Write
`clamp_quantity(q)` that returns `q` unchanged if it is already in range,
`1` if it is below, and `20` if it is above.

```static
clamp_quantity(7)   ->  7
clamp_quantity(0)   ->  1
clamp_quantity(99)  ->  20
```

## Starter

```python
def clamp_quantity(q):
    ...
```

## Hints

1. Two `if` checks, one for each limit, each returning the limit.
2. If neither fires, return `q` as it is.

## Approach

```python
if q < 1: return 1
if q > 20: return 20
return q
```

Python also has `min` and `max`: `max(1, min(q, 20))` does the same in one line.

## Reference

```python
def clamp_quantity(q):
    if q < 1:
        return 1
    if q > 20:
        return 20
    return q
```
