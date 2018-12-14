"""A collection of function for doing my project."""

## Code for imports from Assignment 4
import random
import string

from time import sleep
from IPython.display import clear_output

def add_lists(list1, list2):
    
    ## Function created in Assignment 4
    
    output = []
    
    for it1, it2 in zip(list1, list2):
        
        output.append(it1 + it2)
        
    return output

def check_bounds(position, size):
    
    ## Function created in Assignment 4
    
    for item in position:
        
        if item < 0 or item >= size:
            
            return False
        
    return True

def change_speed(sleep_time, all_sleep_times):

    """
    Makes the bot speed up with each iteration, then slow down again once it reaches a specified speed
    
    Parameters
    ----------
    sleep_time : float
        the amount of time between iterations in seconds
    all_sleep_times : list
        a list to which each sleep time will be added as it is used
    """
    
    if sleep_time <= 0.05:
        ## Starts slowing down again once the time between iterations reaches 0.05
        sleep_time = sleep_time + 0.01
    else:
        for item in all_sleep_times:
            if item <= 0.05:
                ## Continues the slow down process once it has started
                ## Checks in all_sleep_times for 0.05, which is the speed that triggered the slow down process
                sleep_time = sleep_time + 0.01
                return sleep_time
            else:
                continue
        
        ## Speeds up the bot while none of the prior conditions apply
        sleep_time = sleep_time - 0.01
        
    return sleep_time

def play_board(bots, n_iter = 25, grid_size = 25, sleep_time = 0.3, all_sleep_times = []):
    
    ## Code taken from Assignment 4, with minor edits made
    
    """Run a bot across a board.
    
    Parameters
    ----------
    bots : Bot() type or list of Bot() type
        One or more bots to be be played on the board
    n_iter : int, optional
        Number of turns to play on the board. default = 25
    grid_size : int, optional
        Board size. default = 25
    sleep_time : float, optional
        Amount of time to pause between turns. default = 0.3.
    
    ## ADDITIONAL VARIABLE ADDED:
    
    all_sleep_times : list, optional
        a list to which each sleep time will be added as it is used. default = []
    """
    
    # If input is a single bot, put it in a list so that procedures work
    if not isinstance(bots, list):
        bots = [bots]
    
    # Update each bot to know about the grid_size they are on
    for bot in bots:
        bot.grid_size = grid_size

    for it in range(n_iter):
        
        # Create the grid
        grid_list = [['.'] * grid_size for ncols in range(grid_size)]
        
        # Add bot(s) to the grid
        for bot in bots:
            grid_list[bot.position[0]][bot.position[1]] = bot.character    

        # Clear the previous iteration, print the new grid (as a string), and wait
        clear_output(True)
        print('\n'.join([' '.join(lst) for lst in grid_list]))
        sleep(sleep_time)
        
        """ADDITIONAL CODE ADDED"""
        ## Add the current sleep time to all_sleep_times and change the value of sleep_time
        all_sleep_times.append(sleep_time)
        sleep_time = change_speed(sleep_time, all_sleep_times)
        
        ## Once the change_speed process has gone through a full cycle, restart the process
        if all_sleep_times[-1] > 0.3:
            all_sleep_times = []
        """END OF ADDITIONAL CODE"""

        # Update bot position(s) for next turn
        for bot in bots:
            bot.move()
            
class Bot():
    
    ## Taken from Assignment 4
    
    def __init__(self, character = 8982, position = [0, 0], moves = [[-1, 0], [1, 0], [0, 1], [0, -1]], grid_size = None):
        
        self.character = chr(character)
        self.position = position
        self.moves = moves
        self.grid_size = grid_size
        
class DiagBot(Bot):
    
    """
    A bot that moves only diagonally
    
    Parameters
    ----------
    position : list, optional
        the coordinates of the bot on the board (default is [0, 0])
    character : int, optional
        a numerical value that determines the look of the bot (default is 8982)
    moves : list, optional
        a list of possible moves the bot can take (default is [[-1, 1], [1, 1], [1, -1], [-1, -1]])
    grid_size : int, optional
        the length of one side of the board (default is None)
        
    Methods
    -------
    diag()
        Moves the bot in a diagonal direction
    move()
        Moves the bot to the position established in diag()
        
    """
    
    def __init__(self, character = 8982, position = [0, 0], moves = [[-1, 1], [1, 1], [1, -1], [-1, -1]], grid_size = None):
        
        super().__init__(character, position, moves, grid_size)
        
    def diag(self):
        
        """
        Moves the bot in a diagonal direction
        
        Parameters
        ----------
        None
        
        Returns
        -------
        new_pos : list
            the new coordinates of the bot on the board
        """
        
        has_new_pos = False
        
        while not has_new_pos:
            
            ## Choose a random move from the list of moves
            move = random.choice(self.moves)
            
            ## Determine new position by adding move to current position
            new_pos = add_lists(self.position, move)
            
            ## Make sure the new position is on the grid
            has_new_pos = check_bounds(new_pos, self.grid_size)
            
        return new_pos
    
    def move(self):
        
        """
        Moves the bot to the position established in diag()
        
        Changes the value of self.position to that of new_pos
        
        Parameters
        ----------
        None
        
        Returns
        -------
        self.position : list
            the coordinates of the bot on the board
        """
        
        self.position = self.diag()
        
