# Arrays and hashing

Most "find a pair, count things, detect duplicates" problems have an O(n²)
brute force that compares every element with every other. A dict or set
turns "have I seen X?" into a constant-time question, so one pass does the
job. Ask: **what would I need to remember so the current element can be
resolved immediately?**

```python
seen = set()
for x in [3, 1, 4, 1, 5]:
    if x in seen:
        print("repeat:", x)
    seen.add(x)
```

## Problems

:::problem two-sum

A linked-list problem, to show the structure helpers:

:::problem reverse-linked-list
