from solution import labels
from checker import case
case("six", labels(6), ["1", "2", "Box", "4", "Crate", "Box"])
case("fifteen", labels(15), ["1", "2", "Box", "4", "Crate", "Box", "7", "8", "Box", "Crate", "11", "Box", "13", "14", "BoxCrate"])
case("zero", labels(0), [])
case("numbers are strings", labels(1), ["1"])
