"""
This is where all of the user's passwords will be stored.
Passwords will be stored as instances of the Password class, along with the website name and username.
"""

# This is where the Password class is stored
class Password:
    """
    Class for passwords including the website, username, and password
    
    Arguments
    ---------
    site (str) | name of the website
    username (str) | the user's username on the account
    password (str) | the password associated with that account
    """
    
    def __init__(self, site, username, password):
        self.site = site
        self.username = username
        self.password = password

# Gives user an out if they typed in withdraw password and they don't know any website names
quit = Password("quit.com", "quitter", "Iquit@l0t")

# Stored passwords will show up here