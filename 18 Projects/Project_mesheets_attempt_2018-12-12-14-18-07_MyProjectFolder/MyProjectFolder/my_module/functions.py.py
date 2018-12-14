#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

def state_one_year(state, year):
    
    """this function calls on a Cause for any state and year"""

    state_data = final_data[final_data['State'] == state]    
    state_year = state_data[state_data['Year'] == year]
    list_of_causes_in_year = state_year['Cause']    
    return (state_year, list_of_causes_in_year)

def state_all_years(state):
    
    """this function returns the single death rate of a state from all causes over all years"""
    
    state_data = final_data[final_data['State'] == state]    
    state_all_years = state_data[state_data['Cause'] == 'All causes']    
    return (state_all_years)

def sort_state(state_year):
    
    """this function sorts the causes of death by death rates in the given year """
    
    state_year_sorted = state_year.sort_values(['Deaths', 'Cause'], ascending=False)
    return state_year_sorted[['Deaths', 'Cause']].head(11)


# In[ ]:




