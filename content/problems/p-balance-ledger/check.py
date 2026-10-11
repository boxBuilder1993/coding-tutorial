from solution import ledger
from checker import case
case("stays positive", ledger([("sale", 50), ("rent", -30), ("sale", 10)]), ["sale: 50", "rent: 20", "sale: 30"])
case("overdrawn stops early", ledger([("sale", 10), ("rent", -30), ("sale", 100)]), ["sale: 10", "rent: -20", "OVERDRAWN"])
case("empty", ledger([]), [])
case("zero is not overdrawn", ledger([("a", 5), ("b", -5)]), ["a: 5", "b: 0"])
