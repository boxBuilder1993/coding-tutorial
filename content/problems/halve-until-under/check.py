from solution import halvings
from checker import case

case("four halvings", halvings(100, 10), 4)
case("already under", halvings(5, 10), 0)
case("equal to limit needs one", halvings(10, 10), 1)
case("many", halvings(1024, 1), 11)
case("halving gives decimals", halvings(3, 1.5), 2)
