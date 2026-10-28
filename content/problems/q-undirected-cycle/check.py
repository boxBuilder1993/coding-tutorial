from solution import has_cycle
from checker import case

case("line", has_cycle({1: [2], 2: [1, 3], 3: [2]}), False)
case("triangle", has_cycle({1: [2, 3], 2: [1, 3], 3: [1, 2]}), True)
case("two separate edges", has_cycle({1: [2], 2: [1], 3: [4], 4: [3]}), False)
case("empty", has_cycle({}), False)
case("cycle in the second component", has_cycle({1: [], 2: [3, 4], 3: [2, 4], 4: [2, 3]}), True)
case("tree", has_cycle({1: [2, 3], 2: [1, 4, 5], 3: [1], 4: [2], 5: [2]}), False)
