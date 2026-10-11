from solution import receipt
from checker import case
case("two items", receipt({"milk": (2, 2.5), "bread": (3, 25)}), ["bread x 3 = 75", "milk x 2 = 5.0"])
case("empty", receipt({}), [])
