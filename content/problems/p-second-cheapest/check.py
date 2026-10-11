from solution import second_cheapest
from checker import case
case("three", second_cheapest([40, 2.5, 25]), 25)
case("two", second_cheapest([9, 3]), 9)
original = [3, 1, 2]
second_cheapest(original)
case("original unchanged", original, [3, 1, 2])
