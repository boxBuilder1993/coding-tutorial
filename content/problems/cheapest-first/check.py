from solution import cheapest_first
from checker import case

case("three prices", cheapest_first([40, 2.5, 25]), [2.5, 25, 40])
case("already sorted", cheapest_first([1, 2, 3]), [1, 2, 3])
case("empty", cheapest_first([]), [])
original = [40, 2.5, 25]
cheapest_first(original)
case("original is unchanged", original, [40, 2.5, 25])
