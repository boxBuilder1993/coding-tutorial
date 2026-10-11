from solution import names_by_priority
from checker import case
case("three", names_by_priority([(3, "bread"), (1, "cake"), (2, "rolls")]), ["cake", "rolls", "bread"])
case("empty", names_by_priority([]), [])
original = [(2, "b"), (1, "a")]
names_by_priority(original)
case("original unchanged", original, [(2, "b"), (1, "a")])
