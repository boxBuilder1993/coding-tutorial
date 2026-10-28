# Flood fill

`image` is a list of lists of whole numbers (colours). Write `flood_fill(image, r, c, colour)`
that changes the cell at `(r, c)` and every cell connected to it (up, down, left, right)
through cells of the same original colour to the new `colour`, in place, and returns
`image`.

```static
flood_fill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2)  ->  [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
flood_fill([[0, 0]], 0, 0, 0)                          ->  [[0, 0]]   (same colour: nothing changes)
```

The point is to practise a search on a grid that stops at a colour boundary. Watch the
case where the new colour equals the old one, which loops forever if handled naively.

## Starter

```python
def flood_fill(image, r, c, colour):
    ...
```

## Hints

1. Remember `old = image[r][c]`. If `old == colour`, return immediately.
2. Stack or recursion from `(r, c)`: for an in-bounds cell with `image[x][y] == old`, set it to `colour` and push its four neighbours.

## Approach

Connected component on the grid, bounded by the original colour. Painting a cell as you visit it marks it visited. Linear in cells.

## Reference

```python
def flood_fill(image, r, c, colour):
    old = image[r][c]
    if old == colour:
        return image
    rows, cols = len(image), len(image[0])
    stack = [(r, c)]
    while stack:
        x, y = stack.pop()
        if 0 <= x < rows and 0 <= y < cols and image[x][y] == old:
            image[x][y] = colour
            stack.extend([(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)])
    return image
```
