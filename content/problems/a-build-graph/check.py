from solution import build_graph
from checker import case

case("triangle", build_graph([("A", "B"), ("A", "C"), ("C", "B")]), {"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]})
case("no edges", build_graph([]), {})
case("single edge", build_graph([(1, 2)]), {1: [2], 2: [1]})
case("neighbours sorted", build_graph([("A", "Z"), ("A", "M"), ("A", "B")]), {"A": ["B", "M", "Z"], "B": ["A"], "M": ["A"], "Z": ["A"]})
case("plain dict", type(build_graph([(1, 2)])), dict)
