from solution import difference
from checker import case
case("a larger", difference(40, 25), 15)
case("b larger", difference(25, 40), 15)
case("equal", difference(5, 5), 0)
