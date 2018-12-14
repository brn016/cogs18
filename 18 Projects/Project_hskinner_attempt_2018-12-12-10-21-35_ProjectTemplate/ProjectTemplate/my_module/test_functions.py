"""Test for my functions.
"""
import random

from functions import *
from dictionaries import *

def test_remember_punc():

    assert isinstance(remember_punc('hello.'), str)
    assert remember_punc ('hello.') == '.'
    assert isinstance(remember_punc('hello'), str)
    assert remember_punc ('hello') == ''


def test_choose_num():
    
    assert isinstance(choose_num(0,3), str)
    assert choose_num(0,3) == '0' or '1' or '2' or '3'
    

def test_replace_words():
    
    test_genre = { 
        'plural_noun' : ['plural_noun1', 'plural_noun2'], 
        'noun' : ['noun1', 'noun2'],
        'adjective' : ['adjective1', 'adjective2'],
        'name' : ['name1', 'name2'],
        'past_verb' : ['past_verb1', 'past_verb2'],
        'verb' : ['verb1', 'verb2'],
        'adverb': ['adverb1', 'adverb2'],
        'location': ['location1', 'location2']}
    
    test_string = 'hello /name!'
    
    assert isinstance(replace_words(test_string,test_genre), str)
    assert replace_words('/plural_noun', test_genre) == 'plural_noun1' or 'plural_noun2'
    assert replace_words('/noun', test_genre) == 'noun1' or 'noun2'
    assert replace_words('/adjective', test_genre) == 'adjective1' or 'adjective2'
    assert replace_words('/name', test_genre) == 'name1' or 'name2'
    assert replace_words('/past_verb', test_genre) == 'past_verb1' or 'past_verb2'
    assert replace_words('/verb', test_genre) == 'verb1' or 'verb2'
    assert replace_words('/adverb', test_genre) == 'adverb1' or 'adverb2'
    assert replace_words('/location', test_genre) == 'location1' or 'location2'
    assert replace_words('/number', test_genre) == '0' or '1' or '2' or '3'


def test_remember_ends():
    
    assert isinstance(remember_ends('hello!'), str)
    assert remember_ends('hello!') == '!'
    assert remember_ends('hello.') == '.'
    assert remember_ends('hello?') == '?'
    assert remember_ends('hello') == ''
    
    
def test_remove_ends():
    
    assert isinstance(remove_ends('hello!'), str)
    assert isinstance(remove_ends('hello'), str)
    assert remove_ends('hello!') == 'hello'
    assert remove_ends('hello') == 'hello'
    
    
    
def test_cap_sentences():
    
    test_string = 'hi. glad to hear'
    
    assert isinstance(cap_sentences('.',test_string), str)
    assert cap_sentences('.', test_string) == 'Hi. Glad to hear'
    
    

def test_fix_all_caps():
    
    test_string = 'hi. um, HELLO? swell! goodbye.'
    
    assert isinstance(fix_all_caps(test_string), str)
    assert fix_all_caps(test_string) == 'Hi. Um, HELLO? Swell! Goodbye.'
    
    
    
def test_madlib():
   
    test_string1 = '/name1 is a /adjective1 /noun1 from /location1.'
    test_string2 = '/number1 /plural_noun1 will /verb1 after they /past_verb1!'
    test_string3 = 'Are you /adjective1 for the /noun1?'
    
    output1 = madlib(test_string1, fantasy)
    output2 = madlib(test_string2, animal)
    output3 = madlib(test_string3, UCSD)
    
    assert isinstance (output1, str)
    assert isinstance (output2, str)
    assert isinstance (output3, str)
      
    assert output1[0].isupper
    assert output2[0].isupper
    assert output3[0].isupper
    
    assert output1[-1] == '.'
    assert output2 [-1] == '!'
    assert output3 [-1] == '?'
    
    for item in output1[0:-1].split():
        assert item in fantasy or test_string1
         
    for item in output2[0:-1].split():
        assert item in animal or test_string2
    
    for item in output3[0:-1].split():
        assert item in UCSD or test_string3