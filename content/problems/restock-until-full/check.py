from solution import deliveries_needed
from checker import case

case("three boxes", deliveries_needed(2, 3, 10), 3)
case("already enough", deliveries_needed(10, 3, 10), 0)
case("exactly reaches", deliveries_needed(4, 3, 10), 2)
case("one big box", deliveries_needed(0, 100, 10), 1)
