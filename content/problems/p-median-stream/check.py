from solution import median
from checker import case
case("odd", median([40, 2.5, 25]), 25, compare="approx")
case("even", median([40, 2.5, 25, 10]), 17.5, compare="approx")
case("single", median([7]), 7, compare="approx")
original = [3, 1, 2]
median(original)
case("original unchanged", original, [3, 1, 2])
