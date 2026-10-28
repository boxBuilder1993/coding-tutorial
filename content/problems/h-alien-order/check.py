from solution import alien_order
from checker import case


def consistent_with(words):
    letters = {ch for w in words for ch in w}
    def check(actual, expected):
        if expected == "":
            return actual == ""
        if sorted(actual) != sorted(letters):
            return False
        pos = {ch: i for i, ch in enumerate(actual)}
        for a, b in zip(words, words[1:]):
            for x, y in zip(a, b):
                if x != y:
                    if pos[x] > pos[y]:
                        return False
                    break
            else:
                if len(a) > len(b):
                    return False
        return True
    return check


w = ["wrt", "wrf", "er", "ett", "rftt"]
case("classic", alien_order(w), "wertf", compare=consistent_with(w))
case("two letters", alien_order(["z", "x"]), "zx", compare=consistent_with(["z", "x"]))
case("contradiction", alien_order(["z", "x", "z"]), "")
case("prefix violation", alien_order(["abc", "ab"]), "")
case("prefix is fine the right way", alien_order(["ab", "abc"]), "abc", compare=consistent_with(["ab", "abc"]))
case("single word", alien_order(["zyx"]), "xyz", compare=consistent_with(["zyx"]))
