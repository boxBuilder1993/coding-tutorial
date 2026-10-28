from solution import min_cost
from checker import case

case("three stairs", min_cost([10, 15, 20]), 15)
case("classic", min_cost([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]), 6)
case("two stairs", min_cost([5, 3]), 3)
case("all equal", min_cost([2, 2, 2, 2]), 4)
case("long", min_cost([1] * 100001), 50000)
