from solution import by_price_then_name
from checker import case

case("example", by_price_then_name([("bread", 25), ("apple", 40), ("milk", 25), ("eggs", 60)]), [("eggs", 60), ("apple", 40), ("bread", 25), ("milk", 25)])
case("all same price", by_price_then_name([("milk", 5), ("apple", 5), ("bread", 5)]), [("apple", 5), ("bread", 5), ("milk", 5)])
case("empty", by_price_then_name([]), [])
case("single", by_price_then_name([("jam", 3)]), [("jam", 3)])
original = [("b", 1), ("a", 2)]
by_price_then_name(original)
case("does not change the input", original, [("b", 1), ("a", 2)])
