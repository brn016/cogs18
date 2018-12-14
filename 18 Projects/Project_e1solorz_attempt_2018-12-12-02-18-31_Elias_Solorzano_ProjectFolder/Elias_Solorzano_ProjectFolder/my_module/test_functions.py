"""Tests for the `top_list_x` function."""
import pandas as pd
import collections
from my_module.functions import top_list_x

def test_top_list_x():
    
    #makes sure the function outputs a list
    assert isinstance(top_list_x(best_batter_2015,'HR','Name'),list)
    
    #the first value in the list is the top batter according to homeruns (AB > 300 and G >100) which should be Gerardo Parra in 2015
    assert top_list_x(best_batter_2015,'HR','Name')[0] == 'Gerardo Parra'