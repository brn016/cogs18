#import the class Patient from the python file classes.py
from my_module.classes import Patient 

import pandas as pd


def get_alpha(prompt):
    
    """
    get_alpha(prompt)
    
    A function that checks whether user's input consists of only alphabetical characters.
    If it does, function returns the user's input. If it doesn't, function prints an error message.
    
    Parameters
    ----------
    prompt: user's input
    
    Returns
    -------
    alpha: string 
    """

    not_alpha = True
    
    while not_alpha:
        
        alpha = input(prompt)
        
        if alpha.isalpha():
            
            not_alpha = False
            
        else:
            
            print('Please type in valid characters.')
            
    return alpha


def get_num(prompt):

    """
    get_num(prompt)
    
    A function that checks whether user's input is a number.
    If it is, function returns the user's input as a float. If it isn't, function prints an error message.
    
    Parameters
    ----------
    prompt: user's input
    
    Returns
    -------
    alpha: string   
    """
    
    not_num = True

    while not_num:

        num = input(prompt)
        
        if num.isnumeric():
            
            num = float(num)
            not_num = False
            
        else:
            
            print('Please type in a number.')
    
    return num



def chat_with_nurseassistant():
    
    """
    chat_with_nurseassistant()
    
    A function that stores user's input as key-value pairs in a dictionary, unpacks these arguments to create a class instance, and then appends this instance to a list.
        
    Parameters
    ----------
    user input: string
    
    Returns
    -------
    all_patients: list of class instances 
    """
    
    all_patients = []
    
    chat = True
    
    while chat:

        cur_patient = {}
            
        cur_patient['name'] = get_alpha('Patient name: ')
        
        cur_patient['age'] = get_num('Patient age: ')

        cur_patient['height'] = get_num('Patient height (in cm): ')

        cur_patient['weight'] = get_num('Patient weight (in kg): ')

        cur_patient['cholesterol_level'] = get_num('Cholesterol level(mg/dl): ')

        cur_patient['blood_pressure'] = get_num('Systolic blood pressure(mm Hg): ')
        
        #Unpack the user's inputs to create a new instance of the class Patients 
        cur_instance = Patient(**cur_patient)
        
        #Add current patient instance to list of all patient instances
        all_patients.append(cur_instance)
        
        repeat = input('Do you want evaluate another patient(yes/no)? ')
        
        if repeat == 'no':
            
            chat = False
            
        elif repeat == 'yes':
            
            chat
    
    return all_patients


def create_df(all_patients):

    """
    create_df(all_patients)
    
    A function that creates, styles, and returns a DataFrame object using a list of data that is parsed in.
    
    Parameters
    ----------
    all_patients: list
    
    Returns
    -------
    styled_df: DataFrame ojbect
    """
    
    df = pd.DataFrame()

    for patient in all_patients:

        df = df.append(vars(patient), ignore_index=True)
        df = df[['name', 'age', 'height', 'weight', 'cholesterol_level', 'blood_pressure']]

        #style the Data Frame using conditions defined in the functions color_cholesterol_level and color_blood_pressure
        styled_df = df.style.applymap(color_cholesterol_level, subset = ['cholesterol_level']).applymap(color_blood_pressure, subset = ['blood_pressure'])

    return styled_df




def color_cholesterol_level(value):
    
    """
    color_cholesterol_level(value)
    
    A function that returns a color according to input value.
    
    Parameters
    ----------
    value: int
        Cholesterol Level 
        
    Returns
    -------
    'color: ' + the color corresponding to the input value : string    
    """
    
    #average cholesterol level
    if value < 200: 
        color = 'black'
  
    #borderline high cholesterol level
    elif 200 <= value < 240: 
        color = 'orange'
    
    #high cholesterol level
    elif value >= 240: 
        color = 'red'
        
    return 'color: %s' % color




def color_blood_pressure(value):    
    
    """
    color_blood_pressure(value)
    
    A function that returns a color according to input value.
    
    Parameters
    ----------
    value: int
        Blood Pressure
        
    Returns
    -------
    'color:' + the color corresponding to the input value : string
          
    """
    
    #normal blood pressure
    if value < 120: 
        color = 'black'

    #elevated blood pressure
    elif 120 <= value < 130: 
        color = 'orange'

    #high blood pressure
    elif value >= 130: 
        color = 'red'

    return 'color: %s' % color



