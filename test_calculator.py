from calculator import Calculator
cal = Calculator()


def test_one_number_should_equal_to_itself():
    assert cal.calculate("1") == 1


def test_one_plus_two_should_equal_to_three():
    assert cal.calculate("1 + 2") == 3


def test_one_plus_two_with_parentheses_should_equal_to_three():
    assert cal.calculate("(1 + 2)") == 3


def test_two_times_three_should_equal_to_six():
    assert cal.calculate("2 * 3") == 6


def test_five_minus_two_should_equal_to_three():
    assert cal.calculate("5 - 2") == 3


def test_six_divided_by_two_should_equal_to_three():
    assert cal.calculate("6 / 2") == 3


def test_six_divided_by_two_plus_one_should_equal_to_four():
    assert cal.calculate("6 / 2 + 1") == 4
