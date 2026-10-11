from solution import price_table
from checker import case

case("two pairs", price_table(["apple", "bread"], [40, 25]), {"apple": 40, "bread": 25})
case("empty", price_table([], []), {})
case("three pairs", price_table(["a", "b", "c"], [1, 2, 3]), {"a": 1, "b": 2, "c": 3})
