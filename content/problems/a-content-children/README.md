# Content children

`appetites` lists how big a biscuit each child needs; `biscuits` lists the
sizes available. A child is content with a biscuit at least as big as
their appetite, and each biscuit goes to at most one child. Write
`content_children(appetites, biscuits)` that returns the most children who
can be made content.

```static
content_children([1, 2, 3], [1, 1])  ->  1
content_children([1, 2], [1, 2, 3])  ->  2
content_children([], [1])            ->  0
```

The point is to practise the "smallest that fits" greedy rule with two
sorted lists and two pointers.

## Starter

```python
def content_children(appetites, biscuits):
    ...
```

## Hints

1. Sort both lists (use `sorted` so you do not change the caller's lists).
2. Walk the biscuits in order with an index into the children; when a biscuit satisfies the current child, move to the next child.
3. The child index at the end is the count.

## Approach

With both sorted, each biscuit is offered to the least demanding unserved child. Giving it to anyone hungrier would waste a biscuit that a smaller one might not cover. Sort then one pass.

## Reference

```python
def content_children(appetites, biscuits):
    kids = sorted(appetites)
    child = 0
    for b in sorted(biscuits):
        if child < len(kids) and b >= kids[child]:
            child += 1
    return child
```
