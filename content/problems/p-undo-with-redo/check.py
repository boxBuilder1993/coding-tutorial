from solution import final
from checker import case
case("undo then redo", final(["a", "b", "undo", "redo"]), ["a", "b"])
case("new action clears redo", final(["a", "b", "undo", "c", "redo"]), ["a", "c"])
case("ignored when empty", final(["undo", "redo", "a"]), ["a"])
case("multiple undos and redos", final(["a", "b", "c", "undo", "undo", "redo"]), ["a", "b"])
