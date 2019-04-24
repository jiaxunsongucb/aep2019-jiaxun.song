from calculator import Calculator
cal = Calculator()


def test_one_number_should_equal_to_itself():
    assert cal.calculate("1") == 1
