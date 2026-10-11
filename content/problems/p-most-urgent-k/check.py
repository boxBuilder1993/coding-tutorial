from solution import urgent
from checker import case
case("two of three", urgent([(3, "bread"), (1, "cake"), (2, "rolls")], 2), ["cake", "rolls"])
case("k too big", urgent([(1, "a")], 5), ["a"])
case("k zero", urgent([(1, "a")], 0), [])
