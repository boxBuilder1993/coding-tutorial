from solution import change
from checker import case

case("67", change(67), [25, 25, 10, 5, 1, 1])
case("30", change(30), [25, 5])
case("zero", change(0), [])
case("exactly one coin", change(10), [10])
case("only ones", change(4), [1, 1, 1, 1])
case("99", change(99), [25, 25, 25, 10, 10, 1, 1, 1, 1])
