from solution import is_free_delivery
from checker import case

case("60 is free", is_free_delivery(60), True)
case("exactly 50 is free", is_free_delivery(50), True)
case("49 is not free", is_free_delivery(49), False)
case("0 is not free", is_free_delivery(0), False)
case("returns a boolean, not a number", type(is_free_delivery(60)).__name__, "bool")
