###Tests for my functions

from functions import load_data_template, sum_violence_day, visual_incidents

#import necessary modules
import matplotlib.pyplot as plt
import pandas as pd
import folium



#Creating test functions
def test_load_data_template():
    #This is an input check function, is for user reference. 
    assert load_data_template() == None
    
def test_sum_violence_day(day):
    #input must be an integer to represent a day of the month
    assert isinstance(day, int)
    assert day <= 31
    
def test_visual_incidents(incidents):
    #visual_incidents takes return from sum_violence_day and must be integer (number of crimes)
    assert isinstance(incidents, int)
    assert incidents >= 0



#This should fail if any input. It is a check reference function. 
try:
    test_load_data_template(10)
except TypeError:
    print("Error caught")



#Intentional testing, will result in error
try: 
    test_sum_violence_day("Y")
except AssertionError:
    print("Error caught")

test_sum_violence_day(10)



#Intentional testing, will result in error
try:
    test_visual_incidents(-3)
except AssertionError:
    print("Error caught")

test_visual_incidents(500)


