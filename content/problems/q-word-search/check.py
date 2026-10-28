from solution import exists
from checker import case

grid = ["ABCE", "SFCS", "ADEE"]
case("ABCCED", exists(grid, "ABCCED"), True)
case("SEE", exists(grid, "SEE"), True)
case("ABCB reuses a cell", exists(grid, "ABCB"), False)
case("single letter", exists(["A"], "A"), True)
case("not present", exists(["AB"], "C"), False)
case("zigzag", exists(["AAB", "ACA"], "ABA"), True)
case("dead end then retry", exists(["ABC", "AAD"], "ABAC"), False)
