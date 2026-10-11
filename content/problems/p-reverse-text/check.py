from solution import backwards
from checker import case
case("bread", backwards("bread"), "daerb")
case("empty", backwards(""), "")
case("palindrome", backwards("level"), "level")
