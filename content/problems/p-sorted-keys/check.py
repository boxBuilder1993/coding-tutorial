from solution import item_names
from checker import case
case("three", item_names({"milk": 2.5, "apple": 40, "bread": 25}), ["apple", "bread", "milk"])
case("empty", item_names({}), [])
case("returns a list", type(item_names({"a": 1})).__name__, "list")
