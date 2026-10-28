from solution import median
from checker import case

case("odd total", median([1, 3], [2]), 2.0, compare="approx")
case("even total", median([1, 2], [3, 4]), 2.5, compare="approx")
case("one empty", median([], [1]), 1.0, compare="approx")
case("disjoint ranges", median([1, 2, 3], [10, 20]), 3.0, compare="approx")
case("repeats", median([1, 1], [1, 1]), 1.0, compare="approx")
case("different sizes", median([5], [1, 2, 3, 4, 6, 7]), 4.0, compare="approx")
a = list(range(0, 200000, 2)); b = list(range(1, 200000, 2))
case("two hundred thousand", median(a, b), 99999.5, compare="approx")
