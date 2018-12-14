from classes import Variable


def test_variable():
    
    test_var = Variable('string', True, True)
    
    assert test_var.name == 'string'