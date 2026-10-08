from solution import is_valid_quantity
from checker import case

case("lower bound", is_valid_quantity(1), True)
case("upper bound", is_valid_quantity(20), True)
case("middle", is_valid_quantity(7), True)
case("zero", is_valid_quantity(0), False)
case("too many", is_valid_quantity(21), False)
case("negative", is_valid_quantity(-3), False)
