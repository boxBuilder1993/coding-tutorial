from solution import after_sales
from checker import case
case("three sales", after_sales({"apple": 3, "bread": 2}, ["apple", "bread", "apple"]), {"apple": 1, "bread": 1})
case("no sales", after_sales({"apple": 3}, []), {"apple": 3})
case("down to zero", after_sales({"milk": 1}, ["milk"]), {"milk": 0})
