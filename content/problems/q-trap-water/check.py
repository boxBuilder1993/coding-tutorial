from solution import trapped
from checker import case

case("classic", trapped([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)
case("second classic", trapped([4, 2, 0, 3, 2, 5]), 9)
case("rising", trapped([1, 2, 3]), 0)
case("empty", trapped([]), 0)
case("valley", trapped([3, 0, 3]), 3)
case("two walls only", trapped([5, 5]), 0)
