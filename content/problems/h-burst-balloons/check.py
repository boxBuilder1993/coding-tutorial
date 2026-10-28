from solution import max_coins
from checker import case

case("classic", max_coins([3, 1, 5, 8]), 167)
case("two", max_coins([1, 5]), 10)
case("empty", max_coins([]), 0)
case("single", max_coins([7]), 7)
case("ones", max_coins([1, 1, 1]), 3)
case("twelve balloons", max_coins([3, 1, 5, 8, 2, 9, 4, 7, 6, 1, 5, 3]), 1853)
