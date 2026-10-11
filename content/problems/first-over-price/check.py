from solution import first_over
from checker import case

case("found in the middle", first_over([40, 25, 60, 2.5], 50), 2)
case("none over", first_over([40, 25], 50), -1)
case("first position", first_over([99, 1], 50), 0)
case("returns the first match, not the last", first_over([1, 60, 70], 50), 1)
case("empty", first_over([], 0), -1)
