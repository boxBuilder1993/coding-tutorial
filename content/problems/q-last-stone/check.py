from solution import last_stone
from checker import case

case("classic", last_stone([2, 7, 4, 1, 8, 1]), 1)
case("pair cancels", last_stone([3, 3]), 0)
case("single", last_stone([5]), 5)
case("empty", last_stone([]), 0)
case("chain of differences", last_stone([10, 4, 2, 10]), 2)
