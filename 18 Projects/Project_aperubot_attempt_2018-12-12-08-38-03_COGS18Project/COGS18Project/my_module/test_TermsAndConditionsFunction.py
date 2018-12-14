import types
from termsAndConditionsSearchFunction import *

def test_function():
    """Tests for the 'termsAndConditionsSearch' function"""
    
    assert callable(termsAndConditionsSearch)
 
    assert isinstance(termsAndConditionsSearch, types.FunctionType)
