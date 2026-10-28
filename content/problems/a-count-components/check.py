from solution import count_components
from checker import case

case("three groups", count_components({1: [2], 2: [1], 3: [4], 4: [3, 5], 5: [4], 6: []}), 3)
case("empty graph", count_components({}), 0)
case("all connected", count_components({"A": ["B"], "B": ["A", "C"], "C": ["B"]}), 1)
case("no edges at all", count_components({1: [], 2: [], 3: []}), 3)
case("a cycle", count_components({1: [2, 3], 2: [1, 3], 3: [1, 2]}), 1)
big = {i: ([i + 1] if i % 2 == 0 else [i - 1]) for i in range(100000)}
case("fifty thousand pairs", count_components(big), 50000)
