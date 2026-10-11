from solution import shout
from checker import case
case("two words", shout("fresh bread"), "FRESH BREAD!")
case("already capitals", shout("MILK"), "MILK!")
case("empty", shout(""), "!")
