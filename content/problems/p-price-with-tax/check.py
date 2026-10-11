from solution import with_tax
from checker import case
case("whole", with_tax(40), 44.0, compare="approx")
case("half", with_tax(2.5), 2.75, compare="approx")
case("needs rounding", with_tax(19.99), 21.99, compare="approx")
case("zero", with_tax(0), 0, compare="approx")
