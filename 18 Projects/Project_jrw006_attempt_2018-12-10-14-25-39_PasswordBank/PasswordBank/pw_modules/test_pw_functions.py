from pw_functions import create_new_password

def test_create_new_password():
    """Tests the create_new_password function to ensure that the number of characters specified by the user is correct
    and that it asks the user how many characters they'd like to have and that the function returns the password.
    
    When prompted, enter '16'.
    
    Inputs
    ------
    None
    
    Outputs
    -------
    str of randomized characters a length specified by the user"""
    
    # Calls the function
    test_password = create_new_password()
    
    assert len(test_password) == 16
    
test_create_new_password()