from solution import flatten
from checker import case

case("mixed depths", flatten(["apple", ["bread", ["jam"]], "milk"]), ["apple", "bread", "jam", "milk"])
case("deeply nested", flatten([1, [2, [3, [4]]]]), [1, 2, 3, 4])
case("already flat", flatten([1, 2, 3]), [1, 2, 3])
case("empty", flatten([]), [])
case("empty inner lists", flatten([[], [1, []], 2]), [1, 2])
case("keeps order", flatten([[3, 2], [1], 0]), [3, 2, 1, 0])
