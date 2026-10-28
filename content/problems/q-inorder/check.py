from solution import inorder
from checker import case, from_level_order as t

case("bst gives sorted", inorder(t([8, 3, 10, 1, 6, None, 14])), [1, 3, 6, 8, 10, 14])
case("empty", inorder(None), [])
case("single", inorder(t([1])), [1])
case("not a bst", inorder(t([1, 2, 3])), [2, 1, 3])
case("right chain", inorder(t([1, None, 2, None, 3])), [1, 2, 3])
