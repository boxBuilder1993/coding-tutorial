from solution import sort_grades
from checker import case

case("mixed", sort_grades(["C", "A", "F", "B", "A", "C"]), ["A", "A", "B", "C", "C", "F"])
case("empty", sort_grades([]), [])
case("one grade only", sort_grades(["D", "D"]), ["D", "D"])
case("already sorted", sort_grades(["A", "B", "C", "D", "F"]), ["A", "B", "C", "D", "F"])
case("reverse", sort_grades(["F", "D", "C", "B", "A"]), ["A", "B", "C", "D", "F"])
big = ["ABCDF"[(i * 7) % 5] for i in range(100000)]
case("a hundred thousand", sort_grades(big), sorted(big))
