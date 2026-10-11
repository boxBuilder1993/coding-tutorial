from solution import with_tax
from checker import case
case("whole", with_tax(40), 44.0, compare="approx")
case("rounds", with_tax(2.55), 2.81, compare="approx")
case("zero", with_tax(0), 0, compare="approx")
