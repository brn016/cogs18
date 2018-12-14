from psychopy import visual, core, event, gui, data
import os
import random
import time

#myWin = visual.Window([1280, 720], monitor = 'testMonitor', allowGUI = False, units = 'norm', color = (1,1,1))

"""
define the class of the cities in the USA (USACity)
Attributes
---------------
name: city's name
state: state where the city is in
population: population that the city has
spot: a famous sightseeing spot in the city

Methods
---------------
introduce: display the sentences to explain the city
spot_pic: display the picture of the sightseeing spot
"""

class USACity():
    country = 'the USA'
    
    def __init__(self, name, state, population, spot):
        self.name = name
        self.state = state
        self.population = population
        self.spot = spot
        
    def introduce(self, myWin):
        intro_text = visual.TextStim(myWin, text = self.name + ' is a city in '+ self.state +'.\nIts population is about '+
            str(round(self.population/1000000, 2)) + ' million.\nOne of the most famous sightseeing spots is ' + self.spot + '.',
            color = (-1,-1,-1))
        intro_text.draw()
        myWin.flip()
        event.waitKeys(keyList = ['space'])
        
    def spot_pic(self,myWin):
        picture = visual.ImageStim(win = myWin, image = 'Spot_pictures/' + self.spot + ".jpg", pos = (0,0), units = 'norm')
        picture.draw()
        myWin.flip()
        event.waitKeys(keyList = ['space'])
        