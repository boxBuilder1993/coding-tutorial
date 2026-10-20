from solution import power
from checker import case

case("two to the five", power(2, 5), 32)
case("anything to the zero", power(3, 0), 1)
case("to the one", power(5, 1), 5)
case("ten to the three", power(10, 3), 1000)
case("negative base", power(-2, 3), -8)
case("zero base", power(0, 4), 0)
case("deeper", power(2, 60), 2 ** 60)
