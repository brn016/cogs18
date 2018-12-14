import random
import string

from time import sleep
from IPython.display import clear_output


def check_bounds (position, size):
    """
    check if a position is on the grid. 
    
    Parameters
    ----------
    position: a list which typically includes two int items.
    
    size: int.
    
    Return
    -------
    Bolean.
        whether the position is or is not on the grid. 
    """
    for ele in position:
        if ele < 0 or ele >= size:
            return False
    return True


def add_lists (list1, list2):
    """
    add the values of corresponding items in two lists together and produce a new list. 
    
    Parameters
    ----------
    list1: list. 
        list to be added.
        
    list2: list. 
        list to be added.
    
    Return
    ------
    list. 
        a new list where each item is the sum of the corresponding items in the two input lists.
    """
    
    output = []
    
    for e1, e2 in zip (list1, list2):
        output.append (e1 + e2)
    return output


class Bot():
    """
    The base class of all the bots. 
    
    Attributes
    ----------
    character: int. 
        unicode for the character that represent this bot on the grid.
    position: list.
        position of this bot on the grid.
    moves: list.
        a list of possible moves.
    grid_size: int or None. 
        a size of the grid. Default is None. 
    """
    
    def __init__ (self, character = 8982):
        
        self.character = chr(character)
        self.position = [0,0]
        self.moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        self.grid_size = None

        
class WanderBot (Bot):
    """
    A WanderBot moves randomly on the grid. 
    
    Attributes
    ----------
    character: int. 
        unicode for the character that represent this bot on the grid.
    position: list.
        position of this bot on the grid.
    moves: list.
        a list of possible moves.
    grid_size: int or None. 
        a size of the grid. Default is None. 
    """
    
    def __init__ (self, character = 8982):
        
        super().__init__(character)
        self.name = "WanderBot"
        
    def wander(self):
        """
        This function produces a new position for WanderBot by randomly choosing one position from bot.moves and then add it to the last position.
        
        Return
        ------
        new_pos: list. 
            new position for WanderBot. 
        """
        has_new_pos = False
        
        while not has_new_pos:
            move = random.choice (self.moves)
            new_pos = add_lists(self.position, move)
            has_new_pos = check_bounds (new_pos, self.grid_size)
        return new_pos
    
    def move (self, bots):
        """
        a function that updates the position of the bots.
        
        Return
        ------
        bots: list
           a list of bots that are running on the grid.
        """
        self.position = self.wander()
        return bots

    
class ExploreBot(Bot):
    """
    a bot that generally moves towards the same direction but occasionally moves randomly. 
    
     Attributes
    ----------
    character: int. 
        unicode for the character that represent this bot on the grid.
    position: list.
        position of this bot on the grid.
    moves: list.
        a list of possible moves.
    grid_size: int or None. 
        a size of the grid. Default is None. 
    move_prob: float.
        the possibility of moving towards the same direction as last move. 
    last_move: list.
        last position on the grid. None by default. 
    """
    def __init__ (self, character = 8982, move_prob = 0.75):
        
        super().__init__ (character)
        self.move_prob = move_prob
        self.last_move = None
        self.name = "ExploreBot"
        
    def biased_choice (self):
        """
        a function that produce the same moving direction as last time at move_prob and a random direction the rest of times.
        
        Return
        -------
        move: list
           a chosen moving direction.
        """
        move = None
        if self.last_move != None:
            if random.random() < self.move_prob:
                move = self.last_move
            else:
                move = None
        if move == None:
                move = random.choice (self.moves)
        return move
    
    def explore(self):
        """
        a function that produces a new position based on biased_choice function.
        
        Return
        -------
        new_pos: list.
            new position for the bot.
        """
        
        has_new_pos = False
        while not has_new_pos:
            move = self.biased_choice()
            new_pos = add_lists(self.position, move)
            has_new_pos = check_bounds (new_pos, self.grid_size)
            self.last_move = move
        return new_pos
    
    def move(self, bots):
       """
        the function to update new position for ExploreBot. 
        
        Parameters
        ----------
        bots: list. 
            a list of bot class items.
        
        Return
        ----------
        bots: list. 
            a list of bot class items.
        
        self.position = self.explore()
        return bots
        """
    
