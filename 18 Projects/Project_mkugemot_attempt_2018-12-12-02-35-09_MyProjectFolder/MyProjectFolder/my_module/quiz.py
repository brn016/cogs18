from psychopy import visual, event, core, gui
import os
import random
import time

#myWin = visual.Window([1280, 720], monitor = 'testMonitor', allowGUI = False, units = 'norm', color = (1,1,1))

"""
This module includes three quizzes: population_quiz, state_quiz, and spot_quiz.
Population_quiz asks the subject to choose which city has the largest population from three choices.
State_quiz asks the subject to choose which state the city is in from three choices.
Spot_quiz asks the subject to choose which city has the sightseeing spot on the screen.
"""

"""
population_quiz: 'Which city has the largest population?'

Parameters
------------
cities: list
    a list of the instances of USACity
wywin
    setting of the window
"""
    
def population_quiz(cities, myWin):
    #randomly select three cities from the list of cities
    cities_list = random.sample(cities, 3)
    city0 = cities_list[0]
    city1 = cities_list[1]
    city2 = cities_list[2]
    
    #make a list of populations of the selected three cities
    population_list = [city0.population, city1.population, city2.population]
        
    #display the question with the multiple choices
    pquiz_text = visual.TextStim(myWin, text = 'Which has the largest population? \n1.' + city0.name +
        '\n2.' + city1.name + '\n3.' + city2.name, color = (-1,-1,-1))
    pquiz_text.draw()
    myWin.flip()
    answer = event.waitKeys(keyList = ['1', '2', '3'])[0]
    
    #if 1 is the correct answer
    if city0.population == max(population_list):
        #if the subject chose the correct answer
        if answer == '1':
            answer_text = visual.TextStim(myWin, text = 'Correct!\n' + city0.name + ' has the largest population, '+
                str(round(city0.population/1000000,2)) + ' million people.\n\n    -Press the space key-', color = (-1,-1,-1))
            answer_text.draw()
            myWin.flip()
            event.waitKeys(keyList = ['space'])
            
        #if the subject chosed the wrong answer, display the correct answer
        else:
            answer_text = visual.TextStim(myWin, text = 'Sorry, incorrect.\n' + city0.name + ' has the largest population, '+
                str(round(city0.population/1000000,2)) + ' million people.\n\n    -Press the space key-', color = (-1,-1,-1))
            answer_text.draw()
            myWin.flip()
            event.waitKeys(keyList = ['space'])
            
    #if 2 is the correct answer
    elif city1.population == max(population_list):
        if answer == '2':
            answer_text = visual.TextStim(myWin, text = 'Correct!\n' + city1.name + ' has the largest population, '+
                str(round(city1.population/1000000, 2)) + ' million people.\n\n    -Press the space key-', color = (-1,-1,-1))
            answer_text.draw()
            myWin.flip()
            event.waitKeys(keyList = ['space'])

        else:
            answer_text = visual.TextStim(myWin, text = 'Sorry, incorrect.\n' + city1.name + ' has the largest population, '+
                str(round(city1.population/1000000,2)) + ' million people.\n\n    -Press the space key-', color = (-1,-1,-1))
            answer_text.draw()
            myWin.flip()
            event.waitKeys(keyList = ['space'])
            
    #if 3 is the correct answer
    elif city2.population == max(population_list):
        if answer == '3':
            answer_text = visual.TextStim(myWin, text = 'Correct!\n' + city2.name + ' has the largest population, '+
                str(round(city2.population/1000000,2)) + ' million people.\n\n    -Press the space key-', color = (-1,-1,-1))
            answer_text.draw()
            myWin.flip()
            event.waitKeys(keyList = ['space'])
            
        else:
            answer_text = visual.TextStim(myWin, text = 'Sorry, incorrect.\n' + city2.name + ' has the largest population, '+
                str(round(city2.population/1000000, 2)) + ' million people.\n\n    -Press the space key-', color = (-1,-1,-1))
            answer_text.draw()
            myWin.flip()
            event.waitKeys(keyList = ['space'])
            
