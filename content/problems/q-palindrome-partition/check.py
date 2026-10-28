from solution import palindrome_cuts
from checker import case


def same(actual, expected):
    return sorted(tuple(p) for p in actual) == sorted(tuple(p) for p in expected)


case("aab", palindrome_cuts("aab"), [["a", "a", "b"], ["aa", "b"]], compare=same)
case("single", palindrome_cuts("a"), [["a"]], compare=same)
case("all distinct", palindrome_cuts("abc"), [["a", "b", "c"]], compare=same)
case("aaa", palindrome_cuts("aaa"), [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]], compare=same)
case("count", len(palindrome_cuts("abbab")), 4)
