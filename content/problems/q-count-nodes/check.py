from solution import count
from checker import case, from_level_order

case("six nodes", count(from_level_order([8, 3, 10, 1, 6, None, 14])), 6)
case("empty", count(None), 0)
case("single", count(from_level_order([1])), 1)
case("chain", count(from_level_order([1, None, 2, None, 3])), 3)
