from solution import clamp_quantity
from checker import case

case("in range", clamp_quantity(7), 7)
case("lower bound unchanged", clamp_quantity(1), 1)
case("upper bound unchanged", clamp_quantity(20), 20)
case("below range", clamp_quantity(0), 1)
case("far below", clamp_quantity(-50), 1)
case("above range", clamp_quantity(99), 20)
