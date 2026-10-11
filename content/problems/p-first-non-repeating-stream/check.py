from solution import first_unique_stream
from checker import case
case("aabc", first_unique_stream("aabc"), "a#bb")
case("abab", first_unique_stream("abab"), "aab#")
case("empty", first_unique_stream(""), "")
case("all distinct", first_unique_stream("xyz"), "xxx")
case("recovers after a repeat", first_unique_stream("aab"), "a#b")
