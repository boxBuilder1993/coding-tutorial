# Group anagrams

Write `group_anagrams(words)` that groups words that are anagrams of each
other (same letters, any order) and returns the groups as a list of lists.
Within a group keep the words in the order they appeared; order the groups
by the first appearance of any of their words.

```static
group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    ->  [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
group_anagrams([])  ->  []
```

The point is to practise grouping by a computed key.

## Starter

```python
def group_anagrams(words):
    ...
```

## Hints

1. Two words are anagrams exactly when `"".join(sorted(word))` is the same for both. That string is the key.
2. A `defaultdict(list)` or a plain dict: append each word under its key.
3. Dictionaries keep insertion order, so `list(groups.values())` already has the groups in first-appearance order.

## Approach

One pass: compute the sorted-letters key for each word and append the word to that key's list. The dictionary's values, in order, are the answer.

## Reference

```python
def group_anagrams(words):
    groups = {}
    for word in words:
        key = "".join(sorted(word))
        groups.setdefault(key, []).append(word)
    return list(groups.values())
```
