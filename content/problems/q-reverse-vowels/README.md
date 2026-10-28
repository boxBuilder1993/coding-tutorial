# Reverse only the vowels

Write `reverse_vowels(text)` that returns the string with its vowels (`a e i o u`, either
case) reversed in order while every other character stays in place.

```static
reverse_vowels("hello")     ->  "holle"
reverse_vowels("leetcode")  ->  "leotcede"
reverse_vowels("xyz")       ->  "xyz"
```

The point is to practise two pointers moving inwards and skipping items that do not qualify.

## Starter

```python
def reverse_vowels(text):
    ...
```

## Hints

1. Convert to a list so you can swap. `left` from the start, `right` from the end.
2. Move each pointer inwards until it sits on a vowel; swap; step both. Stop when they cross. Join at the end.

## Approach

Two pointers skipping consonants and swapping vowels. Linear, in place on a list copy.

## Reference

```python
def reverse_vowels(text):
    chars = list(text)
    vowels = set("aeiouAEIOU")
    left, right = 0, len(chars) - 1
    while left < right:
        while left < right and chars[left] not in vowels:
            left += 1
        while left < right and chars[right] not in vowels:
            right -= 1
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return "".join(chars)
```
