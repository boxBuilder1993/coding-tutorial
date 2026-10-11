from solution import average
from checker import case

case("three prices", average([40, 25, 2.5]), 22.5, compare="approx")
case("two prices", average([1, 2]), 1.5, compare="approx")
case("rounds to two places", average([10, 20, 25]), 18.33, compare="approx")
case("single", average([7]), 7, compare="approx")
