from solution import max_depth
from checker import case
case("three deep", max_depth("(a(b)(c(d)))"), 3)
case("one", max_depth("()"), 1)
case("empty", max_depth(""), 0)
case("unclosed", max_depth("(()"), -1)
case("closed too early", max_depth(")("), -1)
case("side by side is not nested", max_depth("()()"), 1)
case("no brackets at all", max_depth("abc"), 0)
