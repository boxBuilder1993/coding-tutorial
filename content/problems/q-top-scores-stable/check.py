from solution import top_k
from checker import case

case("ties by arrival", top_k([("ana", 7), ("ben", 9), ("cy", 7), ("dee", 9)], 3), ["ben", "dee", "ana"])
case("all of them", top_k([("a", 1), ("b", 2)], 2), ["b", "a"])
case("k is 1", top_k([("a", 5), ("b", 5)], 1), ["a"])
case("empty", top_k([], 0), [])
case("many ties", top_k([("p", 3), ("q", 3), ("r", 3), ("s", 4)], 3), ["s", "p", "q"])
