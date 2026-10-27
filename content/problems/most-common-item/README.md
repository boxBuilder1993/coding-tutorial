# Most common item

Write `most_common_item(items)` that returns the value that appears most
often in the list. If two values tie, return the one that appears first in
the list. The list has at least one item.

```static
most_common_item(["apple", "bread", "apple"])  ->  "apple"
most_common_item(["milk", "bread", "bread", "milk"])  ->  "milk"
```

The point is to practise `Counter` and `most_common`.

## Starter

```python
def most_common_item(items):
    ...
```

## Hints

1. `Counter(items).most_common(1)` gives a list with one `(value, count)` pair.
2. Take the pair with `[0]`, then the value with another `[0]`.
3. `most_common` already breaks ties by first appearance, so no extra work is needed.

## Approach

Build the Counter, ask for the top one, and unpack it: `Counter(items).most_common(1)[0][0]`. Remember the import line.

## Reference

```python
from collections import Counter

def most_common_item(items):
    return Counter(items).most_common(1)[0][0]
```
