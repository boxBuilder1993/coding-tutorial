from solution import balanced
from checker import case

case("balanced with other characters", balanced("(a + b) * (c)"), True)
case("unclosed", balanced("(()"), False)
case("closed too early", balanced("())("), False)
case("empty", balanced(""), True)
case("nested", balanced("((()))"), True)
case("only closers", balanced(")"), False)
case("equal counts but wrong order", balanced(")("), False)
