from solution import common_items
from checker import case

case("example", common_items([3, 1, 4, 1, 5], [5, 1, 9]), [1, 5])
case("nothing in common", common_items([1, 2], [3]), [])
case("empty a", common_items([], [1]), [])
case("empty b", common_items([1], []), [])
case("each once, order of a", common_items([2, 2, 1, 1], [1, 2]), [2, 1])
case("strings", common_items(["milk", "bread", "milk"], ["milk"]), ["milk"])
a = list(range(0, 200000, 2))
b = list(range(0, 300000, 3))
case("a hundred thousand each", common_items(a, b), list(range(0, 200000, 6)))
