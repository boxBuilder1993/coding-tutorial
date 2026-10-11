from solution import over
from checker import case
case("two over", over({"apple": 40, "milk": 2.5, "bread": 25}, 20), ["apple", "bread"])
case("none over", over({"milk": 2.5}, 20), [])
case("equal is not over", over({"a": 20}, 20), [])
case("sorted", over({"z": 9, "a": 9}, 1), ["a", "z"])
