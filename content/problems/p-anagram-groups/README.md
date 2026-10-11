# Anagram groups

Two words are anagrams if they use exactly the same letters. Write
`anagram_groups(words)` that groups the words into lists of anagrams, with
each group in original order, and the groups sorted by their first word.

```static
anagram_groups(["tea", "eat", "tan", "ate", "nat", "bat"])  ->  [["bat"], ["tan", "nat"], ["tea", "eat", "ate"]]
```

## Starter

```python
def anagram_groups(words):
    ...
```

## Hints

1. A dictionary keyed by the sorted letters of each word.
2. `key = "".join(sorted(word))`; then `if key not in groups: groups[key] = []` before appending; finally `sorted(groups.values(), key=lambda g: g[0])` orders the groups by their first word.

## Approach

Anagrams become identical when their letters are sorted, so that string is the group key. Sorting lists of strings compares their first elements, which gives the required group order.

## Reference

```python
def anagram_groups(words):
    groups = {}
    for word in words:
        key = "".join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return sorted(groups.values())
```
