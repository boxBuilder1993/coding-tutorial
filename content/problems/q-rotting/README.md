# How long until everything rots?

`grid` is a list of lists where `0` is empty, `1` is a fresh orange and `2` is a rotten
one. Every minute, each rotten orange rots the fresh oranges directly up, down, left and
right of it. Write `minutes_to_rot(grid)` that returns how many minutes until no fresh
orange remains, or `-1` if some fresh orange can never be reached.

```static
minutes_to_rot([[2, 1, 1], [1, 1, 0], [0, 1, 1]])  ->  4
minutes_to_rot([[2, 1, 1], [0, 1, 1], [1, 0, 1]])  ->  -1
minutes_to_rot([[0, 2]])                           ->  0
```

The point is to practise BFS from many sources at once: every rotten orange starts in the
queue with time 0.

## Starter

```python
def minutes_to_rot(grid):
    ...
```

## Hints

1. Queue all rotten cells first with minute 0, and count the fresh ones.
2. BFS: a fresh neighbour rots at `minute + 1`; mark it rotten in the grid (or a copy), decrement the fresh count, and queue it.
3. If fresh remains at the end return `-1`, else the largest minute seen.

## Approach

Multi-source BFS: starting all sources at once produces the time each cell is first reached, which is when it rots. Linear in cells.

## Reference

```python
from collections import deque

def minutes_to_rot(grid):
    rows, cols = len(grid), len(grid[0])
    grid = [row[:] for row in grid]
    queue = deque()
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))
            elif grid[r][c] == 1:
                fresh += 1
    minutes = 0
    while queue:
        r, c, t = queue.popleft()
        minutes = max(minutes, t)
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh -= 1
                queue.append((nr, nc, t + 1))
    return minutes if fresh == 0 else -1
```
