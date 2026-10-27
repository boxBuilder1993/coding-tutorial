from solution import group_by_length
from checker import case

case("two groups", group_by_length(["apple", "milk", "bread", "eggs"]), {5: ["apple", "bread"], 4: ["milk", "eggs"]})
case("empty", group_by_length([]), {})
case("all different lengths", group_by_length(["a", "bb", "ccc"]), {1: ["a"], 2: ["bb"], 3: ["ccc"]})
case("keeps order within a group", group_by_length(["jam", "tea", "pie"]), {3: ["jam", "tea", "pie"]})
case("returns a plain dict", type(group_by_length(["x"])), dict)
