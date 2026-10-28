from solution import rotated_min
from checker import case

case("rotated", rotated_min([7, 9, 1, 2, 4]), 1)
case("not rotated", rotated_min([1, 2, 4, 7, 9]), 1)
case("single", rotated_min([3]), 3)
case("rotated by one", rotated_min([9, 1, 2, 4, 7]), 1)
case("minimum at the end", rotated_min([2, 4, 7, 9, 1]), 1)
case("two items", rotated_min([5, 2]), 2)
big = list(range(300000, 10 ** 6)) + list(range(300000))
case("a million items", rotated_min(big), 0)
