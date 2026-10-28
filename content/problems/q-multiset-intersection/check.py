from solution import intersection
from checker import case

case("repeats", intersection([1, 2, 2, 1], [2, 2]), [2, 2])
case("unsorted input", intersection([4, 9, 5], [9, 4, 9, 8, 4]), [4, 9])
case("nothing shared", intersection([1], [2]), [])
case("empty", intersection([], [1, 1]), [])
case("different counts", intersection([3, 3, 3], [3, 3]), [3, 3])
