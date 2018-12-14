"""A collection of function for doing my project."""
#important imports that wil come in handy dandy for our chatbox with Isabelle

import string
import random
import nltk

#imports for images
import urllib.request
import random


def my_func():
    pass

def my_other_func():
    pass

#downloads images for you to look at.
## source: https://www.cybrary.it/0p3n/download-image-using-python/?fbclid=IwAR03DSI6P6jyPMs1R20SSC67vdTxaxqy9Odl-QktMoBgR9Dl5_5ARLzUzOM
def downloader(image_url):
    file_name = random.randrange(1,10000)
    full_file_name = str(file_name) + '.jpg'
    urllib.request.urlretrieve(image_url,full_file_name)

def downloader2(image_url):
    file_name = random.randrange(1,10000)
    full_file_name = str(file_name) + '.png'
    urllib.request.urlretrieve(image_url,full_file_name)
    
#code taken/edited from A3 Chatbots

#pick your town name for the game
def town_name(input_string):
    for char in input_string:
        town += char
    
    return town

#choose/enter your name 
def mayor_name(input_string):
    for char in input_string:
        name += char
    
    return name

##Code made for chatting with Isabelle as mayor

#checks if a given input is a question
def is_question(input_string):
    output = ''
    if '?' in input_string:
        output = True
    else:
        output = False
    return output

#after checking to see if our code is a question, we will be removing punctuation to make talking easier
def remove_punctuation(input_string):
    out_string = ''
    for char in input_string:
        if char not in string.punctuation:
            out_string += char
            
    return out_string

#We will now prepare a new function using the previous two, in order to make a text easier, by removing punctuation 
#after finding out if it is a question, and making the statement lowercase, and split the string into words and return a
#a list of strings. This will make it easier to find key words for our chat bot to have a wider range of responses. 

def prepare_text(input):
    temp_string = input.lower()
    temp_string = remove_punctuation(temp_string)
    out_list = temp_string.split()
    
    return out_list
 

#now we will use a function to help create our responses. It will scan for inputs from the list it gets, and if a certain word appaears in that input list we can create an output list.
def selector(input_list, check_list, return_list):

    output = None
    for word in input_list:
        if word in check_list:
            output = random.choice(return_list)
            break

    return output

#concatenating two strings 
def string_concatenator(string1, string2, separator):
    
    result = string1 + separator + string2
    
    return result

#converts list of strings into one string
def list_to_string(input_list, separator):
    
    output = input_list[0]
    for item in input_list[1:]:
        output = string_concatenator(output, item, separator)
        
    return output

#end the chat entirely
def end_chat(input_list):
    
    if 'bye' in input_list:
        output = True
    else:
        output = False
        
    return output



GREETINGS_IN = ['hi', 'hello',"what's up buttercup",'hiya', 'howdy','hey','hi there','hola','bonjour',]
GREETINGS_OUT = ["Hi! My name is Isabelle. I am your personal assistant to help you with your town or with anything you may need.", "Hi, my name is Isabelle, I'm the town's personal liason, what can I do for you?", "Hi! I'm Isabelle, can I help you with anything?"]

TOWN_IN = ['town', 'mayor', 'city hall', 'public works', 'help','where','job, ''live']
TOWN_OUT = ["Ah yes, this is such a wonderful town, isn't it! After all, it's yours!", \
            "You're the mayor of this town! Congratulations!", \
            "We're standing in city hall! Isn't that neat?", \
            "There's a list of public works projects inside, but we can't start those yet", \
            "Yes, what can I assist you with?", \
            "Where are you? We're in your town silly!", \
            "Your job is to be mayor and help the people of this town!", \
            "Your house is located at the end of the river!"]

PLACES_IN = ['Shampoodle', 'Museum', "Nook's Homes", "Post Office", 'Able Sisters', 'Photo Booth', 'Kicks']
PLACES_OUT = ["Shampoodle is where you can go to get your hair and eyes done! It's on main street", \
            "The Museum is where you can donate and display your findings of your town!", \
            "Nook's Homes is where you can buy and build on your home!", \
            "The post office is where you can send letters and pay off your loans!", \
            "The Able sisters is where you can buy and eventually design clothing ", \
            "The Photo Booth is where you can go to get a new ID card and take pictures with friends ", \
            "Kicks is down the street where you can buy new kicks hehe"]
TODO_IN = ['What is there to do?', "activities", 'games', 'fun', 'to do', 'bored']
TODO_OUT = ["You can go fishing!", "You can go visit the islands!", "You can go shop!", "You can play games on the island!", "you can dig up new fossils!", "you can sell fruits!", "you can start a new project!", "Go make friends!"]

JOKES_IN = ['joke', 'funny', 'lol', 'ahaha', 'hahaha', 'ha', 'lol','lmao']
JOKES_OUT = ['ha', 'ahah', 'lol'] 

NONO_IN = ['school','computer science', 'cogs18','coding','computers']
NONO_OUT = ["I'm sorry, I don't want to talk about that"]

UNKNOWN = ['What?', 'Okays!', "Can you try again?, I didn't get that!"]

QUESTION = "I'm sorry, but I don't have an answer to your question ;;"


#Our official full on chatbox
def talk_to_isabelle():
    
    chat = True
    while chat:

        # Begin to talk to the user and get their input
        msg = input('Begin :\t')
        out_msg = None

        # Check if user's input is a question
        question = is_question(msg)

        # prepare the input message after deciding if it's a question or not
        msg = prepare_text(msg)

        # Check for an end msg 
        if end_chat(msg):
            out_msg = 'Goodbye! It was nice talking to you!'
            chat = False
                 
        
        #The code will now go through and look through the wide range of topics we have selected to speak about
        #The topics are limited to your town in animal crossing, so be somewhat specific!
        if not out_msg:

            # Create an empty string list for possible outputs
            possible_outputs = []

            # If it looks like a greeting, get Isabelle to start talking!
            possible_outputs.append(selector(msg, GREETINGS_IN, GREETINGS_OUT))
           
            # Check if it looks like it's about your town, run this
            if question:
                possible_outputs.append(selector(msg, TOWN_IN, TOWN_OUT))   

            # If you're bored and want something to do, run this!
            possible_outputs.append(selector(msg, TODO_IN, TODO_OUT))
   
           # Check if the input talks about places in town and give more information
            possible_outputs.append(selector(msg, PLACES_IN, PLACES_OUT))


            # If you wanna make a joke with Isabelle, this is what you should use!
            possible_outputs.append(respond_echo(selector(msg, JOKES_IN, JOKES_OUT), 3, ''))

            # If you don't want to talk about something, use this
            if is_in_list(msg, NONO_IN):
                possible_outputs.append(list_to_string([selector(msg, NONO_IN, NONO_OUT), find_in_list(msg, NONO_IN)], ' '))

            # IF YOU WANTED TO ADD MORE TOPICS TO RESPOND TO, YOU COULD ADD THEM IN HERE

            # We could have selected multiple outputs from the topic search above (if multiple return possible outputs)
            #   We also might have appended None in some cases, meaning we don't have a reply
            #   To deal with this, we are going to randomly select an output from the set of outputs that are not None
            options = list(filter(None, outs))
            if options:
                out_msg = "I'm sorry, I have no knowledge of that information. Please try again"

        # If we don't have a listed output, but the input was a question, return that you don't know what it's asking.
        if not out_msg and question:
            out_msg = QUESTION

        # If Isabelle can't understand what you're saying :'( (remember, keep it game related!)
        if not out_msg:
            out_msg = random.choice(UNKNOWN)

        print('OUTPUT:', out_msg)
