# Does the sentence follow the pattern?

Write `follows(pattern, sentence)` where `pattern` is a string of letters and `sentence`
is words separated by single spaces. Return `True` if there is a one-to-one
correspondence between letters and words.

```static
follows("abba", "dog cat cat dog")   ->  True
follows("abba", "dog cat cat fish")  ->  False
follows("aaaa", "dog cat cat dog")   ->  False
follows("abc", "dog dog")            ->  False
```

The point is to practise a two-way mapping where the two sides are different kinds of thing.

## Starter

```python
def follows(pattern, sentence):
    ...
```

## Hints

1. Split the sentence. If the counts differ, return `False`.
2. Then the isomorphic check from earlier, between letters and words, with two dictionaries.

## Approach

Length check, then walk letter-word pairs with two dictionaries enforcing both directions.

## Reference

```python
def follows(pattern, sentence):
    words = sentence.split()
    if len(words) != len(pattern):
        return False
    l2w, w2l = {}, {}
    for letter, word in zip(pattern, words):
        if l2w.get(letter, word) != word or w2l.get(word, letter) != letter:
            return False
        l2w[letter] = word
        w2l[word] = letter
    return True
```
