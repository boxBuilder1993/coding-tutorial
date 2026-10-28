# Steps through a maze

`maze` is a list of strings using `S` for the start, `E` for the exit, `#` for walls and
`.` for open floor. Moves go up, down, left or right. Write `maze_steps(maze)` that
returns the fewest moves from `S` to `E`, or `-1` if the exit cannot be reached.

```static
maze_steps(["S.#", ".##", "..E"])  ->  4
maze_steps(["S#E"])                ->  -1
```

The point is to practise BFS on a grid with a distance map.

## Starter

```python
def maze_steps(maze):
    ...
```

## Hints

1. Find `S` with a double loop. BFS over `(r, c)` cells with a dictionary of distances.
2. Skip walls and out-of-bounds cells. Return the distance when you pop `E`.

## Approach

Breadth-first search over cells with distance recorded on first visit. Linear in the number of cells.

## Reference

```python
from collections import deque

def maze_steps(maze):
    rows, cols = len(maze), len(maze[0])
    start = next((r, c) for r in range(rows) for c in range(cols) if maze[r][c] == "S")
    dist = {start: 0}
    queue = deque([start])
    while queue:
        r, c = queue.popleft()
        if maze[r][c] == "E":
            return dist[(r, c)]
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != "#" and (nr, nc) not in dist:
                dist[(nr, nc)] = dist[(r, c)] + 1
                queue.append((nr, nc))
    return -1
```
