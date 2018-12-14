import string      
        
def execute_action(thing, input_string): 
    """ performs commanded user action upon object and avoids nonetype error created by unknown objects not in room inventory
    
    Parameters
    -----------
    thing : object 
            selected by user
    
    input_string : string
            user input
    
    """
    if thing == None:
        print("Try another object in the room. \n")
        
    else:
        thing.take_action(input_string)  ## take_action method found in ThingsInventory class
        

def end_game(input_string):
    """ allows user to end game by typing "quit"
    
    Parameters
    ----------
    
    input_string : string
            user input
    
    """

    if "quit" in input_string:
        output = True
    else:
        output = False
    return output


## makes input all lower case and removes punctuation

def remove_punctuation(input_string):
    """ removes punctuation from user input to make programming easier
        This function was used with permission from Tom Donoghue's A3 Chatbots assignment 
        which can be found here: https://cogs18.github.io/assignments/A3-Chatbots/
    
    Parameters
    ----------
    input_string : string
            user input
    
    Returns
    --------
    out_string : string
            user input without punctuation
    
    """
    out_string = ""
    
    for char in input_string:
        if char not in string.punctuation:
            out_string = out_string + char
    return out_string
    

def prepare_text(input_string):
    """ removes capitalization from user input to make programming easier
        This function was used with permission from Tom Donoghue's A3 Chatbots assignment 
        which can be found here: https://cogs18.github.io/assignments/A3-Chatbots/
    
    Parameters
    ----------
    input_string : string
            user input
    
    Returns
    --------
    out_string : string
            user input in all lowercase
    
    """
    temp_string = input_string.lower()
    temp_string = remove_punctuation(temp_string)
    out_list = temp_string.split()
    
    return out_list
