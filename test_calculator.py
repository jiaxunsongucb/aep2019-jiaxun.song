from calculator import Calculator
cal = Calculator()


def test_one_number_should_equal_to_itself():
    assert cal.calculate("1") == 1


def test_one_plus_two_should_equal_to_three():
    assert cal.calculate("1+2") == 3

def test_one_plus_two_with_parentheses_should_equal_to_three():
    assert cal.calculate("(1+2)") == 3
