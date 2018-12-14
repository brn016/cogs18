"""Script to run some part of my project."""

# This adds the directory above to our Python path
#   This is so that we can add import our custom python module code into this script
import sys
sys.path.append('../')


# Imports
# Imports allow for random number generation, ASCII characters, and clearing the command prompt screen
import random
import string
import os

# Imports allow for pauses during runtime and clearing the screen in Jupyter notebooks
from time import sleep
from IPython.display import clear_output
from my_module.functions import my_func, my_other_func

###
###

# Define a group of bots
# Modified code from A4-Artificial Agents
bots = [WanderBot(character = 1078), WanderBot(character = 1078), WanderBot(character = 1078),
        ExploreBot(character = 1127), ExploreBot(character = 1127), ExploreBot(character = 1127),
        TeleportBot(character = 1279), RookBot(character = 220), RookBot(character = 220)]

# Define a group of obstacles
obstacles = [PitFall(character = 216), PitFall(character = 216), PitFall(character = 216),
             PitFall(character = 216), PitFall(character = 216), PitFall(character = 216)]

# Play the board with our bot list
# External code from A4-Artificial Agents
play_board(bots, obstacles, grid_size=15, n_iter=50)

pass
