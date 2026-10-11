from solution import wrap
from checker import case
case("example", wrap("fresh sourdough bread baked daily", 12), ["fresh", "sourdough", "bread baked", "daily"])
case("fits on one line", wrap("milk eggs", 20), ["milk eggs"])
case("empty", wrap("", 10), [])
case("exact fit", wrap("ab cd", 5), ["ab cd"])
case("one over", wrap("ab cd", 4), ["ab", "cd"])
