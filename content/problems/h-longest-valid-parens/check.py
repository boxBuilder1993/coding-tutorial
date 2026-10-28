from solution import longest_valid
from checker import case

case("prefix", longest_valid("(()"), 2)
case("middle", longest_valid(")()())"), 4)
case("empty", longest_valid(""), 0)
case("all balanced", longest_valid("()()"), 4)
case("nested", longest_valid("((()))"), 6)
case("broken middle", longest_valid("()(()"), 2)
case("long", longest_valid("(" + "()" * 50000), 100000)
