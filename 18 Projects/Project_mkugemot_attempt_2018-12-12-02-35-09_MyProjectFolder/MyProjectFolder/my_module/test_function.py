from function import create_choices

"""
check these three things
    whether the outout is a list
    whether the output has three items
    whether target 'Arizona' is not duplicated
    (The correct answer should be one among the options)
"""
def test_create_choices():
    assert isinstance(create_choices('Arizona'), list) 
    assert len(create_choices('Arizona')) == 3
    assert create_choices('Arizona').count('Arizona') == 1
    