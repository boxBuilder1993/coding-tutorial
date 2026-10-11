from solution import to_pay
from checker import case
case("large", to_pay(120), 96.0, compare="approx")
case("medium", to_pay(60), 54.0, compare="approx")
case("small", to_pay(20), 20, compare="approx")
case("exactly 100", to_pay(100), 80.0, compare="approx")
case("exactly 50", to_pay(50), 45.0, compare="approx")
case("needs rounding", to_pay(77.77), 69.99, compare="approx")
