from solution import shelf_report
from checker import case
case("two by two", shelf_report([[1, 2], [3, 4]]), {"rows": [3, 7], "columns": [4, 6], "max_row": 1})
case("tie keeps first", shelf_report([[5], [5]]), {"rows": [5, 5], "columns": [10], "max_row": 0})
case("one row", shelf_report([[1, 2, 3]]), {"rows": [6], "columns": [1, 2, 3], "max_row": 0})
