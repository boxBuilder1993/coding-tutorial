from solution import change_due
from checker import case

case("change_due(50, 35)", change_due(50, 35), 15)
case("exact payment", change_due(20, 20), 0)
case("decimals", change_due(10, 2.5), 7.5)
case("order of parameters", change_due(100, 1), 99)
