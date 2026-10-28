from solution import pivot_index
from checker import case

case("classic", pivot_index([1, 7, 3, 6, 5, 6]), 3)
case("none", pivot_index([1, 2, 3]), -1)
case("first index", pivot_index([2, 1, -1]), 0)
case("last index", pivot_index([1, -1, 2]), 2)
case("single", pivot_index([5]), 0)
case("empty", pivot_index([]), -1)
