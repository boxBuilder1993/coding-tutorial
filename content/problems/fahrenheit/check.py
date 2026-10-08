from solution import to_celsius
from checker import case

case("boiling point", to_celsius(212), 100.0, compare="approx")
case("freezing point", to_celsius(32), 0.0, compare="approx")
case("body temperature", to_celsius(98.6), 37.0, compare="approx")
case("below zero", to_celsius(-40), -40.0, compare="approx")
