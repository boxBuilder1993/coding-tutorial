# Most water between two walls

`heights` lists the heights of vertical walls at positions 0, 1, 2, and so
on. Pick two walls; the water they could hold between them is the distance
between them times the shorter wall's height. Find the most water any pair
can hold. Start with the two outermost walls. The only way a narrower pair
could hold more is if it is taller, and the shorter wall is the limit, so
move the shorter wall's position inward and try again. Stop when the
positions meet.

Write `most_water(heights)` for a list with at least two walls.

```static
most_water([1, 8, 6, 2, 5, 4, 8, 3, 7])  ->  49
most_water([1, 1])                       ->  1
```

## Starter

```python
def most_water(heights):
    ...
```

## Hints

1. `left, right = 0, len(heights) - 1`; area is `(right - left) * min(heights[left], heights[right])`.
2. Move whichever side is shorter: `if heights[left] < heights[right]: left += 1 else: right -= 1`.

## Approach

Moving the taller side can never help, because the width shrinks and the height is still capped by the shorter one. Nested loops over all pairs also pass.

## Reference

```python
def most_water(heights):
    left = 0
    right = len(heights) - 1
    best = 0
    while left < right:
        area = (right - left) * min(heights[left], heights[right])
        best = max(best, area)
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return best
```
