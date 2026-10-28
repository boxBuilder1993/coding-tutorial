from solution import isomorphic
from checker import case

case("egg add", isomorphic("egg", "add"), True)
case("foo bar", isomorphic("foo", "bar"), False)
case("paper title", isomorphic("paper", "title"), True)
case("two to one", isomorphic("ab", "aa"), False)
case("one to two", isomorphic("aa", "ab"), False)
case("empty", isomorphic("", ""), True)
case("identical", isomorphic("abc", "abc"), True)
