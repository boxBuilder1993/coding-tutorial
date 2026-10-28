from solution import rearrange
from checker import case
from collections import Counter


def valid_for(text):
    def check(actual, expected):
        if expected == "":
            return actual == ""
        return Counter(actual) == Counter(text) and all(a != b for a, b in zip(actual, actual[1:]))
    return check


case("aab", rearrange("aab"), "aba", compare=valid_for("aab"))
case("impossible", rearrange("aaab"), "")
case("aabb", rearrange("aabb"), "abab", compare=valid_for("aabb"))
case("single", rearrange("x"), "x")
case("empty", rearrange(""), "")
case("longer", rearrange("aaabbc"), "ababac", compare=valid_for("aaabbc"))
case("exactly half plus one", rearrange("aaaabbb"), "abababa", compare=valid_for("aaaabbb"))
