from solution import balanced
from checker import case
case("nested", balanced("([])"), True)
case("interleaved", balanced("([)]"), False)
case("unclosed", balanced("(("), False)
case("empty", balanced(""), True)
case("with other characters", balanced("a[b](c)"), True)
case("wrong closer", balanced("(]"), False)
