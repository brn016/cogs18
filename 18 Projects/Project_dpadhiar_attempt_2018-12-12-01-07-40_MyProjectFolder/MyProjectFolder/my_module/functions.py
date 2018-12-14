"""A collection of functions used within project."""

import string

def encrypt_choice(user_input):
    """Determines if user will be decoding or encoding message.
    
    Parameters
    
    ----------
    
    user_input: string
        
        String identifying the choice of the user
        
    Return
    
    ------
    
    bool
    
        True if encoding, false if not

    """
    # If input is e or E, this means our program will focus on encoding
    if(user_input == 'e'):
        return True
    
    elif(user_input == 'E'):
        return True
    
    # If input didn't match either case we will decode for this program
    else:
        return False

def dict_create(encrypt, key):
    """Creates a dictionary that will be used as the key for
       encoding the input of the user.
       
    Parameters
    
    ----------
    
    encrypt : boolean
    
        Boolean that identifies if message will encoded or not
        
    key : integer
    
        Key used in algorithm for creating dictionary
        
    Return
    
    ------
    
    dictionary
        
        Returns dictionary used to encode/decode messages
       
    """

    # This alphabet list will be helpful in constructing the dict
    alphabet = list(string.ascii_lowercase)

    # Empty dictionary to be filled
    encrypt_dict = {}
    
    # Looks over every element as this is necessary for en/decoding
    for i in range(len(alphabet)):
    
        # Uses boolean from prev method to continue encoding logic
        if(encrypt == True):
            
            # Uses the key to know how many letters over it will be
            # Mod 26 is utilized to keep us in range
            encrypt_dict[alphabet[i]] = alphabet[(i + key)%26]
        
        else:
            
            # If decoding, key is subtracted from index
            encrypt_dict[alphabet[i]] = alphabet[(i - key)%26]
        
    # Returns dictionary that has been constructed    
    return encrypt_dict

def encrypt_string(message, encrypt_dict):
    """Encodes or decodes message passed using dictionary as a key
    
    Parameters
    
    ----------
    
    message: string
    
        String that will be encoded or decoded
        
    encrypt_dict: dictionary
    
        Key used to encode or decode message
        
    Return
    
    ------
    
    string
    
        Message after it has been encoded or decoded
    
    """
    
    # Empty string that will build encrypted message string
    encrypted = ''
    
    # Iterates through every char as every letter must be changed
    for item in message:
        
        # Preserves capitals throughout the encryption
        if(item.isupper() == True):
            
            # Sets it to lowercase to match with dictionary
            lower_item = item.lower()
            
            # Asserts that item is still in dict
            if lower_item in encrypt_dict:
                
                # Adds item to encoded to build string
                encrypted = encrypted + encrypt_dict[lower_item].upper()
                
        else:
                
            # Asserts that lowercase items are in dict
            if item in encrypt_dict:
                encrypted = encrypted + encrypt_dict[item]
                    
            # All other items like ints or punctuation preserved
            else:
                encrypted = encrypted + item
                    
    return encrypted
