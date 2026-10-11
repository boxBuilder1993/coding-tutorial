from solution import how_many
from checker import case
case("two", how_many(["apple", "bread", "apple"], "apple"), 2)
case("none", how_many(["apple"], "milk"), 0)
case("empty basket", how_many([], "apple"), 0)
