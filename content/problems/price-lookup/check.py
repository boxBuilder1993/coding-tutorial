from solution import price_of
from checker import case

case("present", price_of({"apple": 40, "bread": 25}, "bread"), 25)
case("missing gives 0", price_of({"apple": 40, "bread": 25}, "milk"), 0)
case("empty dict", price_of({}, "apple"), 0)
case("value of zero is still returned", price_of({"free": 0}, "free"), 0)
