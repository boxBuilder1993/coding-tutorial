from solution import is_bipartite
from checker import case

case("square", is_bipartite({0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}), True)
case("triangle", is_bipartite({0: [1, 2], 1: [0, 2], 2: [0, 1]}), False)
case("empty", is_bipartite({}), True)
case("line", is_bipartite({0: [1], 1: [0, 2], 2: [1]}), True)
case("isolated nodes", is_bipartite({0: [], 1: []}), True)
case("pentagon", is_bipartite({0: [1, 4], 1: [0, 2], 2: [1, 3], 3: [2, 4], 4: [3, 0]}), False)
