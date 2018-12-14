"""
PASSWORDBANK
PasswordBank is an interactive Python program used to store, retrieve, and create passwords.
"""

# Creating a clear function so that we can keep the terminal looking pretty
import os
def clear():
    os.system('cls')
    
# Imports functions necessary to run PasswordBank
import sys
sys.path.append("../")
from pw_modules.pw_functions import create_new_password, deposit_password, withdraw_password

import storage
import importlib

clear()

# Welcome Screen
print("""
~~~~~~~~~~~~
PasswordBank
~~~~~~~~~~~~

Welcome to PasswordBank!
PasswordBank is your one-stop shop for secure password storage!""")

# While the user still wants to do stuff
user_active = True
while user_active:
    
    # Welcome Screen
    print("""
To use PasswordBank, simply type one of the commands below:
'deposit password', 'withdraw password', 'quit'""")
    
    # Takes command from user input
    user_action = input("""
>>>    """)
    
    # Checks command and performs function
    if user_action == "deposit password":
        
        # If the user wants to deposit a password, clear the window
        clear()
        
        # Pretty header telling the user what they're doing
        print("""
~~~~~~~~~~~~~~~~
Deposit Password
~~~~~~~~~~~~~~~~
""")
        
        # Checks to make sure that the user isn't depositing a duplicate password
        password_in_storage = True
        while password_in_storage:
            
            # Has the user input the name of the website they're depositing a password for
            site = input("""You must be able to remember this name to withdraw the password later.
Website Name:
>>>    """)
            
            # If the website is already in storage, stop 'em while they're hot
            if hasattr(storage, site):
                
                print("""It appears there's already a website in storage with that name. 
Please try again.
""")
            # If it's not, let 'em do it
            else:
                password_in_storage = False
                break
        
        print("I love that website.")
        
        # Has the user input the username of their account
        username = input("""
Username:
>>>    """)
        
        print("Nice name... has a lot of character.")
        
        print("""
So for the password, you can either 'input' your own, or 
PasswordBank can 'create' one for you using its SuperSecure(TM) technology.
Which would you like? 
'input' or 'create'""")
        
        # The user must input 'input' or 'create' in order to continue
        acceptable = False
        while not acceptable:
            
            # Has the user decide to input their own password or have PasswordBank create a "SuperSecure(TM)" one for them
            choice = input(""">>>    """)
        
            if choice == "input":
                # If the user wants to input their own password, let 'em do it. 
                
                # Set acceptable to true so they don't have to do it again
                acceptable = True
                
                # Has the user input their own password
                password = input("""
Password:
>>>    """)
                
            elif choice == "create":
                # If the user wants PasswordBank to create a password for them, let 'em do it.
                
                # Set acceptable to true so they don't have to do it again
                acceptable = True
                
                # Runs the create new password function
                password = create_new_password()
                
                # Prints the password for the user's reference
                print("""
This is the password I made for you:
""" + password)
                
                # Lets the user see the password
                lets_continue = input("""
Press enter to continue with this password.""")
                
            else:
                # The user messed up, let 'em try again
                print("""
I don't know what you're trying to do.
Remember, only 'input' or 'create'.
""")
        # Deposits the password to storage    
        deposit_password(site, username, password)
        
        # This reloads storage so that the newly deposited password can be withdrawn immediately
        importlib.reload(storage)
        
        # Clears terminal
        clear()
        
        print("""
Password deposited successfully.""")
        
        
    elif user_action == "withdraw password":
        
        # If the user wants to withdraw a password, clear the window
        clear()
        
        # Pretty header telling the user what they're doing
        print("""
~~~~~~~~~~~~~~~~~
Withdraw Password
~~~~~~~~~~~~~~~~~""")
        
        # While loop to stay in if the user enters a website that isn't in storage
        password_in_storage = False
        while not password_in_storage:
            
            # Asks the user to input a website they want their password from
            site = input("""
What website would you like to withdraw your password from?
>>>    """)
            
            # Checks if the website has an instance in storage
            if hasattr(storage, site):
                
                # Gives them what they want
                withdraw_password(site)
                
                # Break out of the loop if it's in storage
                password_in_storage = True
                break
                
            else:
                
                # Tells the user they messed up
                print("""It appears this website is not in storage. Please check your spelling and try again.""")
        
        # Lets them see the password all nice and clear
        lets_continue = input("""Here ya go! Press enter to continue.""")
        
         # Clears terminal
        clear()
        
    elif user_action == "quit":
        
        # If the user wants to leave, let them
        user_active == False
        
        break
        
    else:
        
        # The user entered something the program cannot understand, clear the window
        clear()
        
        # Tell them they messed up
        print("""
Hmm... I'm not sure I understand your command.
""")


# Goodbye Message
clear()
print("""
Thank you for choosing PasswordBank!
Press enter to quit!""")

# Make sure the user sees the goodbye message :)
stay = input("")