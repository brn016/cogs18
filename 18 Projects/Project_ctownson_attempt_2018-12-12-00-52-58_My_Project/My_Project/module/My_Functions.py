#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""A collection of functions for doing my project."""


# In[ ]:


import string
import random


# In[ ]:


def remove_punctuation(input_string):
    """Removes punctuation from the input string so Bot-any can read it better. This is from the assignment."""
    out_string=''
    
    
    for item in input_string:
        
        if item in string.punctuation:
            continue
            
        else: out_string+=item
            
            
    return out_string


# In[ ]:


def selector(input_list,check_list, return_list):
    """Checks if an item in the first list is in another list and then returns a random item from a 
    third list if so. This is from the assignment."""
    
    output=None
    
    
    for item in input_list:
        if item in check_list:
            output=random.choice(return_list)
            break
            
            
    return output


# In[ ]:


def sunlight_question(input_list):
    """This determines if the user is asking about sunlight and then finds the amount of sunlight that particular 
    plant needs in the corresponding dictionary. If someone just says 'sunlight', it will request specifics."""

    
    output=None
    
    
    if is_in_list(input_list, SUNLIGHT) and is_in_list(input_list, PLANTS_IN):
        
        plant= find_in_list(input_list, PLANTS_IN)
        output=list_to_string([plant.capitalize(), "plants", "need", sunlight_dict[plant],"sunlight."]," ")
        
    if is_in_list(input_list, SUNLIGHT) and not is_in_list(input_list, PLANTS_IN):
        
        output= "All plants need a specific amount and type of sunlight. Please specify which plant!"
        
        
    return output


# In[ ]:


def water_question(input_list):
    """This determines if the user is asking about water usages and then finds the amount of water that 
    particular plant needs in the corresponding dictionary. If someone just says 'water', it will request specifics."""
    output=None
    
    if is_in_list(input_list, WATER) and is_in_list(input_list, PLANTS_IN):
        
        plant=find_in_list(input_list, PLANTS_IN)
        output=list_to_string([plant.capitalize(),"plants", "need to be watered", water_dict[plant]]," ")
        
    if is_in_list(input_list, WATER) and not is_in_list(input_list, PLANTS_IN):
        
        output= "All plants need a specific amount of water. Please specify which plant!"
        
        
    return output


# In[ ]:


def soil_question(input_list):
    """This determines if the user is asking about soil type and then finds the type of soil that particular 
    plant needs in the corresponding dictionary. If someone just says 'soil', it will request specifics."""
    
    output=None
    
    if is_in_list(input_list, SOIL) and is_in_list(input_list, PLANTS_IN):
        
        plant= find_in_list(input_list, PLANTS_IN)
        output=list_to_string([plant.capitalize(),"plants","need", soil_dict[plant]]," ")
        
    if is_in_list(input_list, SOIL) and not is_in_list(input_list, PLANTS_IN):
        
        output= "All plants need a specific type of soil. Please specify which plant!"
        
    return output


# In[1]:


def value_question(input_list):
    """This determines if the user is asking for some type of 'value question', i.e. what is the best ___, what is a 
    cheapest ___ and then. She responds."""
    
    output= None
    
    #Determines if input is about 'goodness' and then responds using the dictionary
    if is_in_list(input_list, GOOD_TERMS) and is_in_list(input_list, PLANTS_IN):
        
        type_of_plant= find_in_list(input_list, PLANTS_IN)
        specific_plant=good_dict[type_of_plant]
        output= list_to_string([specific_plant,"are the best", type_of_plant,"in my opinion.","They love", sunlight_dict[type_of_plant],
                              "sunlight and water", water_dict[type_of_plant]]," ")
    
    #determines if input is about 'cheapness' and then responds using the corresponding dictionary
    if is_in_list(input_list, CHEAP_TERMS) and is_in_list(input_list, PLANTS_IN):
        
        type_of_plant= find_in_list(input_list, PLANTS_IN)
        output= list_to_string([cheap_dict[type_of_plant],"are the cheapest", type_of_plant]," ")
    
    #literally just answers the question 'easiest plant'
    if "plant" in (input_list) and is_in_list(input_list, EASY_TERMS):
        output= "Succulents are the easiest plants."
        
        
    return output


# In[ ]:


def prepare_text(input_string):
    """This prepares the text to be read by my chatbot. This is from the assignment."""
    #lower case
    lower_string=input_string.lower()
    
    #removes punctuation
    lower_string=remove_punctuation(lower_string)
    
    #splits items in the string into a list
    out_list=lower_string.split()
    
    return out_list


# In[ ]:


def end_chat(input_list):
    """This quits the chat. This is from the assignment."""
    
    if "bye" in input_list:
        
        return True
    
    else: return False


# In[ ]:


def string_concatenator(string1, string2,separator):
    """This concatenates the strings that Bot-any says. This is from the assignment."""
    output=None
    
    output=string1+separator+string2
    
    return output


# In[ ]:


def list_to_string(input_list,separator):
    """ This turns a list of items into a string. This is from the assignment."""
    output=input_list[0]
    
    
    for item in input_list[1:]:
        output=string_concatenator(output,item,separator)
        
        
    return output


# In[ ]:


