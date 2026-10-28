from solution import evens_first
from checker import case

case("mixed", evens_first([3, 1, 2, 4, 5, 6]), [2, 4, 6, 3, 1, 5])
case("all odd", evens_first([1, 3]), [1, 3])
case("all even", evens_first([4, 2]), [4, 2])
case("empty", evens_first([]), [])
case("negatives", evens_first([-3, -2, 0, 1]), [-2, 0, -3, 1])
