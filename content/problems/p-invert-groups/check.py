from solution import stockists
from checker import case
case("two shops", stockists({"north": ["milk", "bread"], "south": ["bread"]}), {"milk": ["north"], "bread": ["north", "south"]})
case("empty", stockists({}), {})
case("sorted shops", stockists({"z": ["x"], "a": ["x"]}), {"x": ["a", "z"]})
