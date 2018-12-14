from psychopy import visual, core, event, gui, data
import os
import random
import time

"""
-Project discription-
This program introduces the cities in the US for international students.
It is divided into two sections: learning section and quiz section. 
The quiz section includes three questions: about population, state, and sightseeing spot.

Personally, this program is a practice of PsychoPy becauese I am a psych major.

"""

#import class(USACity) from Final_Project_class module 
from my_module.classes import USACity

#instances of USACity
san_diego = USACity('San Diego', 'California', 1400000, 'La Jolla Cove')
los_angeles = USACity('Los Angeles', 'California', 4000000, 'Hollywood sign')
houston = USACity('Houston', 'Texas', 2100000, 'Johnson Space Center')
boston = USACity('Boston', 'Massachusetts', 690000, 'Faneuil Hall')
philadelphia = USACity('Philadelphia', 'Pennsylvania', 1600000, 'Liberty Bell')
phoenix = USACity('Phoenix', 'Arizona', 1500000, 'Desert Botanical Gardern')
detroit = USACity('Detroit', 'Michigan', 700000, 'Henry Ford Museum and Greenfield Village')
columbus = USACity('Columbus', 'Ohio', 780000, 'Ohio Stadium')

#store all instances into 'all_cities'
all_cities = [san_diego, los_angeles, houston, boston, philadelphia, phoenix, detroit, columbus]


#display the introduction text on the screen to explain this program
myWin = visual.Window([1280, 720], monitor = 'testMonitor', allowGUI = False, units = 'norm', color = (1,1,1))
text1 = visual.TextStim(myWin, 
    text = 'Hello, international students.\nThis program is created to introduce the cities in the USA.\n\n-Press the space key-',
    color = (-1,-1,-1))
text1.draw()
myWin.flip()
event.waitKeys(keyList = ['space'])

#While the subject wants to learn about the cities (learnign = True), the program is stuck to the learning section
#When the subjct wants to move onto the quiz section(press a space key), learning becomes False
learning = True

while learning:
    text2 = visual.TextStim(myWin, 
        text = 'Choose the city you want to learn. \n 1. San Diego \n 2. Los Angeles \n 3. Houston \n 4. Boston' + 
        '\n 5. Philadelphia \n 6. Phoenix \n 7. Detroit \n 8. Columbus \nIf you want to move to the quiz section, press the space key.',
        color = (-1,-1,-1))
    text2.draw()
    myWin.flip()
    chosen_city = event.waitKeys(keyList = ['1','2','3','4','5','6','7','8','space'])[0]

#based on their answers, start the learning section, display the name of the city
    #San Diego
    if chosen_city == '1':
        #color = blue
        text3 = visual.TextStim(myWin, text = san_diego.name, color = (-1,-1,1), height = 0.2)
        text3.draw()
        myWin.flip()
        event.waitKeys(keyList = ['space'])
    
        san_diego.introduce(myWin)
        san_diego.spot_pic(myWin)
    
    #Los Angeles
    elif chosen_city == '2':
        text3 = visual.TextStim(myWin, text = los_angeles.name, color = (-1,-1,1), height = 0.2)
        text3.draw()
        myWin.flip()
        event.waitKeys(keyList = ['space'])
    
        los_angeles.introduce(myWin)
        los_angeles.spot_pic(myWin)
    
    #Houston
    elif chosen_city == '3':
        text3 = visual.TextStim(myWin, text = houston.name, color = (-1,-1,1), height = 0.2)
        text3.draw()
        myWin.flip()
        event.waitKeys(keyList = ['space'])
    
        houston.introduce(myWin)
        houston.spot_pic(myWin)
    
    #Boston
    elif chosen_city == '4':
        text3 = visual.TextStim(myWin, text = boston.name, color = (-1,-1,1), height = 0.2)
        text3.draw()
        myWin.flip()
        event.waitKeys(keyList = ['space'])
    
        boston.introduce(myWin)
        boston.spot_pic(myWin)
    
    #Philadelphia
    elif chosen_city == '5':
        text3 = visual.TextStim(myWin, text = philadelphia.name, color = (-1,-1,1), height = 0.2)
        text3.draw()
        myWin.flip()
        event.waitKeys(keyList = ['space'])
    
        philadelphia.introduce(myWin)
        philadelphia.spot_pic(myWin)
    
    #Phoenix
    elif chosen_city == '6':
        text3 = visual.TextStim(myWin, text = phoenix.name, color = (-1,-1,1), height = 0.2)
        text3.draw()
        myWin.flip()
        event.waitKeys(keyList = ['space'])

        phoenix.introduce(myWin)
        phoenix.spot_pic(myWin)
    
    #Detroit
    elif chosen_city == '7':
        text3 = visual.TextStim(myWin, text = detroit.name, color = (-1,-1,1), height = 0.2)
        text3.draw()
        myWin.flip()
        event.waitKeys(keyList = ['space'])
    
        detroit.introduce(myWin)
        detroit.spot_pic(myWin)
    
    #Columbus
    elif chosen_city == '8':
        text3 = visual.TextStim(myWin, text = columbus.name, color = (-1,-1,1), height = 0.2)
        text3.draw()
        myWin.flip()
        event.waitKeys(keyList = ['space'])
    
        columbus.introduce(myWin)
        columbus.spot_pic(myWin)
    
    #quit the learning section ('learning' becomes false), move onto the quiz section
    elif chosen_city == 'space':
        learning = False

#start the quiz section
text4 = visual.TextStim(myWin, text = 'Now, quiz time! \n\n-Press the space key-', color = (-1, -1,-1))
text4.draw()
myWin.flip()
event.waitKeys(keyList = ['space'])

#start a quiz about the population
from my_module.quiz import population_quiz
population_quiz(all_cities, myWin)

#start a quiz about the states
from my_module.function import create_choices
from my_module.quiz import state_quiz
state_quiz(all_cities, myWin)

#start a quiz about the sightseeing spot
from my_module.quiz import spot_quiz
spot_quiz(all_cities, myWin)

text5 = visual.TextStim(myWin, text = 'Thank you for playing!!', color = (-1, -1, 1), height = 0.1)
text5.draw()
myWin.flip()
event.waitKeys(keyList = ['space'])
