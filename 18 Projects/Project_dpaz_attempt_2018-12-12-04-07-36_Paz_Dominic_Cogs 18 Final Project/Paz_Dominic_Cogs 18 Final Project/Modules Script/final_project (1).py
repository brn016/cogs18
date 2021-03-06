# -*- coding: utf-8 -*-
"""Final Project

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MXTu53J2zSscF1YtzZml61Lz_ahyTtRA
"""

import random #for random shuffle
import os #for pause below
def pause():
    programPause = input("Press the <ENTER> key to begin the experiment")
    
def Trials_test(): 
  """runs a trials based experiment in three loops. 
    
    No parameters required, info is collected on input
    ----------
    Part 1: Collects basic user info such as intials, gender, and age
    Part 2: Prints experiment prompt and how to enter answers
    Part 3: runs the actual experiment in 3 loops.
    Note: Three lists are created to perform operations temp_type, response, and
    correct. These encode hot and cold as 1 and 2, which is compared to hot and 
    cold response 1 Hot and 2 cold, and 0 if anything else. If both are equal 
    then correct has a 1 appended to it, otherwise its a 0
    All three loops function simulatanously. Specific info can be found in 
    individual comments around the loop and process. 
    Given this experiment is confined to one function, the test file will have
    all this code in script form, and the asserts in a separate cell like how
    assignments were checked in Jupiter. 
    
    
    Returns
    -------
    A unique message will appear giving user instant feedback on their accuracy
    While primative at its core, this function is a basic/lower division level
    experiment with the keyboard. Advanced implementation could include reaction
    times and integration with screen flipping in psycho-py
    """
  subject_init=input('Enter your first and last intials here: ')
  
  subject_gender=input('Enter M for male, F for female: ')
  
  subject_age=input('Enter your age: ')
  
  print('')


  print('Greetings', subject_init , ',this experiment is an example')
  print("of a a basic trials structure that would be integrated with PsychoPy.")
  print('')
  print('In this task you will asked to press a specific key when the word HOT or')
  print('COLD appears on the screen.')
  print('Press the x key followed by ENTER when cold appears')
  print('Press the z key followed by ENTER when hot appears,')
  pause()
  print('')
  trials=['hot', 'cold','hot','hot','hot','hot','hot','hot','hot','hot','hot','cold','cold','cold','cold','cold','cold','cold','cold','cold']
  temp_type=[]
  response=[]
  correct=[]
  random.shuffle(trials)
  
  for temperature in trials: 
     if temperature == 'hot':
      temp_type.append(1) #codes the number 1 as hot, 2 as cold
     else:
      temp_type.append(2)
#print(temp_type) checking to see if it looked right
  
  for i in trials:
    print(i)
    user_response=input()
    if user_response=='z': #if the user pressed z, its coded as 1
        response.append(1)
    elif user_response=='x': #if the user pressed x, 
        response.append(2)
    else:
      response.append(0)
#print(response) this was a step to check the comparsion lists were working
  
  for x, y in zip(temp_type, response):
    if x==y:
      correct.append(1)
    else:
      correct.append(0)
#print(correct) another check to see if lists looked right
 
  num_correct=correct.count(1)
  if num_correct==20:
    print('Excellent, you got a perfect score!')
  elif num_correct >= 12:
    print('Nice Work! You scored', num_correct, 'out of 20.')
  elif num_correct < 12: 
    print('Good try, you scored', num_correct, 'out of 20. Try again?')
  else: 
    print('We did not get a score from you, please try again')

#when the experiment is in script form, the following asserts can be used to
#test the code
#assert len(trials)==20
#assert isinstance(subject_init, str)
#assert isinstance(subject_gender, str)
#assert isinstance(subject_age, str)
#assert len(temp_type==20)
#assert len(correct==20)
#assert len(user_response==20)

Trials_test()