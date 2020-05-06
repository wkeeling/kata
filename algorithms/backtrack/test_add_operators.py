"""
Given a string that contains only digits 0-9 and a target value,
return all possibilities to add binary operators (not unary) +, -, or *
between the digits so they prevuate to the target value.
Examples:
"123", 6 -> ["1+2+3", "1*2*3"]
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []
"""


def add_operators(num, target):
    pass


def test_add_operators():
    assert add_operators('123', 6) == ['1+2+3', '1*2*3']
    assert add_operators('232', 8) == ['2*3+2', '2+3*2']
    assert add_operators('105', 5) == ['1*0+5', '10-5']
    assert add_operators('00', 0) == ['0+0', '0-0', '0*0']
    assert add_operators('3456237490', 9191) == []
