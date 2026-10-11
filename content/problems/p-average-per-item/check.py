from solution import averages
from checker import case
case("two items", averages({"apple": [40, 42], "milk": [2.5]}), {"apple": 41.0, "milk": 2.5})
case("rounding", averages({"x": [1, 2, 2]}), {"x": 1.67})
case("empty", averages({}), {})
