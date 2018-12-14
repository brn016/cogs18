#!/usr/bin/env python
# coding: utf-8

# In[2]:


from FinalCode import *


# In[3]:


def TestsForEncodingMessages():
    game = Game() # create new game
    msg = 'message to encode' 
    # make list with same size as the message and add key values inside that will be used for encoding
    key_list = [1,2,3] 
    # call the EncodingMessage method and pass in msg and key list 
    encoded = game.EncodingMessage(msg, key_list) 
    # check if the encoding is what you expect it to be
    assert encoded == 'nfttbhf vq hqfrgh' 

    game = Game() # create new game
    msg = 'change me' 
    # make list with same size as the message and add key values inside that will be used for encoding
    key_list = [1,2] 
    # call the EncodingMessage method and pass in msg and key list
    encoded = game.EncodingMessage(msg, key_list)  
    # check if the encoding is what you expect it to be
    assert encoded == 'dibohf og' 


# In[4]:


def TestsForShuffledCypherQuestions():
    game = Game() # create a new game
    original_key_list = [1,2,3,4,5] 
    #shuffle the list of Cypher Questions
    shuffled_list = game.ShuffledCypherQuestions(original_key_list) 
    #check if the length of the shuffled list is the same as the original key list
    assert (len(shuffled_list) == len(original_key_list)) 

    game = Game()
    original_key_list = [1,3,5,2,4]
    shuffled_list = game.ShuffledCypherQuestions(original_key_list)
    assert (len(shuffled_list) == len(original_key_list))


# In[5]:


def TestsForCheckAnswer():
    game = Game()
    original_key_list = [1,2,3,4,5]
    correct_user_response = '12345' 
    #check if the user's response to the questions is correct
    assert(game.checkAnswer(correct_user_response, original_key_list, False) == True)

    game = Game()
    original_key_list = [1,2,3,4,5]
    wrong_user_response = '12346'
    assert(game.checkAnswer(wrong_user_response, original_key_list, False) == False)

    game = Game()
    original_key_list = [1,2,3,4,5]
    wrong_user_response = '12346'
    #raise an error if the user's response to the questions is incorrect
    assert(game.checkAnswer(wrong_user_response, original_key_list, True) == False)


# In[ ]:




