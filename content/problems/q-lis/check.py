from solution import lis
from checker import case

case("classic", lis([10, 9, 2, 5, 3, 7, 101, 18]), 4)
case("all equal", lis([7, 7, 7]), 1)
case("empty", lis([]), 0)
case("increasing", lis([1, 2, 3, 4]), 4)
case("decreasing", lis([4, 3, 2, 1]), 1)
case("zigzag", lis([0, 1, 0, 3, 2, 3]), 4)
