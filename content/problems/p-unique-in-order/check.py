from solution import unique
from checker import case
case("with repeats", unique(["apple", "bread", "apple", "milk", "bread"]), ["apple", "bread", "milk"])
case("empty", unique([]), [])
case("order kept", unique(["z", "a", "z"]), ["z", "a"])
case("returns a list", type(unique(["a"])).__name__, "list")
