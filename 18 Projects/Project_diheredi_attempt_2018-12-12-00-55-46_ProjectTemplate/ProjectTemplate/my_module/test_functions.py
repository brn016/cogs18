"""Test for my functions."""



from functions import choose_madlib
# first test. tests whether or not the function generate_madlib works 
def test_choose_madlib():
    madlib_holiday = "christmas"
    choose_madlib(madlib_holiday)
    assert "christmas" == christmas_madlib