class BounceBot(Bot):
    
    """
    A bot that bounces diagonally off the boundary of the grid
    
    Attributes
    ----------
    position : list, optional
        the coordinates of the bot on the board (default is [0, 0])
    character : int, optional
        a numerical value that determines the look of the bot (default is 8982)
    moves : list, optional
        a list of possible moves the bot can take (default is [[-1, 1], [1, 1], [1, -1], [-1, -1]])
    grid_size : int, optional
        the length of one side of the board (default is None)
    move_var : int, optional
        variable that determines which move to take from the list 'moves' (default is 0)
        
    Methods
    -------
    bounce()
        Directs the bot's movement so that it moves diagonally in a straight line until it reaches the edge of the grid
    move()
        Moves the bot to the position established in bounce()
    """
    
    def __init__(self, character = 8982, position = [3, 0], moves = [[-1, 1], [1, 1], [1, -1], [-1, -1]], grid_size = None, 
                move_var = 0):
        
        super().__init__(character, position, moves, grid_size)
        self.move_var = move_var
        
    def bounce(self):
        
        """
        Directs the bot's movement so that it moves diagonally in a straight line until it reaches the edge of the grid
        
        The bot will move in a random diagonal direction once reaching the edge
        
        Parameters
        ----------
        None
        
        Returns
        -------
        new_pos : list
            the new coordinates of the bot on the board 
        """
        
        has_new_pos = False
        
        while not has_new_pos:
            
            ## Maintains previous move to continue in line, based off of move_var
            move = self.moves[self.move_var]
            
            ## Determine new position by adding move to current position
            new_pos = add_lists(self.position, move)
            
            ## Check if the last move goes outside of bounds, to see if the bot has reached the edge of the grid
            if check_bounds(new_pos, self.grid_size):
                ## If in bounds, return the new position
                has_new_pos = True
                return new_pos
            else:
                ## If not in bounds, change the direction by randomly changing the value of move_var
                self.move_var = random.choice([0, 1, 2, 3])
                
    def move(self):
        
        """
        Moves the bot to the position established in bounce()
        
        Changes the value of self.position to that of new_pos
        
        Parameters
        ----------
        None
        
        Returns
        -------
        self.position : list
            the coordinates of the bot on the board
        """
        
        self.position = self.bounce()
        
class SquareBot(Bot):
    
    """
    A bot that moves in a square
    
    Attributes
    ----------
    position : list, optional
        the coordinates of the bot on the board (default is [0, 0])
    character : int, optional
        a numerical value that determines the look of the bot (default is 8982)
    moves : list, optional
        a list of possible moves the bot can take (default is [[0, -1], [1, 0], [0, 1], [-1, 0]])
    grid_size : int, optional
        the length of one side of the board (default is None)
    move_list : list, optional
        a list to store each move after it is taken (default is [])
    move_var : int, optional
        a variable to determine which move to take from the list 'moves' (default is 1)
        
    Methods
    -------
    square()
        Sets new positions for the bot in the pattern of a 5-by-5 square
    move()
        Moves the bot to the position established in square()
    """
    
    def __init__(self, position = [0, 0], character = 8982, moves = [[0, -1], [1, 0], [0, 1], [-1, 0]], grid_size = None, 
                 move_list = [], move_var = 1):
    
        super().__init__(character, position, moves, grid_size)
        self.move_list = move_list
        self.move_var = move_var
        
    def square(self):
        
        """
        Sets new positions for the bot in the pattern of a 5-by-5 square
        
        Parameters
        ----------
        None
        
        Returns
        -------
        new_pos : list
            the new coordinates of the bot on the board
        """
        
        has_new_pos = False
        
        while not has_new_pos:
            
            if len(self.move_list) == 4:
                
                ## length of self.position_list == (length of side of square - 1)
                ## Signals change of direction
                ## Clear move_list to restart for the next side of the square
                self.move_list = []
                
                ## Change the direction, new direction determined by move_var
                move = self.moves[0 + self.move_var]
                
                ## Change the value of move_var, to maintain current direction and determine the next direction
                if self.move_var == 3:  
                    self.move_var = 0
                else:
                    self.move_var += 1
            
            ## Maintain current direction when len(self.move_list) != 4, based on the value of move_var
            elif self.move_var == 0:
                
                move = [-1, 0]
                
            elif self.move_var == 1:
                
                move = [0, -1]
                
            elif self.move_var == 2:
                
                move = [1, 0]
                
            else:
                
                move = [0, 1]
            
            ## Add move to move_list
            (self.move_list).append(move)
            
            ## Determine new position by adding move to current position
            new_pos = add_lists(self.position, move)
            
            ## Make sure the new position is on the grid
            has_new_pos = check_bounds(new_pos, self.grid_size)
        
        return new_pos
    
    def move(self):
        
        """
        Moves the bot to the position established in square()
        
        Changes the value of self.position to that of new_pos
        
        Parameters
        ----------
        None
        
        Returns
        -------
        self.position : list
            the coordinates of the bot on the board
        """
        
        self.position = self.square()