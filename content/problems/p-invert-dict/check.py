from solution import by_code
from checker import case
case("two", by_code({"bread": "BRD-001", "milk": "MLK-010"}), {"BRD-001": "bread", "MLK-010": "milk"})
case("empty", by_code({}), {})
