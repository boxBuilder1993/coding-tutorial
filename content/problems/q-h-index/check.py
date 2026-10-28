from solution import h_index
from checker import case

case("classic", h_index([3, 0, 6, 1, 5]), 3)
case("small", h_index([1, 3, 1]), 1)
case("zero", h_index([0]), 0)
case("all large", h_index([100, 100]), 2)
case("empty", h_index([]), 0)
case("ascending", h_index([1, 2, 3, 4, 5]), 3)
