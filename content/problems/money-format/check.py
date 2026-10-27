from solution import money
from checker import case

case("adds trailing zero", money(2.5), "2.50")
case("whole number", money(40), "40.00")
case("thousands", money(1250), "1,250.00")
case("millions, rounded", money(1234567.891), "1,234,567.89")
case("zero", money(0), "0.00")
case("returns a string", type(money(1)), str)
