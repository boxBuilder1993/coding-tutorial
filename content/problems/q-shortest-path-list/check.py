from solution import shortest_path
from checker import case

graph = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A", "D"], "D": ["B", "C", "E"], "E": ["D"]}
case("route", shortest_path(graph, "A", "E"), ["A", "B", "D", "E"])
case("same node", shortest_path(graph, "A", "A"), ["A"])
case("unreachable", shortest_path({"A": [], "B": []}, "A", "B"), [])
case("neighbour", shortest_path(graph, "D", "E"), ["D", "E"])
case("neighbour order decides ties", shortest_path({1: [3, 2], 2: [1, 4], 3: [1, 4], 4: [2, 3]}, 1, 4), [1, 3, 4])
