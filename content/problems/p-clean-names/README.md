# Clean up names

Staff typed item names with stray spaces and capitals, and some lines are
blank. Write `clean(names)` that returns the names stripped and lowercased,
with blank entries removed.

```static
clean(["  Bread ", "", "MILK", "   "])  ->  ["bread", "milk"]
```

## Starter

```python
def clean(names):
    ...
```

## Hints

1. `strip` and `lower` each one, keep it only if something is left.
2. `if cleaned:` is true for a non-empty string.

## Approach

Transform, then filter on the transformed value. An empty string counts as false.

## Reference

```python
def clean(names):
    result = []
    for name in names:
        cleaned = name.strip().lower()
        if cleaned:
            result.append(cleaned)
    return result
```