def is_in_list(list_one, list_two):
    """Check if any element of list_one is in list_two. This is from the assignment."""
    
    for element in list_one:
        if element in list_two:
            return True
    return False

def find_in_list(list_one, list_two):
    """Find and return an element from list_one that is in list_two, or None otherwise. This is from the assignment."""
    
    for element in list_one:
        if element in list_two:
            return element
    return None


# In[ ]:


def introduction():
    """Literally all this does is give the instructions. But it is a function TECHNICALLY."""
    
    print("Welcome! Ask me anything about houseplants! I know a lot about cacti, ferns, succulents, orchids and bonsai.")


# In[ ]:


def have_a_chat():
    """Main function to run our chatbot."""

    chat = True
    while chat:

        # Get a message from the user
        msg = input('CUSTOMER :\t')
        out_msg = None

        # Prepare the input message
        msg = prepare_text(msg)

        # Check for an end msg 
        if end_chat(msg):
            out_msg = 'Bye! Come back soon.'
            chat = False
# Check for the questions we have designed Bot-any to respond to.
        #   Here, we will check for a series of topics that we have designed to answer to
        if not out_msg:

            # Initialize to collect a list of possible outputs
            outs = []

            # Check if the input looks like a greeting, add a greeting output if so
            outs.append(selector(msg, GREETINGS_IN, GREETINGS_OUT))
            
            # Check if the input looks like a thank you and add a "you're welcome" equivolent response
            outs.append(selector(msg, THANKS_IN, THANKS_OUT))
              #Check if the input mentions sunlight and a plant
                #if so respond with the corresponding value from the sunlight dictionary
            outs.append(sunlight_question(msg))
                
                
            #Check if the input message mentions water and a plant 
            #if so respond with the corresponding value from the water dictionary
            outs.append(water_question(msg))
                
            #Check if the input message mentions soil type and a plant 
            #if so respond with the corresponding value from the soil dictionary
            outs.append(soil_question(msg))
            
            #returns value assessments from the dictionary
            outs.append(value_question(msg))
                
            #Gives a fun fact about plants
            if is_in_list(msg, RANDOM_IN):
                out_msg=random.choice(RANDOM_OUT)

            # We could have selected multiple outputs from the topic search above (if multiple return possible outputs)
            #   We also might have appended None in some cases, meaning we don't have a reply
            #   To deal with this, we are going to randomly select an output from the set of outputs that are not None
            options = list(filter(None, outs))
            if options:
                out_msg = random.choice(options)

    

        # Catch-all to say something if msg not caught & processed so far
        if not out_msg:
            out_msg = random.choice(UNKNOWN)

        print('BOT-any:', out_msg)


# In[ ]:


GREETINGS_IN = ['hello', 'hi', 'hey', 'hola', 'welcome', 'bonjour', 'greetings','howdy']
GREETINGS_OUT = ["Nice to meet you! To begin, ask me anything about houseplants!", 
                 "Hi! Ask me anything about houseplants, or say 'random fact' to get a random fact!", 
                 "Hello! Ask me anything about houseplants."]

CHEAP_TERMS= ["cheap","cheaper","cheapest"]
GOOD_TERMS= ["good", "best"]
EASY_TERMS= ["easy", "easiest"]
                
WATER= ["water", "h2o"]
SUNLIGHT= ["sunlight", "sun"]
SOIL= ["soil","dirt"]

THANKS_IN = ["thank", "thanks", "thx"]
THANKS_OUT = ["No problem!", "Any time!", "You're welcome!"]

PLANTS_IN = ["cactus", "succulent", "fern", "orchid", "bonsai"]


UNKNOWN = ["What do you mean?", 'Okay', 'Huh?', 'Could you repeat that?', 'Check your spelling?']

RANDOM_IN= ["random"]
RANDOM_OUT=["The Earth has more than 80,000 species of edible plants!","90% of the foods humans eat come from just 30 plants!",
            "Vanilla flavoring comes from the pod of an orchid, Vanilla planifolia!","The Amazon rainforest produces half the world’s oxygen supply!",
           "The strawberry is the only fruit that bears its seeds on the outside"]


# In[ ]:


"""These dictionaries hold all the information for the functions above."""


sunlight_dict={"cactus":"indirect, filtered","succulent":"indirect, filtered", "fern":"partial to little", 
               "orchid":"high, bright","bonsai":"bright, direct"}

water_dict= {"cactus": "once a week, or when topsoil is dry.","succulent":"at least once a week.",
             "fern":"before the soil dries, but don't let them get soggy!","orchid": "every 5 to 6 days.",
             "bonsai":"whenever the soil feels slightly dry."}

soil_dict={"cactus":"soil with good drainage, such as cactus potting soil.","succulent":
           "sand mixed with potting soil.", "fern":"porous, organic soil",
           "orchid":"2 parts bark and 1 part peat moss.",
           "bonsai":"a mixture of 2 parts akadama, one part pumice and one part lava rock."}

good_dict={"cactus":"Echinocacti","succulent":"Burro tails","fern":'Ghost ferns','orchid':'Boat orchids',"bonsai":
           "Ficus bonsais"}

cheap_dict={"cactus":"Air plants","succulent":"Rosette succulents", "fern":"Boston ferns", "orchid":
            "White orchids", "bonsai":"Juniper bonsais"}

