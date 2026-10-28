# Largest rectangle in a histogram

`heights` lists bar heights of width one. Write `largest_rectangle(heights)` that returns
the area of the largest rectangle that fits entirely inside the bars.

```static
largest_rectangle([2, 1, 5, 6, 2, 3])  ->  10     (5 and 6, height 5, width 2)
largest_rectangle([2, 4])              ->  4
largest_rectangle([])                  ->  0
```

A stack of indices with increasing heights. When a lower bar arrives, every taller bar
on the stack has found its right boundary; pop it and compute its rectangle, with the
left boundary being the new stack top. A sentinel of height 0 at the end flushes the stack.

## Starter

```python
def largest_rectangle(heights):
    ...
```

## Hints

1. Loop `i` over `range(len + 1)` with `h = heights[i]` or `0` at the end. While the stack is non-empty and `heights[stack[-1]] >= h`: pop `top`; width is `i` if the stack is empty else `i - stack[-1] - 1`; area is `heights[top] * width`.
2. Then push `i`.
3. Each index is pushed and popped once.

## Approach

Each bar is the shortest bar of exactly one maximal rectangle; the monotonic stack finds that rectangle's two boundaries in amortised constant time. Linear.

## Reference

```python
def largest_rectangle(heights):
    stack = []
    best = 0
    for i in range(len(heights) + 1):
        h = heights[i] if i < len(heights) else 0
        while stack and heights[stack[-1]] >= h:
            top = stack.pop()
            width = i if not stack else i - stack[-1] - 1
            best = max(best, heights[top] * width)
        stack.append(i)
    return best
```
