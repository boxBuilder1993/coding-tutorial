from solution import total
from checker import case

case("three prices", total([40, 25, 2.5]), 67.5, compare="approx")
case("empty", total([]), 0, compare="approx")
case("one price", total([9]), 9, compare="approx")
case("many", total(list(range(1, 101))), 5050, compare="approx")
