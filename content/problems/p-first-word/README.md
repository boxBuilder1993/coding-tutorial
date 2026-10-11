# First word

Write `first_word(sentence)` that returns the first word of a sentence.
Words are separated by spaces, the sentence has at least one word, and
there may be extra spaces before the first word.

```static
first_word("fresh bread daily")  ->  "fresh"
first_word("   apple pie")       ->  "apple"
```

## Starter

```python
def first_word(sentence):
    ...
```

## Hints

1. `split` then index.
2. `sentence.split()[0]`

## Approach

`split()` with no argument skips any leading spaces and gives a list of words; take position 0. `split(" ")` would give an empty first piece for the second example.

## Reference

```python
def first_word(sentence):
    return sentence.split()[0]
```
