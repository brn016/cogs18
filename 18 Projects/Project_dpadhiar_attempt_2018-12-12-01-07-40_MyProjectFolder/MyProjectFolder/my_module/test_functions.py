""" Test for my functions. """

from functions import encrypt_choice, dict_create, encrypt_string

def test_encrypt_choice():

    assert isinstance(encrypt_choice('e'), bool)
    assert encrypt_choice('d') == False

def test_dict_create():

    assert isinstance(dict_create(True, 200), dict)
    assert dict_create(True,200) == {'a': 's', 'b': 't', 'c': 'u', 'd': 'v', 'e': 'w', 'f': 'x',
                                     'g': 'y', 'h': 'z', 'i': 'a', 'j': 'b', 'k': 'c', 'l': 'd',
                                    'm': 'e', 'n': 'f', 'o': 'g', 'p': 'h', 'q': 'i', 'r': 'j', 
                                    's': 'k', 't': 'l', 'u': 'm', 'v': 'n', 'w': 'o', 'x': 'p',
                                     'y': 'q', 'z': 'r'} 

def test_encrypt_string():

    assert isinstance(encrypt_string('hello', dict_create(True, 200)), str)
    assert encrypt_string('hello', dict_create(True, 200)) == 'zwddg'