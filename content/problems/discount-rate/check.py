from solution import discount_rate
from checker import case

case("bulk", discount_rate(12), 0.2, compare="approx")
case("exactly 10", discount_rate(10), 0.2, compare="approx")
case("exactly 5", discount_rate(5), 0.1, compare="approx")
case("nine items", discount_rate(9), 0.1, compare="approx")
case("four items", discount_rate(4), 0, compare="approx")
case("none", discount_rate(0), 0, compare="approx")
