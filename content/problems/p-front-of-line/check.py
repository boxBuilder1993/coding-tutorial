from collections import deque
from solution import next_customer
from checker import case
line = deque(["Ada", "Grace"])
case("front", next_customer(line), "Ada")
case("not removed", list(line), ["Ada", "Grace"])
