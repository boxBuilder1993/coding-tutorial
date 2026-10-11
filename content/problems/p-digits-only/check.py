from solution import code_number
from checker import case
case("code", code_number("BRD-1042-A"), 1042)
case("single digit", code_number("x7y"), 7)
case("leading zeros drop", code_number("A007"), 7)
case("returns an int", type(code_number("1")).__name__, "int")
