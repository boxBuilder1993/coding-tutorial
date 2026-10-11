from solution import title_case
from checker import case
case("mixed", title_case("fresh SOURDOUGH bread"), "Fresh Sourdough Bread")
case("one word", title_case("milk"), "Milk")
case("empty", title_case(""), "")
