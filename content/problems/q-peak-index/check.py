from solution import peak_index
from checker import case

case("middle peak", peak_index([1, 3, 5, 4, 2]), 2)
case("early peak", peak_index([0, 10, 5]), 1)
case("late peak", peak_index([1, 2, 3, 4, 0]), 3)
case("long rise", peak_index(list(range(1000)) + [500]), 999)
case("long fall", peak_index([0, 1000] + list(range(999, 0, -1))), 1)
