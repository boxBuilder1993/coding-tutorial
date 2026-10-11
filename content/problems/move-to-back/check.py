from collections import deque
from solution import to_back
from checker import case

case("three", list(to_back(deque(["Ada", "Grace", "Linus"]))), ["Grace", "Linus", "Ada"])
case("empty", list(to_back(deque())), [])
case("single", list(to_back(deque(["Ada"]))), ["Ada"])
line = deque([1, 2])
case("returns the same deque", to_back(line) is line, True)
