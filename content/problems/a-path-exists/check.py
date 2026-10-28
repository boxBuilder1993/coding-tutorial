from solution import path_exists
from checker import case

graph = {"A": ["B"], "B": ["C"], "C": [], "D": ["A"]}
case("forward path", path_exists(graph, "A", "C"), True)
case("not backwards", path_exists(graph, "C", "A"), False)
case("longer path", path_exists(graph, "D", "C"), True)
case("node reaches itself", path_exists(graph, "C", "C"), True)
case("cycle does not loop forever", path_exists({1: [2], 2: [1], 3: []}, 1, 3), False)
case("cycle with a way out", path_exists({1: [2], 2: [1, 3], 3: []}, 1, 3), True)
