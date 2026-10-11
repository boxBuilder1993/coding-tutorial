from solution import count_items
from checker import case

case("repeats", count_items(["apple", "bread", "apple"]), {"apple": 2, "bread": 1})
case("empty", count_items([]), {})
case("all different", count_items(["a", "b", "c"]), {"a": 1, "b": 1, "c": 1})
case("all the same", count_items(["x"] * 5), {"x": 5})
