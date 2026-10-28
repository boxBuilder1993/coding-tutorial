# Letters a phone number could spell

On an old phone keypad `2` is `abc`, `3` is `def`, `4` is `ghi`, `5` is `jkl`, `6` is `mno`,
`7` is `pqrs`, `8` is `tuv`, `9` is `wxyz`. Write `spellings(digits)` that returns every
string the digits (all between 2 and 9) could spell. Order of the output does not matter.

```static
spellings("23")  ->  ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
spellings("")    ->  []
```

The point is to practise a backtracking loop whose choices come from a lookup table.

## Starter

```python
def spellings(digits):
    ...
```

## Hints

1. A dictionary from digit to its letters.
2. Recurse on the position; at each, loop over the letters for that digit, append, recurse, pop. Return `[]` for empty input.

## Approach

Depth equals the number of digits, branching equals the letters per key. Product of the key sizes results.

## Reference

```python
KEYS = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

def spellings(digits):
    if not digits:
        return []
    out = []
    partial = []

    def go(i):
        if i == len(digits):
            out.append("".join(partial))
            return
        for ch in KEYS[digits[i]]:
            partial.append(ch)
            go(i + 1)
            partial.pop()

    go(0)
    return out
```
