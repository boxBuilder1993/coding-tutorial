from solution import word_counts
from checker import case
case("sentence", word_counts("Bread and milk and bread"), {"bread": 2, "and": 2, "milk": 1})
case("empty", word_counts(""), {})
case("one word repeated", word_counts("a a a"), {"a": 3})
