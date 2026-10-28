from solution import min_connection_cost
from checker import case

case("classic", min_connection_cost(4, [(0, 1, 1), (1, 2, 2), (2, 3, 3), (0, 3, 10), (1, 3, 4)]), 6)
case("disconnected", min_connection_cost(3, [(0, 1, 1)]), -1)
case("single town", min_connection_cost(1, []), 0)
case("triangle", min_connection_cost(3, [(0, 1, 5), (1, 2, 5), (0, 2, 1)]), 6)
case("duplicate roads", min_connection_cost(2, [(0, 1, 7), (0, 1, 3)]), 3)
n = 2000
roads = [(i, (i + 1) % n, 1) for i in range(n)] + [(i, (i * 7) % n, 100) for i in range(n)]
case("two thousand towns", min_connection_cost(n, roads), n - 1)
