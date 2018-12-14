"""Script to run some part of my project."""

# This adds the directory above to our Python path
#   This is so that we can add import our custom python module code into this script
import sys
sys.path.append('../')


#Installing necessary packages
get_ipython().system('pip install twisted')
get_ipython().system('pip install ipyleaflet')
get_ipython().system('pip install folium')
get_ipython().system('pip install pandas')

#Imports
from my_module.functions import load_data_template, sum_violence_day, visual_incidents
import pandas as pd
import folium

###
###

# PYTHON SCRIPT HERE

#Sample code file provided, file titled "guns_example.csv"
#Importing data and converting dates and pulling day to analyze crimes on specific day
gun_csv = pd.read_csv("guns_example.csv")
gun_csv["date"] = pd.to_datetime(gun_csv["date"])
gun_csv["day"] = gun_csv["date"].map(lambda x: x.day)

#Template to match if user want to add statistics
template = pd.read_csv('template.csv')
print("Please ensure that data matches this template!")

#Run program to collect analyzed data
gun_violence = sum_violence_day(10)

#Visualize data in map
gun_violence
visual_incidents(gun_violence)
