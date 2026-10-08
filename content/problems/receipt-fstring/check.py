from solution import receipt_line
from checker import case

case("whole numbers", receipt_line("bread", 3, 40), "3 x bread = 120")
case("decimal price", receipt_line("milk", 2, 2.5), "2 x milk = 5.0")
case("quantity one", receipt_line("apple", 1, 40), "1 x apple = 40")
