#!/usr/bin/env python
# coding: utf-8

# In[12]:


"""All of this is code taken from A3.
end_chat has been modified to also recognize 'bye' and 'goodbye'.
prepare_text has been modified so that 'big bear' can be recognized as one phrase"""


#Remove the punctuation of the input
def remove_punctuation(input_string):
    out_string = ""
    for char in input_string:
        if not char in string.punctuation:
            out_string = out_string + char
    return out_string


#Turn the input into a list of single-word strings
import string
def prepare_text(input_string):
    temp_string = input_string.lower()
    temp_string2 = remove_punctuation(temp_string)
    out_list = temp_string2.split()
    if "big" in out_list and "bear" in out_list:
        out_list.append("big bear")
    return out_list


#Determine if the message should end the chat
def end_chat(input_list):
    if "quit" in input_list:
        output = True
    elif "bye" in input_list:
        output = True
    elif "goodbye"  in input_list:
        output = True
    else:
        output = False
    return output


#Check if an element in list_one is in list_two
def is_in_list(list_one, list_two):
    for element in list_one:
        if element in list_two:
            return True
    return False


#Find and return an element from list_one that is in list_two, or None otherwise.
def find_in_list(list_one, list_two):
    for element in list_one:
        if element in list_two:
            return element
    return None

