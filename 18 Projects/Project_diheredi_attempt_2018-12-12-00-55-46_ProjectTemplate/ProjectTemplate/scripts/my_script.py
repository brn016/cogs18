"""Script to run some part of my project."""

# This adds the directory above to our Python path
#   This is so that we can add import our custom python module code into this script
import sys
sys.path.append('../')

import random 

# variables that describe what should be input into the madlibs

adj1 = ("insert adjective here")
color1 = ("insert color here")
color2 = ("insert color here")
adj2 = ("insert adjective or action here")
verb1 = ("insert verb here")
noun1 = ("insert noun here")
month1 = ("insert month here")
food1 = ("insert food here")

##
##


# Christmas mad libs from https://www.woojr.com/christmas-mad-libs/grinch-mad-libs/
# concatenates strings with the variables to set up the outline for the Christmas madlib

christmas_madlib = "The Grinch is a " + adj1 + " " + color1 + " creature with " + color2 + " " + \
    "eyes who does not like " + "Christmas cheer" + " when he sees people celebrating Christmas it makes him" + \
    " "+ adj2 + "."
print(christmas_madlib)

##
##


# Halloween mad libs from https://www.pinterest.com/pin/142074563222734524/
# concatenates strings with the variables to set up the outline for the Halloween madlib

halloween_madlib = "Tonight is the night when all of the " + adj1 + " monsters come out to " + verb1 + "."+ \
    " " + color1 + "  witches with big " + noun1 + " and " + color2 + " shoes make potions and very spooky brews."
print(halloween_madlib)

##
##


# Thanksgiving mad libs from https://www.woojr.com/thanksgiving-mad-libs/mad-libs-kids-thanksgiving/
# concatenates strings with the variables to set up the outline for the Thanksgiving madlib

thanksgiving_madlib = "Every " + month1 + " my family celebrates Thanksgiving. First, my parents buy a " + adj1 + \
    " " + food1 + " to " + verb1 + " in the oven all day."
print(thanksgiving_madlib)

##
##


#all the holiday madlibs are put into one list 
madlibs_list = [christmas_madlib, halloween_madlib, thanksgiving_madlib]

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
