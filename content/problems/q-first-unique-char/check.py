from solution import first_unique
from checker import case

case("first letter", first_unique("leetcode"), 0)
case("later letter", first_unique("loveleetcode"), 2)
case("none", first_unique("aabb"), -1)
case("empty", first_unique(""), -1)
case("last letter", first_unique("aabbc"), 4)
