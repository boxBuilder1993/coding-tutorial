from solution import merged
from checker import case
case("overlap", merged({"apple": 3, "bread": 2}, {"bread": 1, "milk": 5}), {"apple": 3, "bread": 3, "milk": 5})
case("empty b", merged({"a": 1}, {}), {"a": 1})
case("empty a", merged({}, {"a": 1}), {"a": 1})
a = {"x": 1}
merged(a, {"x": 1})
case("inputs unchanged", a, {"x": 1})