"""
state_quiz: 'Which state has this city?'

Parameters
------------
cities: list
    a list of the instances of USACity
wywin
    setting of the window
"""
def state_quiz(cities,myWin):
    from my_module.function import create_choices
    #randomly select a city on a topic
    target_city = random.choice(cities)
    
    #pass the state of target city to create_choices
    #choice_states store the three options of states for the state quiz
    choice_states = create_choices(target_city.state)
    
    #display the question with three multiple chioces
    squiz_text = visual.TextStim(myWin, text = 'Which state has ' + target_city.name + '? \n1. ' + choice_states[0] +
        '\n2. ' + choice_states[1] + '\n3. ' + choice_states[2], color = (-1, -1, -1))
    squiz_text.draw()
    myWin.flip()
    answer = event.waitKeys(keyList = ['1', '2', '3'])[0]
    
    #if 1(choice_states[0]) is the correct answer
    if choice_states[0] == target_city.state:
        #if the subject chose the correct answer
        if answer == '1':
            answer_text = visual.TextStim(myWin, text = 'Correct!\n' + target_city.name + ' is in ' + target_city.state +
                '.\n\n    -Press the space key-', color = (-1, -1, -1))
            answer_text.draw()
            myWin.flip()
            event.waitKeys(keyList = ['space'])
            
        #if the subject chose the wrong answer, show the correct answer
        else:
            answer_text = visual.TextStim(myWin, text = 'Sorry, incorrect.\n' + target_city.name + ' is in ' + target_city.state +
                '.\n\n    -Press the space key-', color = (-1, -1, -1))
            answer_text.draw()
            myWin.flip()
            event.waitKeys(keyList = ['space'])
            
    #if 2(choice_states[1]) is the correct answer
    elif choice_states[1] == target_city.state:
        if answer == '2':
            answer_text = visual.TextStim(myWin, text = 'Correct!\n' + target_city.name + ' is in ' + target_city.state +
                '.\n\n    -Press the space key-', color = (-1, -1, -1))
            answer_text.draw()
            myWin.flip()
            event.waitKeys(keyList = ['space'])

        else:
            answer_text = visual.TextStim(myWin, text = 'Sorry, incorrect.\n' + target_city.name + ' is in ' + target_city.state + 
                '.\n\n    -Press a space key-', color = (-1, -1, -1))
            answer_text.draw()
            myWin.flip()
            event.waitKeys(keyList = ['space'])
            
    #if 3(chioce_states[2]) is the correct answer
    elif choice_states[2] == target_city.state:
        if answer == '3':
            answer_text = visual.TextStim(myWin, text = 'Correct!\n' + target_city.name + ' is in ' + target_city.state + 
                '.\n\n    -Press a space key-', color = (-1, -1, -1))
            answer_text.draw()
            myWin.flip()
            event.waitKeys(keyList = ['space'])

        else:
            answer_text = visual.TextStim(myWin, text = 'Sorry, incorrect.\n' + target_city.name + ' is in ' + target_city.state +
                '.\n\n    -Press a space key-', color = (-1, -1, -1))
            answer_text.draw()
            myWin.flip()
            event.waitKeys(keyList = ['space'])
            
"""
spot_quiz: 'Which city has this sightseeing spot?'

Parameters
------------
cities: list
    a list of the instances of USACity
wywin
    setting of the window
"""
def spot_quiz(cities, myWin):
    #randomly choose three cities
    cities_list = random.sample(cities, 3)
    #randomly choose a number from 0, 1, 2. The chosen number will be the correct answer.
    target = random.choice([0,1,2])
    
    #display the question
    sptext = visual.TextStim(myWin, text = 'Which city has this sightseeing spot? \n\n    -Press the space key-', color = (-1, -1, -1))
    sptext.draw()
    myWin.flip()
    event.waitKeys(keyList = ['space'])
    
    #display the picture, identify the picture of 'target' in the file 'Spot_pictures' 
    picture = visual.ImageStim(win = myWin, image = 'Spot_pictures/' + cities_list[target].spot + ".jpg", pos = (0,0), units = 'norm')
    picture.draw()
    myWin.flip()
    event.waitKeys(keyList = ['space'])
    
    #display the multiple choices
    sptext2 = visual.TextStim(myWin, text = '\n1. ' + cities_list[0].name + '\n2. '+cities_list[1].name + '\n3. '+cities_list[2].name, color = (-1,-1, -1))
    sptext2.draw()
    myWin.flip()
    answer = event.waitKeys(keyList = ['1','2','3'])[0]
    
    if target == 0:
        if answer == '1':
            answer_text = visual.TextStim(myWin, text = 'Correct!\n' + cities_list[0].spot + ' is in ' + cities_list[0].name +
                '.\n\n    -Press the space key-', color = (-1, -1, -1))
            answer_text.draw() 
            
            myWin.flip()
            event.waitKeys(keyList = ['space'])
        
        else:
            answer_text = visual.TextStim(myWin, text = 'Sorry, incorrect.\n' + cities_list[0].spot + ' is in ' + cities_list[0].name +
                '.\n\n    -Press the space key-', color = (-1, -1, -1))
            answer_text.draw()
            myWin.flip()
            event.waitKeys(keyList = ['space'])
            
    elif target == 1:
        if answer == '2':
            answer_text = visual.TextStim(myWin, text = 'Correct!\n' + cities_list[1].spot + ' is in ' + cities_list[1].name +
                '.\n\n    -press the space key-', color = (-1, -1, -1))
            answer_text.draw()
            myWin.flip()
            event.waitKeys(keyList = ['space'])
        
        else:
            answer_text = visual.TextStim(myWin, text = 'Sorry, incorrect.\n' + cities_list[1].spot + ' is in ' + cities_list[1].name +
                '.\n\n    -press the space key-', color = (-1, -1, -1))
            answer_text.draw()
            myWin.flip()
            event.waitKeys(keyList = ['space'])
            
    if target == 2:
        if answer == '3':
            answer_text = visual.TextStim(myWin, text = 'Correct!\n' + cities_list[2].spot + ' is in ' + cities_list[2].name +
                '.\n\n  -Press the space key-', color = (-1, -1, -1))
            answer_text.draw()
            myWin.flip()
            event.waitKeys(keyList = ['space'])
        
        else:
            answer_text = visual.TextStim(myWin, text = 'Sorry, incorrect.\n' + cities_list[2].spot + ' is in ' + cities_list[2].name +
                '.\n\n  -Press the space key-', color = (-1, -1, -1))
            answer_text.draw()
            myWin.flip()
            event.waitKeys(keyList = ['space'])