from solution import double_price
from checker import case
case("whole", double_price(40), 80)
case("decimal", double_price(2.5), 5.0)
case("zero", double_price(0), 0)
