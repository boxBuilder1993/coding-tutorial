from solution import levels
from checker import case, from_level_order

case("example tree", levels(from_level_order([8, 3, 10, 1, 6, None, 14])), [[8], [3, 10], [1, 6, 14]])
case("single node", levels(from_level_order([1])), [[1]])
case("empty", levels(None), [])
case("right chain", levels(from_level_order([1, None, 2, None, 3])), [[1], [2], [3]])
case("gaps in a level", levels(from_level_order([1, 2, 3, None, 4, 5, None])), [[1], [2, 3], [4, 5]])
