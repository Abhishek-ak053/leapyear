from leap_year import is_leap_year
def test_is_leap_year():
    assert is_leap_year(2000) == True  # Divisible by 400
def test_is_leap_year():
    assert is_leap_year(1900) == False  # Divisible by 100 but not by 400
def test_is_leap_year():
    assert is_leap_year(2012) == True  # Divisible by 4 but not by 100
    