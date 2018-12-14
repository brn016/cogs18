"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from functions import pick_word

words = ['guitar','piano','duduk','clarinet','saxophone','violin','drums', 'trombone']

##
##

def test_pick_word():
    word = "".join(pick_word())
    assert word in words;
    
test_pick_word();