from solution import can_make
from checker import case

case("enough", can_make("aa", "aab"), True)
case("not enough", can_make("aa", "ab"), False)
case("empty note", can_make("", "x"), True)
case("empty magazine", can_make("a", ""), False)
case("spaces count", can_make("a b", "ab"), False)
case("exact", can_make("abc", "cba"), True)
