from solution import undo
from checker import case

history = ["add bread", "add milk"]
case("returns the most recent change", undo(history), "add milk")
case("removes it from the history", history, ["add bread"])
case("empty history gives None", undo([]), None)
single = ["x"]
undo(single)
case("undoing the only change empties the list", single, [])
