# Trapped rainwater

`heights` describes a row of walls. After rain, water sits wherever a lower wall has
higher walls somewhere on both sides. Write `trapped(heights)` that returns the total
units of water held.

```static
trapped([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])  ->  6
trapped([4, 2, 0, 3, 2, 5])                     ->  9
trapped([1, 2, 3])                              ->  0
```

The point is to practise two pointers where you can safely settle the lower side: the
water above a position is bounded by the smaller of the tallest walls to its left and right.

## Starter

```python
def trapped(heights):
    ...
```

## Hints

1. Pointers at both ends with `left_max` and `right_max`. Whichever side's max is smaller is the side you can settle: water there is `that_max - height`.
2. Move that pointer inwards, updating its max. Repeat until they meet.

## Approach

The water at a position is limited by the lower of the two surrounding maxima. Processing the side with the smaller max guarantees the other side's max is at least as large, so the answer for that position is final. Linear.

## Reference

```python
def trapped(heights):
    left, right = 0, len(heights) - 1
    left_max = right_max = 0
    water = 0
    while left < right:
        if heights[left] < heights[right]:
            left_max = max(left_max, heights[left])
            water += left_max - heights[left]
            left += 1
        else:
            right_max = max(right_max, heights[right])
            water += right_max - heights[right]
            right -= 1
    return water
```
