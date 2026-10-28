from solution import k_frequent
from checker import case

case("classic", k_frequent([1, 1, 1, 2, 2, 3], 2), [1, 2])
case("ties by value", k_frequent([4, 4, 5, 5, 6], 2), [4, 5])
case("k is 1", k_frequent([7, 7, 8], 1), [7])
case("all distinct", k_frequent([3, 1, 2], 3), [1, 2, 3])
case("negatives", k_frequent([-1, -1, 2], 2), [-1, 2])
