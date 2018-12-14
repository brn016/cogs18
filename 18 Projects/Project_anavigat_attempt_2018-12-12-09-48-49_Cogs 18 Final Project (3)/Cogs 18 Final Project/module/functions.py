def my_func():
    pass

def calculate_total_cost(list_of_products):
    
        """
        Given a list of products that you can purchase, this function will calculate the total price of the 
        items that is selected. It does so by initially starting with a total at zero and then working through 
        the products in the list and adding the prices from each product together to return a total.
    
        Parameters
        ----------
        list_of_products : list 
    
        Return
        ----------
        total : int
    
        """
        total = 0 
        for product in list_of_products:
            total += product.price
       
        return total

def check_quantity(list_of_products):
    
    
        """
        Parameters
        ----------
        This function takes in the quantity of a class to determine how many are in stock in the store.
        If the quantity of the product is less than one, then the code will not run.
        
        list_of_products : list
        
        Return
        ----------
        return: None or pass
        """
        for product in list_of_products:

            if product.quantity < 1:
                return None
            else:
                pass

"""
Now that there is a store created I am going to set a chatbot to interact with the store and the customer.
To do so, I will take functions from the chatbot done in Assignment 3.
"""

def is_question(input_string):
    """
    Given an input string the following function will see if the string is a question or not by looping through the string to
    see if there is a question mark in the string
    
    Parameters
    ----------
    
    input_string : string
    
    Return
    ---------
    output = boolean
    """
    if '?' in input_string:
        output = True
    else:
        output = False
    
    return output

def remove_punctuation(input_string):
    """
    Next it is important to create a function that will get rid of any punctuation that is given to my chatbot.
    This function takes in any string and removes any punctuation that it recieves.
    
    Parameters
    ----------
    input_string : string
    
    Return
    ----------
    out_string : string
    """
    out_string = ''
    for char in input_string:
        if char not in string.punctuation:
            out_string += char
            
    return out_string

# Now it is time to make some text of our own
def prepare_text(input_string):
    """
    Given an input string, this function will make a new, temporary string that first puts the string in a lower case. Then,
    I wish to remove all punctuation from the temporary string with my function remove_punctuation. Finally I output a new string
    that splits all of the words by using the split method.
    
    Parameters
    ----------
    input_string : string
    
    Return
    ----------
    out_list : list
    
    """
    temp_string = input_string.lower()
    temp_string = remove_punctuation(temp_string)
    out_list = temp_string.split()
    
    return out_list
#I do not need to add echo in my chatbot. I do not think it applies

# Later on I will create a series of posssible input and output lists, where I will need to respond something given a possible 
# input list
def selector(input_list, check_list, return_list):
    """
    Given a possible response from a customer, I need to create a loop that will check every word in my input lists, if a word 
    provided by the customer is said then I will randomly select an answer from my corresponding output list. If there are no
    words that are said in the the input list, then it will break the conditional.
    
    Parameters
    ----------
    input_list : list
    check_list : list
    return_list : list
    
    Return
    ----------
    output : list
    """
    output = None
    for word in input_list:
        if word in check_list:
            output = random.choice(return_list)
            break

    return output

# Now I will to make our response somewhat readable by concatenating strings with a separator.
def string_concatenator(string1, string2, separator):
    """
    The function string concatenator will take strings from our input and make add them together with a seperator in between.
    The seperator will almost always be a space.
    
    Parameters
    ----------
    string1 : string
    string2 : string
    seperator : string
    
    Return
    ----------
    result : string
    """
    result = string1 + separator + string2
    
    return result

#Once we have a determined output list from what the customer wants, we need to respond to the customer in a string, to do that
#I will create a function list_to_string to do so

def list_to_string(input_list, separator):
    """
    Given a list, I first need to first make the output equal to the first element of my input list, which is a string. 
    Then, I will loop through the rest of the items in that list. Finally, I will set the output equal to a concatenated string
    of all the itmes in that list using the previous function = string_concatenator.
    
    Parameters
    ----------
    input_list : list
    separator : list
    
    Return
    ----------
    output : string
    """
    output = input_list[0]
    for item in input_list[1:]:
        output = string_concatenator(output, item, separator)
        
    return output

