from solution import numbered
from checker import case

case("two items", numbered(["apple", "bread"]), ["1. apple", "2. bread"])
case("empty", numbered([]), [])
case("numbering continues past 9", numbered(list("abcdefghij"))[-1], "10. j")
