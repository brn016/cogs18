"""Test for my functions.
"""

from functions import char_to_ASCII,is_prime

##
##

def char_to_ASCII():

    assert char_to_ASCII("Hello") == [72, 101, 108, 108, 111]
    
def is_prime():
    
    assert True == is_prime(1171)