#Finally, we will create a simple way to end the chat if the customer no longer wants to buy anything.

def end_chat(input_list):
    """
    Given a list from the customer, I want the chat to end if the customer says any of the string below. To do so, I created 
    a function that has a conditional to detect if one of the strings is said. If it is said, then the chat will end. If it 
    is not said, then output will return False and keep going.
    
    Parameters
    ----------
    input_list : list
    
    Return
    ----------
    output = boolean
    """
    if 'goodbye' or "im done shopping" or "thanks for the help" or "quit" in input_list:
        output = True
    else:
        output = False
        
    return output


def is_in_list(list_one, list_two):
    """
    This function loops through all of the elements in list one, and sets up a conditional that ultimitaley finds if the words
    are being said in list two. If it is list the word in list one is in list two it will return True and if not will return 
    False.
    
    Parameters
    ----------
    list_one : list
    list_two : list
    
    Return
    ----------
    function will return a boolean
    """
    
    for element in list_one:
        if element in list_two:
            return True
    return False

def find_in_list(list_one, list_two):
    """
    This function loops through every element in list one, and if it is in list two then it will return the element itself.
    If it does not find the element then it will result in nothing happening.
    
    Parameters
    ----------
    list_one : list
    list_two : list
    
    Return
    ----------
    function will return a boolean
    """
    
    for element in list_one:
        if element in list_two:
            return element
    return None

#Here we are setting up the actual way to chat with the the store.
def have_a_chat():
    """Main function to run our chatbot."""
    
    chat = True
    while chat:

        # Get a message from the user
        msg = input('INPUT :\t')
        out_msg = None

        # Check if the input is a question
        question = is_question(msg)

        # Prepare the input message
        msg = prepare_text(msg)

        # Check for an end msg 
        if end_chat(msg):
            out_msg = 'Bye!'
            chat = False

        # Check for a selection of topics that we have defined to respond to
        #   Here, we will check for a series of topics that we have designed to answer to
        if not out_msg:

            # Initialize to collect a list of possible outputs
            outs = []

            # Check if the input looks like a greeting, add a greeting output if so
            outs.append(selector(msg, GREETINGS_IN, GREETINGS_OUT))
            
            # Check if the input looks like if they are asking if there is any of the products left
            outs.append(selector(msg, PRODUCTS_IN, PRODUCTS_OUT))
            
            # Check if the input looks like if they are asking if they have any microwaves left
            outs.append(selctor(msg, OUT_OF_STOCK_IN, OUT_OF_STOCK_OUT))
            
            #Here I wish to take in a response from the customer and return the name of the product as well as the description
            # for example : "what kind of phone is it" would return the name of the phone with description in the class
            
            #if is_in_list(msg, ASKING_ABOUT_PRODUCT_IN):
                #name = find_in_list(msg, list_of_products)
                #if name = "what kind of phone is it":
                    #my_phone = find_in_list(phone, list_of_products)
                    #outs = my_phone.name + ": " + my_phone.description
                #if name = "what kind of tv is it":
                    #my_tv = find_in_list(tv, list_of_products)
                    #outs = my_tv.name + ": " + my_tv.description
                #if name = "what kind of computer is it":
                    #my_computer = find_in_list(computer, list_of_products)
                    #outs = my_computer.name + ": " + my_comptuer.description
                #if name = "what kind of microwave is it":
                    #my_microwave = find_in_list(microwave, list_of_products)
                    #outs = my_microwave.name + ": " + my_microwave.description
                #if name = "what kind of refrigerator is it":
                    #my_refrigerator = find_in_list(refrigerator, list_of_products)
                    #outs = my_refrigerator.name + ": " + my_refrigerator.description
                
                    
            #   We also might have appended None in some cases, meaning we don't have a reply
            #   To deal with this, we are going to randomly select an output from the set of outputs that are not None
            options = list(filter(None, outs))
            if options:
                out_msg = random.choice(options)

        # If we don't have an output yet, but the input was a question, return msg related to it being a question
        if not out_msg and question:
            out_msg = QUESTION

        # Catch-all to say something if msg not caught & processed so far
        if not out_msg:
            out_msg = UNKNOWN

        print('OUTPUT:', out_msg) 
                
    
