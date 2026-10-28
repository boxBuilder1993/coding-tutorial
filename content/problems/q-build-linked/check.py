from solution import build
from checker import case, to_list, ListNode

case("three", to_list(build([1, 2, 3])), [1, 2, 3])
case("empty", build([]), None)
case("one", to_list(build(["x"])), ["x"])
case("nodes are ListNodes", isinstance(build([1]), ListNode), True)
case("long", to_list(build(range(5000))), list(range(5000)))
