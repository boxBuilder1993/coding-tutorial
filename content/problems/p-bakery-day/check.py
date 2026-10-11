from solution import schedule
from checker import case
case("two hours", schedule([(3, "bread"), (1, "cake"), (2, "rolls")], 2), ["cake", "rolls"])
case("runs out", schedule([(1, "cake")], 5), ["cake"])
case("zero hours", schedule([(1, "cake")], 0), [])
case("all", schedule([(2, "b"), (1, "a"), (3, "c")], 3), ["a", "b", "c"])
