# First word

Write `first_word(sentence)` that returns the first word of a sentence.
Words are separated by spaces, and the sentence has at least one word.

```static
first_word("fresh bread daily")  ->  "fresh"
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

`split` gives a list of words; take position 0.

## Reference

```python
def first_word(sentence):
    return sentence.split()[0]
```
