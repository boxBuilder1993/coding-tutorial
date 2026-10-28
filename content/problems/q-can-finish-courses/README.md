# Can every course be taken?

`prereqs` is a dictionary from each course to the courses required before it; every
course is a key. Write `can_finish(prereqs)` that returns whether it is possible to take
them all, which fails only when requirements go round in a circle.

```static
can_finish({"a": [], "b": ["a"]})       ->  True
can_finish({"a": ["b"], "b": ["a"]})    ->  False
can_finish({"a": ["a"]})                ->  False
```

The point is to practise cycle detection in a directed graph.

## Starter

```python
def can_finish(prereqs):
    ...
```

## Hints

1. Topological sort from the previous problem: if the order produced has fewer tasks than there are, some were stuck in a cycle.
2. Or DFS with three states per node: unvisited, in progress, done. Reaching an in-progress node means a cycle.

## Approach

Either count what Kahn's algorithm manages to order, or DFS tracking the current path. Both linear.

## Reference

```python
def can_finish(prereqs):
    state = {}

    def dfs(course):
        if state.get(course) == "doing":
            return False
        if state.get(course) == "done":
            return True
        state[course] = "doing"
        for p in prereqs[course]:
            if not dfs(p):
                return False
        state[course] = "done"
        return True

    return all(dfs(c) for c in prereqs)
```
