from solution import parts
from checker import case
case("code", parts("BRD-001-A"), ("BRD", "001", "A"))
case("returns a tuple", type(parts("A-B-C")).__name__, "tuple")
