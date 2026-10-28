from solution import distances
from checker import case

graph = {"A": [("B", 4), ("C", 1)], "B": [("D", 1)], "C": [("B", 2), ("D", 5)], "D": []}
case("classic", distances(graph, "A"), {"A": 0, "B": 3, "C": 1, "D": 4})
case("from a sink", distances(graph, "D"), {"D": 0})
case("unreachable omitted", distances({1: [(2, 1)], 2: [], 3: [(1, 1)]}, 1), {1: 0, 2: 1})
case("zero weights", distances({1: [(2, 0)], 2: [(3, 0)], 3: []}, 1), {1: 0, 2: 0, 3: 0})
case("longer direct edge loses", distances({1: [(2, 10), (3, 1)], 3: [(2, 1)], 2: []}, 1), {1: 0, 3: 1, 2: 2})
n = 20000
line = {i: ([(i + 1, 2)] if i + 1 < n else []) + ([(i + 2, 5)] if i + 2 < n else []) for i in range(n)}
case("twenty thousand nodes", distances(line, 0)[n - 1], 2 * (n - 1))
