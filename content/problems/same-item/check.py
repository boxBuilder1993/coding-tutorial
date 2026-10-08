from solution import same_item
from checker import case

case("identical", same_item("bread", "bread"), True)
case("different capitals", same_item("Bread", "bread"), True)
case("all capitals", same_item("MILK", "milk"), True)
case("different items", same_item("bread", "milk"), False)
case("prefix is not the same", same_item("bread", "breads"), False)
