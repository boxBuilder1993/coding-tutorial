from solution import follows
from checker import case

case("abba", follows("abba", "dog cat cat dog"), True)
case("abba wrong last", follows("abba", "dog cat cat fish"), False)
case("aaaa", follows("aaaa", "dog cat cat dog"), False)
case("length mismatch", follows("abc", "dog dog"), False)
case("two letters one word", follows("ab", "dog dog"), False)
case("single", follows("a", "x"), True)
