from solution import letter_counts
from checker import case
case("sentence", letter_counts("a bad cab"), {"a": 3, "b": 2, "d": 1, "c": 1})
case("empty", letter_counts(""), {})
case("only spaces", letter_counts("   "), {})
