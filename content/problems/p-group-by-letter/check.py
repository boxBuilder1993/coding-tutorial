from solution import by_letter
from checker import case
case("three", by_letter(["apple", "bread", "apricot"]), {"a": ["apple", "apricot"], "b": ["bread"]})
case("empty", by_letter([]), {})
case("order within group kept", by_letter(["bz", "ba"]), {"b": ["bz", "ba"]})
