from solution import top_sellers
from checker import case
case("top two", top_sellers(["milk", "bread", "milk", "apple", "bread", "milk"], 2), [("milk", 3), ("bread", 2)])
case("tie broken alphabetically", top_sellers(["b", "a"], 2), [("a", 1), ("b", 1)])
case("k too big", top_sellers(["x"], 5), [("x", 1)])
case("empty", top_sellers([], 3), [])
