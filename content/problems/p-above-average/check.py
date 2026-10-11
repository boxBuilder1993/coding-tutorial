from solution import above_average
from checker import case
case("four", above_average([40, 25, 2.5, 60]), 2)
case("all equal", above_average([5, 5, 5]), 0)
case("one", above_average([9]), 0)
