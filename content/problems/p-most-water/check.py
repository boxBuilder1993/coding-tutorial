from solution import most_water
from checker import case
case("example", most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
case("two walls", most_water([1, 1]), 1)
case("increasing", most_water([1, 2, 3, 4]), 4)
case("tall ends", most_water([5, 1, 1, 5]), 15)
