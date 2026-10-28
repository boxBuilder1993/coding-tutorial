# Same shape of letters

Two strings are isomorphic if every character of the first can be replaced to get the
second, with each character always mapping to the same character and no two
characters mapping to the same one. Write `isomorphic(s, t)` for strings of equal length.

```static
isomorphic("egg", "add")      ->  True
isomorphic("foo", "bar")      ->  False
isomorphic("paper", "title")  ->  True
isomorphic("ab", "aa")        ->  False
```

The point is to practise maintaining a mapping in both directions.

## Starter

```python
def isomorphic(s, t):
    ...
```

## Hints

1. Two dictionaries: `s_to_t` and `t_to_s`. Walk the pairs of characters with `zip`.
2. If a character is already mapped, it must map to the current partner; otherwise record it in both directions.

## Approach

A one-to-one correspondence needs both directions checked. One pass with two dictionaries; the second direction is what catches `ab` versus `aa`.

## Reference

```python
def isomorphic(s, t):
    s_to_t = {}
    t_to_s = {}
    for a, b in zip(s, t):
        if s_to_t.get(a, b) != b or t_to_s.get(b, a) != a:
            return False
        s_to_t[a] = b
        t_to_s[b] = a
    return True
```
