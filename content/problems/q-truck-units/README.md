# Load the truck

`boxes` is a list of `(count, units_per_box)` and the truck holds at most `capacity` boxes.
Write `max_units(boxes, capacity)` that returns the most units you can load.

```static
max_units([(1, 3), (2, 2), (3, 1)], 4)  ->  8     (1x3 + 2x2 + 1x1)
max_units([(5, 10)], 2)                 ->  20
```

The point is to practise the simplest greedy: sort by value and take as much as fits.

## Starter

```python
def max_units(boxes, capacity):
    ...
```

## Hints

1. Sort by units per box descending.
2. Take `min(count, capacity)` boxes of each type, reduce capacity, stop when it hits zero.

## Approach

Boxes all take the same space, so the most valuable ones first is optimal. Sort then one pass.

## Reference

```python
def max_units(boxes, capacity):
    total = 0
    for count, units in sorted(boxes, key=lambda b: -b[1]):
        take = min(count, capacity)
        total += take * units
        capacity -= take
        if capacity == 0:
            break
    return total
```
