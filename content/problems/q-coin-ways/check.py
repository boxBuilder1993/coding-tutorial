from solution import change_ways
from checker import case

case("five", change_ways(5, [1, 2, 5]), 4)
case("impossible", change_ways(3, [2]), 0)
case("exact coin", change_ways(10, [10]), 1)
case("zero amount", change_ways(0, [1, 2]), 1)
case("order does not matter", change_ways(3, [1, 2]), 2)
case("larger", change_ways(100, [1, 5, 10, 25, 50]), 292)
