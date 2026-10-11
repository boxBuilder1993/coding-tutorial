from solution import available
from checker import case
case("mixed", available({"milk": 0, "apple": 3, "bread": 1}), ["apple", "bread"])
case("all out", available({"milk": 0}), [])
case("empty", available({}), [])
case("sorted, not insertion order", available({"milk": 2, "bread": 1, "apple": 3}), ["apple", "bread", "milk"])
