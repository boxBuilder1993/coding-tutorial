from solution import triple
from checker import case

case("triple(5)", triple(5), 15)
case("triple(0)", triple(0), 0)
case("triple(2.5)", triple(2.5), 7.5)
case("triple(-4)", triple(-4), -12)
