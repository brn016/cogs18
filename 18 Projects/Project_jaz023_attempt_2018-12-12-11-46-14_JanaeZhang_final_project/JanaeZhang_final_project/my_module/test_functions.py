#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""Given that the functions in functions.py are from A3,
the tests included in this file will only test the modified code."""

from functions import prepare_text, end_chat

def test_prepare_text():
    assert callable(prepare_text)
    assert isinstance(prepare_text("This should become a list"), list)
    assert prepare_text("THISSHOULDBECOMELOWERCASE") == ["thisshouldbecomelowercase"]
    assert prepare_text("there should be no spaces") == ["there", "should", "be", "no", "spaces"]
    assert prepare_text("big bear added as one phrase") == ["big", "bear", "added", "as", "one", "phrase", "big bear"]
    
def test_end_chat():
    assert callable(end_chat)
    assert isinstance(end_chat("boolean?"), bool)
    assert end_chat("quit") == True
    assert end_chat("bye") == True
    assert end_chat("goodbye") == True
    assert end_chat("stay") == False

