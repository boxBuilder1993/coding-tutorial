from solution import has_milk
from checker import case
case("capitalised", has_milk("2 x Milk, 1 x bread"), True)
case("absent", has_milk("bread"), False)
case("all capitals", has_milk("MILK"), True)
case("empty", has_milk(""), False)
