from solution import sorted_squares
from checker import case
case("example", sorted_squares([-4, -1, 0, 3, 10]), [0, 1, 9, 16, 100])
case("all negative", sorted_squares([-3, -2, -1]), [1, 4, 9])
case("all positive", sorted_squares([1, 2, 3]), [1, 4, 9])
case("empty", sorted_squares([]), [])
case("single", sorted_squares([-5]), [25])
original = [-2, 1]
sorted_squares(original)
case("original unchanged", original, [-2, 1])
