from solution import with_extra
from checker import case

case("result has the extra", with_extra(["apple", "bread"], "milk"), ["apple", "bread", "milk"])
case("from empty", with_extra([], "milk"), ["milk"])
original = ["apple", "bread"]
result = with_extra(original, "milk")
case("original is unchanged", original, ["apple", "bread"])
case("result is a different list", result is original, False)
