from solution import can_finish
from checker import case

case("simple", can_finish({"a": [], "b": ["a"]}), True)
case("two-cycle", can_finish({"a": ["b"], "b": ["a"]}), False)
case("self", can_finish({"a": ["a"]}), False)
case("empty", can_finish({}), True)
case("long chain", can_finish({i: [i - 1] if i else [] for i in range(1000)}), True)
case("cycle deep in", can_finish({1: [], 2: [1], 3: [2, 4], 4: [3]}), False)
