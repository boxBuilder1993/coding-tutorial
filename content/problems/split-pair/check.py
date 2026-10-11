from solution import describe
from checker import case

case("bread", describe(("bread", 3)), "3 x bread")
case("milk", describe(("milk", 12)), "12 x milk")
case("quantity one", describe(("apple", 1)), "1 x apple")
