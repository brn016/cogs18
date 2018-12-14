import string
from my_module.custom import *


# Checks if input is a question - External Code (A3)
def is_question (input_string):
    output = False 
    if '?' in input_string:
        output = True 
    else: 
        ouput = False
    return output 

# Removes punctuation from input string - External Code (A3)
def remove_punctuation (input_string):
    out_string = ''
    for x in input_string: 
        if x not in string.punctuation:
            out_string = out_string + x
    return out_string 

#Prepares text inputs for Chatbot to process - External Code (A3)
def prepare_text(input_string):
    temp_string = input_string.lower()
    temp_string = remove_punctuation(temp_string)
    out_list = temp_string.split()
    return out_list

#Select an output for the chatbot, based on the input it got - External Code (A3)
def selector(input_list, check_list, return_list):
    output = None 
    for x in input_list: 
        if x in check_list: 
            output = random.choice(return_list)
            break 
    return output

# will concatenate two strings, combining them with a specified separator. - External Code (A3)
def string_concatenator (string1, string2, separator):
    output = string1 + separator + string2 
    return output

# return a string that is each element of input_list concatenated together with each separated by the string seperator
# External Code (A3)
def list_to_string(input_list, separator):
    output = input_list[0]
    
    for x in input_list[1:]: 
        output = string_concatenator(output, x, separator)
    return output

#End chat with Chatbot using "i am awesome" - External Code (A3)
def end_chat (input_list):
    output = False 
    if 'awesome' in input_list: 
        output = True 
    else: 
        output =  False 
    return output

#Check if any element of list_one is in list_two - External Code (A3)
def is_in_list(list_one, list_two):
    for element in list_one:
        if element in list_two:
            return True
    return False

#Find and return an element from list_one that is in list_two, or None otherwise. - External Code (A3)
def find_in_list(list_one, list_two):
    for element in list_one:
        if element in list_two:
            return element
    return None

# External Code - (A3)
GREETINGS_IN = ["hello", "hi", "hey", "hola", "whats up"]
GREETINGS_OUT = ["Hey! What's up?", "How have you been feeling lately?", \
                 "What brings you here?","Woe !- did my monitor just brighten or was that your smile?"]


SAD_IN = ["hopeless", "sad", "depressed", "unhappy", "lonely", "dumb", "idiot", "worthless",\
           "alone", "mad", "upset" ]
INSPO_OUT = ["Never give up!", \
             "Anyone who has never made a mistake has never tried anything new!", \
             "Hitting rock bottom means that you can only go up!", \
             "You're pretty special, just saying. ", \
             "You are more than capable of accomplishing your dreams.", \
             " You're so cool and fun!" , "I love talking to you!", "You can do all the things!", \
             "I believe in you! Don't give up!"]


NEGATIVE_IN = ["boring", "loser", "suck", "horrible", "stupid"]
NEGATIVE_OUT = ["you're the coolest person i've ever met!", "I bet so many people care about you", \
                "the room lights up as soon as you walk in, you're RADIANT"]
NEGATIVE_SELF = {"boring": "You're not", "loser": "You're not a", "suck": "You don't", "horrible" : "You are't", \
                 "stupid" : "You're not" }

HARM_IN = ["i hate myself", "die", "suicide", "dead", "kill", "fuck"]
HARM_OUT = ["I love you! You matter, you're important, and you are worth fighting for. Please don't give up. ❤", \
           "Here's someone you could talk to about that; Suicide Prevention Lifeline(24/7): Call 1-800-273-8255", \
           "Please don't say that/:", "I believe in you! Don't give up!", \
           "The room lights up as soon as you walk in, you're RADIANT. Thank you for existing. ❤", \
           "Hitting rock bottom means that you can only go up! You're worth the struggle to the top."]

UNKNOWN = ["Woops! I didn't quiet get that. ", \
           'How about we talk about something else?(: ',\
           "Don't worry you can talk to me(:",\
           "Here's a drawing I made of me giving you all the affirmations: ◟(＾◡＾)◞♥◟(◕◡◕)◞", \
           "Did you say you're the most amazing person ever?! Because its true!!", \
           "Huh? Sorry, I was distracted by how cool you are"]

QUESTION = "Sorry I can't answer questions. But a walk might help you clear your mind to find a solution. (:"



# the follwing code is External code from Assignment 3 with some unique code/modifications 
# Main function to run affirmation_chatbot()

def affirmation_chatbot():
    
    # Prints the intro to Affirmation Chatbot
    print("""\t\t Hello Sunshine! Welcome to Affirmation Chatbot! \n 
        Please Read the following line out loud to continue: 'I love myself' \n 
        \t....Tricked you! I can't hear anything you say haha.\n 
        One way to feel good about yourself is to LOVE yourself... to take care of yourself' - G.H.
        -------------------------------------------------------------------------------------------------------------
        - To talk with Affirmation Chatbot: use plain english with either upper/lower case letters and punctuation
        - To end the chat, enter: awesome""")
    
    # Displays positive image with words 
    display(Image("img/Starshine.jpg"))
    
    #External Code 
    chat = True
    while chat:

        # Gets a message from the user - External 
        msg = input('Cool Person input :\t')
        out_msg = None

        # Check if the input is a question - External 
        question = is_question(msg)

        # Prepare the input message - External 
        msg = prepare_text(msg)
        
        

        # Check for an end msg - External 
        if end_chat(msg):
            out_msg = 'Heck yea you are! Thanks for chatting <3'
            either_pic()
            chat = False

        # Check for a selection of topics that we have defined to respond to - External 
        if not out_msg:

            # Collects a list of possible outputs - External 
            outs = []

            # Check if the input looks like a greeting, and adds a greeting output - External 
            outs.append(selector(msg, GREETINGS_IN, GREETINGS_OUT))
           

            # Check if the input looks like a sad thing, add a inspirational output and positive picture - External 
            if is_in_list(msg, SAD_IN):
                outs.append(selector(msg, SAD_IN, INSPO_OUT))
                pos_pic()
            
            # Check if the input mentions a negative trait about themselves, and adds an affirming output to it
            # displays a positive image with words
            #External Code 
            if is_in_list(msg, NEGATIVE_IN):
                affirm = find_in_list(msg, NEGATIVE_IN)
                outs.append(list_to_string([NEGATIVE_SELF[affirm], affirm, selector(msg, NEGATIVE_IN, NEGATIVE_OUT)], ' '))
                word_pic()

            # Check if the input has some harm words and respond with - External 
            if is_in_list(msg, HARM_IN):
                outs.append(selector(msg, HARM_IN, HARM_OUT))
                display(Image("img/Clouds.jpg"))

            
            #   We also might have appended None in some cases, meaning we don't have a reply - External Code 
            #   Randomly selects an output from the set of outputs that are not None
            options = list(filter(None, outs))
            if options:
                out_msg = random.choice(options)

        # If we don't have an output yet, but the input was a question, return msg related to it being a question
        # External Code 
        if not out_msg and question:
            out_msg = QUESTION

        # Catch-all to say something if msg not caught & processed so far - External Code 
        if not out_msg:
            out_msg = random.choice(UNKNOWN)

        print('OUTPUT:', out_msg)