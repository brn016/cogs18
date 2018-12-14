#########################################
#  These functions were provided in A3
#########################################

def is_question(input_string):
    for char in input_string:
        if char == '?':
            output = True
        else: 
            output = False
    return output

#removes all punctuation from the input string

def remove_punctuation(input_string):
    out_string= ''
    for word in input_string:
        if not word in string.punctuation:
            out_string += word
    return out_string

#creates list from words in input_string

def prepare_text(input_string):
    temp_string = str.lower(input_string)
    temp_string = remove_punctuation(temp_string)
    out_list = temp_string.split()
    return out_list

#use random.choice to choose from several output/responses

#this was edited to return a specified output instead of a random choice of a list
def selector(input_list, check_list, attribute):
    output = None
    for char in input_list:
        if char in check_list:
            output = attribute
            break
    return output
    

def list_to_string(input_list, separator):
    output = input_list[0]
    for word in input_list[1:]:
        output = string_concatenator(output,word,separator)
    return output

def string_concatenator(string1, string2, separator):
    output = string1 + separator + string2
    return output

#this was edited a bit to include more options
def end_chat(input_list):

""" Checks is user says keywords that signify that they are done talking."""

    if 'quit' in input_list or 'done' in input_list or 'bye' in input_list:
        return True
    else:
        return False
def is_in_list(list_one, list_two):
    """Check if any element of list_one is in list_two."""
    
    for element in list_one:
        if element in list_two:
            return True
    return False

def find_in_list(list_one, list_two):
    """Find and return an element from list_one that is in list_two, or None otherwise."""
    
    for element in list_one:
        if element in list_two:
            return element
    return None

###############################
# These functions were created
###############################

#check is user is mentioned another category of mammal
def switch_chat(input_list, animal):
    
    """ Checks if the user mentions another animal category than the one currently on"""

    MAIN_ANIMALS = ['mammal', 'mammals', 'fish', 'bird', 'birds', 'insect', 'insects']

    for word in input_list:
        
        if word in MAIN_ANIMALS and word != animal:
            
            ask = input('Would you like to return to the main menu? [Y/N] ') #Double checks and asks if the 
            ask = remove_punctuation(ask.lower())
            
            if ask == 'y' or ask == 'yes':
                
                animal_chat() #restart from the main menu
                
#compares migration distances of an animal category and returns either longest or shortest
def compare_distance(animal_category, comparison):
    
    """Compares migration distance attribute between all animals in a category if user says the keywords for comparing."""
    
    lowest=animal_category[0]
    highest = lowest
        
    for animal in animal_category:
            
        if int(animal.migration_distance) < int(lowest_migration_distance):
                
            lowest = animal
            
        elif int(animal.migration_distance) > int(highest.migration_distance):
                
            highest = animal
        
    if comparison == 'longest' or comparison == 'furthest':
            
        output = highest
        
    elif comparison == 'shortest':
            
        output = lowest
        
    output = remove_punctuation(str(output))
        
    return output