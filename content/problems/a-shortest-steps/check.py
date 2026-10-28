from solution import shortest_steps
from checker import case

graph = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A", "D"], "D": ["B", "C", "E"], "E": ["D"], "F": []}
case("three steps", shortest_steps(graph, "A", "E"), 3)
case("unreachable", shortest_steps(graph, "A", "F"), -1)
case("same node", shortest_steps(graph, "A", "A"), 0)
case("neighbour", shortest_steps(graph, "D", "E"), 1)
case("shortest of two routes", shortest_steps({1: [2, 4], 2: [1, 3], 3: [2, 4], 4: [1, 3]}, 1, 3), 2)
line = {i: [j for j in (i - 1, i + 1) if 0 <= j < 50000] for i in range(50000)}
case("a long line", shortest_steps(line, 0, 49999), 49999)
