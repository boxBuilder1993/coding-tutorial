from solution import largest
from checker import case, from_level_order

case("deep right", largest(from_level_order([8, 3, 10, 1, 6, None, 14])), 14)
case("single", largest(from_level_order([5])), 5)
case("not a search tree", largest(from_level_order([1, 9, 2, 3])), 9)
case("negatives", largest(from_level_order([-5, -9, -2])), -2)
