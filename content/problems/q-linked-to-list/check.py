from solution import values
from checker import case, from_list

case("three", values(from_list([1, 2, 3])), [1, 2, 3])
case("empty", values(None), [])
case("one", values(from_list(["x"])), ["x"])
case("long", values(from_list(range(5000))), list(range(5000)))
