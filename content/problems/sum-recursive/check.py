from solution import total
from checker import case

case("three numbers", total([3, 5, 7]), 15)
case("empty", total([]), 0)
case("one number", total([4]), 4)
case("negatives", total([1, -1, 2, -2]), 0)
case("floats", total([0.5, 0.25]), 0.75, compare="approx")
case("a hundred items", total(list(range(100))), 4950)
