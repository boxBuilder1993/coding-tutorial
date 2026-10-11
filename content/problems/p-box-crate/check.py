from solution import labels
from checker import case
case("six", labels(6), ["1", "2", "Box", "4", "Crate", "Box"])
case("fifteen is both", labels(15)[-1], "BoxCrate")
case("zero", labels(0), [])
case("numbers are strings", labels(1), ["1"])
