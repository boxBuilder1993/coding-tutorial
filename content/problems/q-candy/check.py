from solution import min_sweets
from checker import case

case("valley", min_sweets([1, 0, 2]), 5)
case("plateau", min_sweets([1, 2, 2]), 4)
case("single", min_sweets([5]), 1)
case("rising", min_sweets([1, 2, 3, 4]), 10)
case("falling", min_sweets([4, 3, 2, 1]), 10)
case("peak", min_sweets([1, 3, 2, 2, 1]), 7)
case("empty", min_sweets([]), 0)
