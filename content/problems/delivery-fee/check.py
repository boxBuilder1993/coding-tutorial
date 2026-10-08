from solution import delivery_fee
from checker import case

case("large order", delivery_fee(60), 0)
case("exactly 50", delivery_fee(50), 0)
case("small order", delivery_fee(20), 5)
case("empty order", delivery_fee(0), 5)
case("just under", delivery_fee(49.99), 5)
