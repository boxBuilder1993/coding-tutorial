from solution import most_urgent
from checker import case

orders = [(3, "bread"), (1, "wedding cake"), (2, "sandwiches")]
case("most urgent by priority", most_urgent(orders), "wedding cake")
case("list is unchanged", orders, [(3, "bread"), (1, "wedding cake"), (2, "sandwiches")])
case("single order", most_urgent([(5, "rolls")]), "rolls")
case("urgent one is last", most_urgent([(2, "a"), (3, "b"), (1, "c")]), "c")