class TeleportBot(WanderBot):
    """
    a bot that generally wander around randomly but occasionally teleport to a random position on the grid. 
    
    Attributes
    ----------
    character: int. 
        unicode for the character that represent this bot on the grid.
    position: list.
        position of this bot on the grid.
    moves: list.
        a list of possible moves.
    grid_size: int or None. 
        a size of the grid. Default is None. 
    name: string. 
        defined as TeleportBot. 
    """
    
    def __init__ (self, character = 8982, tele_prob = 0.2):
        super().__init__(character)
        self.tele_prob = tele_prob
        self.name = "TeleportBot"
   
    # at a defined small possibility (default = 0.2), TeleportBot gets teleport to a random location on the grid.
    def teleport(self):
        """
        the function to randomly choose a location on the grid.
        
        Return
        -------
        a random location on the grid. 
        """
        return [random.choice(range(self.grid_size)), random.choice(range(self.grid_size))]
    
    def move(self, bots):
        """
        the function to update new position for a TeleportBot. 
        
        Parameters
        ----------
        bots: list. 
            a list of bot class items.
        
        Return
        ----------
        bots: list. 
            a list of bot class items.
        """
        if random.random() < self.tele_prob:
            self.position = self.teleport()
        else:
            self.position = self.wander()
        return bots

    
class HorizontalBot (Bot):
    """
    a type of bots that moves only from left to right, but jump randomly up and down. 
    
    Attributes
    ----------
    character: int. 
        unicode for the character that represent this bot on the grid.
    position: list.
        position of this bot on the grid.
    moves: list.
        a list of possible moves.
    grid_size: int or None. 
        a size of the grid. Default is None. 
    name: string. 
        defined as HorizontalBot. 
    """
    def __init__(self, character = 8982):
        super().__init__(character)
        self.name = "HorizontalBot"
        
    # move one step to the right. if the position is out of the grid, then horizontalbot should come back to the far left of the grid and start all over again.     
    def move(self, bots):
        """
        the function to update new position for a HorizontalBot. 
        
        Parameters
        ----------
        bots: list. 
            a list of bot class items.
        
        Return
        ----------
        bots: list. 
            a list of bot class items.
        """
        horizontal_position = self.position[1]
        
        if horizontal_position + 1 < self.grid_size:
            horizontal_position = horizontal_position + 1
        else:
            horizontal_position = 0
            
        self.position = [random.choice(range(self.grid_size)), horizontal_position]

        return bots
    
    
class DiagonalBot (Bot):
    
    """
    a type of bots that jumps randomly on diagonal lines of the grid.
    
    Attributes
    ----------
    character: int. 
        unicode for the character that represent this bot on the grid.
    position: list.
        position of this bot on the grid.
    moves: list.
        a list of possible moves.
    grid_size: int or None. 
        a size of the grid. Default is None. 
    name: string. 
        defined as DiagonalBot. 
    """
    def __init__ (self, character = 8982):
        
        super().__init__(character)
        self.name = "DiagonalBot"
        
    # create a list of all the positions on the two diagonal lines. randomly choose one of the positions as the new position.
    def move(self, bots):
        
        diagonal_list = []
        
        for num in range (self.grid_size):
            diagonal_list.append ([num, num])
            diagonal_list.append ([num, self.grid_size - num - 1])
            
        self.position = random.choice(diagonal_list)
        
        return bots
    
    
class BotEater(WanderBot):
    """
    this class of bots moves randomly on the grid, deletes the bots that it runs into. 
    """
    
    def __init__(self, character = 8982):
    
        super().__init__ (character)
        self.name = "BotEater"
        
    def move(self, bots):
       """
       This function checks the positions of all the bots in the list. if one bot's position is the same as the BotEater at this time point, then omit this bot from the new list. update the list and update the position of BotEater.   
       
       Parameters
       -----------
       bots: list. 
           a list of bot items.
           
       Return
       ------
       new_bots: list
           a updated list of bots.
       """
       new_bots = []
    
       for bot in bots:
            
            if bot.name == "BotEater":
                new_bots.append(bot)
                
            elif not (bot.position[0] == self.position[0] and bot.position[1] == self.position[1]):
                new_bots.append(bot)
                
       self.position = self.wander()
 
       return new_bots

    
def play_board(bots, n_iter=25, grid_size=5, sleep_time=0.3):
    """Run a bot across a board.
    
    Parameters
    ----------
    bots : Bot() type or list of Bot() type
        One or more bots to be be played on the board
    n_iter : int, optional
        Number of turns to play on the board. default = 25
    grid_size : int, optional
        Board size. default = 5
    sleep_time : float, optional
        Amount of time to pause between turns. default = 0.3.
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
        
        # Update bot position(s) for next turn
        new_bots = bots.copy()
        for bot in bots:
            
            if not bot.name == "BotEater":
                bot.move(bots)
            else:
                new_bots = bot.move(bots)
                bots = new_bots