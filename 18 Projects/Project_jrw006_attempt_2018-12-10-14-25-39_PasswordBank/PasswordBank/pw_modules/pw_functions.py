import sys
sys.path.append("../")
import os

def create_new_password():
    """
    Creates a new randomized password for the user and stores it in the password storage dictionary.
    Passwords will have at least one uppercase letter, one lowercase letter, one symbol, and one number.
    
    Inputs
    ------
    Takes no inputs
    
    Outputs
    -------
    A string containing a random string of uppercase and lowercase letters, symbols, and numbers of a user specified length
    """
    
    from random import randint
    
    # Has the user indicate how many characters the password should have
    number_of_characters = input("""
How many characters would you like this password to have?
>>> """)
    
    # Organized list of distinct characters the function will use to create the password
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '1234567890'
    symbols = '!@#$%^&*()_+'
    character_bank = [lowercase_letters, uppercase_letters, numbers, symbols]
    
    # While the password is incomplete and does not have one character of each type, create a new password
    one_of_each_type = False 
    while one_of_each_type == False:
        
        # Creates blank string for password to return
        password = ""

        # For loop to create a character for each character required in the password
        for char in range(int(number_of_characters)):
            
            # Pick which type of character to concatenate
            choice = character_bank[randint(0,3)]

            # Checks which type of character is to be used and concatenates a random one to the password string
            if choice == lowercase_letters:
                password += lowercase_letters[randint(0,25)]
            elif choice == uppercase_letters:
                password += uppercase_letters[randint(0,25)]
            elif choice == numbers:
                password += numbers[randint(0,9)]
            elif choice == symbols:
                password += symbols[randint(0,11)]
        
        # Booleans to check if each character type is in the password string
        check_lower = False
        check_upper = False
        check_numbers = False
        check_symbols = False
        
        # For loop to run over what each type of character is and to change the booleans if a type is present
        for char in password:
            if char in lowercase_letters:
                check_lower = True
            elif char in uppercase_letters:
                check_upper = True
            elif char in numbers:
                check_numbers = True
            elif char in symbols:
                check_symbols = True
        
        # Check if all booleans are true, if they are then there is one of each type in the password string
        if check_lower and check_upper and check_numbers and check_symbols:
            one_of_each_type = True
        else:
            continue
    
    return password

def deposit_password(site, username, password):
    """
    Adds a username and password associated with a website to the users storage
    
    Inputs
    ------
    site (str) | the name of the site with which the account is registered
    username (str) | the username of the user for that website
    password (str) | the password that the user would like to store
    
    Outputs
    -------
    Has no outputs
    """
    
    # Opens the storage file
    with open('storage.py', 'a') as file:
        
        # Writes the user's input into the storage file as a new Password class instance
        file.write(f"""
{site} = Password("{site}", "{username}", "{password}")""")
        
def withdraw_password(site):
    """
    Prints the website name, username, and password from storage based on a user specified website
    
    Inputs
    ------
    site (str) | The website of the information the user would like to retrieve

    Outputs
    -------
    Has no outputs besides the print statements
    """
    
    import pw_scripts.storage as storage
    
    # Gets the instance attributes from the storage file
    site_name = getattr(storage, site).site
    username = getattr(storage, site).username
    password = getattr(storage, site).password
    
    # Prints the attributes in a fancy way
    print(f"""
Website:     {site_name}
Username:    {username}
Password:    {password}
""")
