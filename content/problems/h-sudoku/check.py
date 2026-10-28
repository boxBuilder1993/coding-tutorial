from solution import solve
from checker import case

puzzle = ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
answer = ["534678912", "672195348", "198342567", "859761423", "426853791", "713924856", "961537284", "287419635", "345286179"]
case("classic puzzle", solve(puzzle), answer)
case("already solved", solve(answer), answer)
hard = ["..9748...", "7........", ".2.1.9...", "..7...24.", ".64.1.59.", ".98...3..", "...8.3.2.", "........6", "...2759.."]
result = solve(hard)
def valid(g):
    for i in range(9):
        if sorted(g[i]) != list("123456789"): return False
        if sorted(g[r][i] for r in range(9)) != list("123456789"): return False
    for br in range(3):
        for bc in range(3):
            if sorted(g[br*3+r][bc*3+c] for r in range(3) for c in range(3)) != list("123456789"): return False
    return True
case("harder puzzle is valid", valid(result), True)
case("harder puzzle keeps the givens", all(hard[r][c] == "." or hard[r][c] == result[r][c] for r in range(9) for c in range(9)), True)
