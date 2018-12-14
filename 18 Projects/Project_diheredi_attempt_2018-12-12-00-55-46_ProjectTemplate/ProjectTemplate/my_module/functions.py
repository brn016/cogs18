"""A collection of function for doing my project."""

import random

##
##

 

#first function!! provides a random madlib 
def generate_madlib(madlibs_list):
    
    """
    Parameters
    -----------
    madlibs_list: list
        List so that there is only one input for the function instead of 3 concatenated strings
    
    Returns
    --------
    random_madlib: str
        String contains either the Christmas, Halloween, or Thanksgiving madlib
    """
    
    #the following loop will help generate a random madlib 
    for random_madlib in madlibs_list:
        random_madlib = random.choice(madlibs_list)
    return random_madlib
    
##
##

#list of all the keywords that can be used to provide an output for the next function 
madlib_holiday = ["christmas", "halloween", "thanksgiving", "random"]

#this function provides the madlib that corresponds to each keyword 
def choose_madlib(madlib_holiday):

   
    """
    Parameters
    ----------
    madlib_holiday: list of strings
        key words used to get a certain madlib
        
    Returns
    --------
    output: string
        Depending on the keyword inputed, the output will be the outline for one of the holiday madlibs
    """
    
    #the following conditional will determine which madlib will be used
    if madlib_holiday == "christmas":
        output = christmas_madlib
    elif madlib_holiday == "halloween":
        output = halloween_madlib
    elif madlib_holiday == "thanksgiving":
        output = thanksgiving_madlib
    elif madlib_holiday == "random":
        output = generate_madlib(madlibs_list)
    else:
        output = "pick christmas, halloween, thanksgiving, or random"
    return output
        