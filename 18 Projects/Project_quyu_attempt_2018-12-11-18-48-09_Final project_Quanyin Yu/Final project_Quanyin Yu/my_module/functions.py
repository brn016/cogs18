import random
import string


def is_question(input_string):
    # Copied from A3
    
    if '?' in input_string:
        output = True
    else:
        output = False

    return output


def prepare_text(input_string):
    """Converts an input string into a list containing strings.
    
    Parameters
    ----------
    input_string : string
        String to convert to a list of string.
        
    Returns
    -------
    out_list : list
        List containing the input string.  
    """
    
    # Converting a string into lower cases
    temp_string = input_string.lower()
    # Spliting up the characters of the string in lower cases
    out_list = temp_string.split()
                
    return out_list


def select(input_list, check_list, return_list):
    # Copied from A3
    
    output = None
    for word in input_list:
        if word in check_list:
            output = random.choice(return_list)
            break

    return output


def respond(input_string, answers):
    """Finding the imput string in the dictionary and return the value 
    
    Parameters
    ----------
    input_string : string
        String to look for as the keys in the dictionary of answers.
    answers : dictionary
        dictionary of answers
        
    Returns
    -------
    output : string
        String containing the value of the keys in the dictionary of answers.  
    """
    
    output = None
    # Checking if the imput string contains the keys in the dictionary of answers 
    for word in input_string:
        if word in answers.keys():
            output = answers[word].get_info()
    
    return output


def end_chat(input_list):
    # Copied from A3
    
    if 'quit' in input_list:
        output = True
    else:
        output = False
        
    return output