"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""
import string
import random
import nltk

from functions import is_question, remove_punctuation, prepare_text, respond_echo, selector, string_concatenator, list_to_string, end_chat

##
##  
def is_question(input_string):
    assert is_question('hey')==False
    assert is_question('hey?')==True
    
def remove_punctuation(input_string):
    assert remove_punctuation("Hey! It's me!") == "Hey Its me"
    
def prepare_text(input_string):
    assert isinstance(prepare_text('One two three.'), list)
    assert prepare_text('Hi! Also, howdy.') == ['hi', 'also', 'howdy']
    
def respond_echo(input_string):
    assert isinstance(respond_echo('ha', 2, ' '), str)
    assert respond_echo('meow', 3, '~') == 'meow~meow~meow~'
    assert respond_echo(None, 2, '') == None
    
    
def selector(input_list, check_list, return_list):
    assert selector(['in', 'words'], ['words'], ['yes']) == 'yes'
    assert selector(['in', 'words'], ['out'], ['yes']) == None
    
def string_concatenator(string1, string2, separator):
    assert isinstance(string_concatenator('hello', 'world', ' '), str)
    assert string_concatenator('hello', 'world', ' ') == 'hello world'
    
    
def list_to_string(input_list, separator):
    assert isinstance(list_to_string(['a', 'b'], '|'), str)
    assert list_to_string(['a', 'b'], '|') == 'a|b'

def end_chat(input_list):
    assert isinstance(end_chat(['a', 'b']), bool)
    assert end_chat(['quit']) == True
    