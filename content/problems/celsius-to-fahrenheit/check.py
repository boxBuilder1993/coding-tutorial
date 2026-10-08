from solution import to_fahrenheit
from checker import case

case("freezing point", to_fahrenheit(0), 32.0, compare="approx")
case("boiling point", to_fahrenheit(100), 212.0, compare="approx")
case("freezer", to_fahrenheit(-18), -0.4, compare="approx")
case("same in both scales", to_fahrenheit(-40), -40.0, compare="approx")
