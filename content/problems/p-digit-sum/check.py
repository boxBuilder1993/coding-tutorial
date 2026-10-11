from solution import digit_sum
from checker import case
case("1234", digit_sum(1234), 10)
case("zero", digit_sum(0), 0)
case("single digit", digit_sum(7), 7)
case("with zeros", digit_sum(1000), 1)
