from solution import pairs
from checker import case
case("four", pairs(["a", "b", "c", "d"]), [("a", "b"), ("c", "d")])
case("empty", pairs([]), [])
case("two", pairs([1, 2]), [(1, 2)])
