from solution import is_even
from checker import case
case("even", is_even(4), True)
case("odd", is_even(7), False)
case("zero", is_even(0), True)
case("negative even", is_even(-2), True)
