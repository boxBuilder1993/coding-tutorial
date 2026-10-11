from solution import final
from checker import case
case("one undo", final(["add bread", "add milk", "undo", "add eggs"]), ["add bread", "add eggs"])
case("undo on empty is ignored", final(["undo", "add milk"]), ["add milk"])
case("two undos", final(["a", "b", "undo", "undo"]), [])
case("no undos", final(["a", "b"]), ["a", "b"])
