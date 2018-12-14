import random
"""
supplemental function for state_quiz
to create three multiple choices including the correct answer
I separated this function, create_choices because otherwise, pytest did not pass outside of PsychoPy.

Parameters
-------------
target: string
    the name of a state, which is the correct answer
    
returns
-------------
choices_list: list
    the list of three states, including target and other two wrong answers

"""

def create_choices(target):
    #list which includes the state names
    states_list = ['Arizona', 'Colorado', 'California', 'Florida', 'Kansas', 'Massachusetts', 'Michigan', 'Ohio', 'Pennsylvania', 'South Carolina', 'Texas', 'Virginia']
    
    #remove the target (correct answer) from states_list
    states_list.remove(target)
    #randomly choose two states from the list as wrong answers(2 items in the 'others')
    others = random.sample(states_list, 2)
        
    #shuffle the order of the three states
    choices_list = random.sample([others[0], others[1], target], 3)
    return choices_list
