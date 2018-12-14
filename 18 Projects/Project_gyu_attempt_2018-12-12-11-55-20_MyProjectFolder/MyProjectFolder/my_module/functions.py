"""A collection of function for doing my project."""

def clear():
    """Clears command prompt outputs."""
    
    # Helps keep clutter off of the screen
    os.system('cls')


def add_lists(list1, list2):
    """Adds the corresponding elements of two lists, appends results to output list
        External code from A4- Artificial Agents
    
    Parameters
    ----------
    list1 : list
        first list of values to be added
    list2 : list
        second list of values to be added
        
    Returns
    -------
    output : list of added values
        result of addition.
    """
    
    output=[]
    
    # Adding corresponding values in lists allows bots to move by increments from their previous positions
    for it1, it2 in zip(list1, list2):
        result = it1 + it2
        output.append(result)
        
    return output


def check_bounds(position, size):
    """Checks if a bot's position will be outside of the board.
    
    Parameters
    ----------
    position : list of ints
        Position of bots on the board
    size : int
        Size of the board
        
    Returns
    -------
    return : bool
        Answer to whether it is on the board or not.
    """
    
    # For a bot's position, return false if it is outside the board, true if inside so will not throw error
    for item in position:
        if item < 0 or item >= size:
            return False
        
    return True


def play_board(bots, obstacles, n_iter = 25, grid_size = 5, sleep_time = 0.5):
    """Run a bot across a board.
    External code from A4- Artificial Agents
    
    Parameters
    ----------
    bots : Bot() type or list of Bot() type
        One or more bots to be be played on the board
    n_iter : int, optional
        Number of turns to play on the board. default = 25
    grid_size : int, optional
        Board size. default = 5
    sleep_time : float, optional
        Amount of time to pause between turns. default = 0.5.
    """
    
    # If input is a single bot, put it in a list so that procedures work
    if not isinstance(bots, list):
        bots = [bots]
        
    # If input is a single pit, put it in a list so that procedures work
    if not isinstance(obstacles, list):
        obstacles = [obstacles]
    
    # Update each bot to know about the grid_size they are on
    for bot in bots:
        bot.grid_size = grid_size
        
    # Lets pits know about the grid_size they are on
    for pit in obstacles:
        pit.grid_size = grid_size
        
    # Update pit position(s) for next turn
    for pit in obstacles:
        pit.place_pit()
            
    # Removes bots that occupy spaces that pits occupy
    for it in range(n_iter):
        if it >10:
            for pit in obstacles:
                for bot in bots:
                    if bot.position == pit.position:
                        bots.remove(bot)

    # Removes a bot when two occupy the same space, 50% chance of either being removed
    for it in range(n_iter):
        if it > 10:
            for bot1 in bots:
                remove_bot = False
                for bot2 in bots:
                    if remove_bot != False:
                        bots.remove(remove_bot)
                        remove_bot = False
                    if random.random() <= .5:
                        if bot1.position == bot2.position and bot1.character != bot2.character:
                            remove_bot = bot2
                    else:
                        if bot1.position == bot2.position and bot1.character != bot2.character:
                            remove_bot = bot1

        # Create the grid
        grid_list = [['.'] * grid_size for ncols in range(grid_size)]
        
        # Add bot(s) to the grid
        for bot in bots:
            grid_list[bot.position[0]][bot.position[1]] = bot.character
            
        # Add pits to the grid
        for pit in obstacles:
            grid_list[pit.position[0]][pit.position[1]] = pit.character

        # Clear the previous iteration, print the new grid as a string, and wait
        clear()
        clear_output(True)
        print('\n'.join([' '.join(lst) for lst in grid_list]))
        sleep(sleep_time)

        # Update bot position(s) for next turn
        for bot in bots:
            bot.move()

class Bot():
    """The base class for every bot
    
    Parameters
    ----------
    
    """
    
    def __init__(self, character = 8982):
        """
        character: chr
            Character used to represent bots or space
        position: list of ints
            Position of bots on board
        moves: list of lists of ints
            Possible movement of bots
        grid_size: int
            size of board.
        """
        
        # Initializes variables for bots
        self.character = chr(character)
        self.position = [0, 0]
        self.moves = [[-1, 0], [1,0], [0, 1], [0, -1]]
        self.grid_size = None

        
class PitFall():
    """Kills bots that move onto it.
    
    Parameters
    ----------
    """
    
    
    def __init__(self, character = 8982):
        """
        character: chr
            Character used to represent bots or space
        position: list of ints
            Position of pits on board
        grid_size: int
            size of board.
        """
        
        # Initializes variables for pits
        self.character = chr(character)
        self.position = [0, 0]
        self.grid_size = None
        
        
    def pit_area(self):
        """
        Determines locations of pits.
        
        Returns
        -------
        pit_pos : list of ints
            Location of pits on board
        
        """
        
        # Finds a completely random area on the board to place a pit
        pit_pos = [random.choice(range(self.grid_size)), random.choice(range(self.grid_size))]
        
        return pit_pos
        
        
    def place_pit(self):
        """
        Sets pitfall position.
        
        """
        
        # Set position of pits on board
        self.position = self.pit_area()
        
        
class WanderBot(Bot):
    """This bot will move horizontally or vertically at random one step at a time.
    
    Parameters
    ----------
    """
    
    
    def __init__(self, character = 8982):
        """
        character: chr
            Character used to represent bots or space
        position: list of ints
            Position of bots on board
        moves: list of lists of ints
            Possible movement of bots
        grid_size: int
            size of board.
        """
        
        # Call superclass's constructor
        super().__init__(character)
        
        
    def wander(self):
        """
        Moves the bot horizontally or vertically by one step while ensuring the move is within the board.
        
        Returns
        -------
        new_pos : list of ints
        """
        
        # While the bot is not in a new position, add a random move list to the position list
        has_new_pos = False
        
        while not has_new_pos:
            move = random.choice(self.moves)
            new_pos = add_lists(self.position, move)
            has_new_pos = check_bounds(new_pos, self.grid_size)
            
        return new_pos
    
    
    def move(self):
        """
        Sets the bot's position to the move.
        
        """
        
        # Use wander() to set position of bot on board
        self.position = self.wander()


        
class RookBot(Bot):
    """This bot will move horizontally or vertically at random for a random distance.
    
    Parameters
    ----------
    """
    
    def __init__(self, character = 8982):
        """
        character: chr
            Character used to represent bots or space
        position: list of ints
            Position of bots on board
        moves: list of lists of ints
            Possible movement of bots
        grid_size: int
            size of board.
        """
        
        # Call superclass's constructor
        super().__init__(character)
        
        
    def hori_verti(self):
        """
        Moves the bot horizontally or vertically for random distance while ensuring the move is within the board.
        
        Returns
        -------
        new_pos : list of ints
        
        """
        
        has_new_pos = False
        
        # If the bot is not in a new position, choose a move from move_options
        while not has_new_pos:
            move_options = [[0,random.choice(range(self.grid_size))],[random.choice(range(self.grid_size)),0],
                     [0,-1 * random.choice(range(self.grid_size))],[-1 * random.choice(range(self.grid_size)),0]]
            move = random.choice(move_options)
            new_pos = add_lists(self.position, move)
            has_new_pos = check_bounds(new_pos, self.grid_size)
            
        return new_pos
    
    
    def move(self):
        """
        Sets the bot's position to the move.
        
        """
        
        # Use hori_verti() to set position of bot on board
        self.position = self.hori_verti()
    
    
class ExploreBot(Bot):
    """This bot will generally move in the same direction on consecutive steps.
    
    Parameters
    ----------
    """
    
    
    def __init__(self, character = 8982, move_prob = 0.75):
        """
        character: chr
            Character used to represent bots or space
        position: list of ints
            Position of bots on board
        moves: list of lists of ints
            Possible movement of bots
        grid_size: int
            Size of board.
        move_prob: float
            Probability of moving in same direction as last move
        last_move: None
            Variable showing if the bot moved last turn
        """
        
        # Call superclass's constructor and initialize variables for different types of movement 
        # and checking if there was a move last turn
        super().__init__(character)
        self.move_prob = move_prob
        self.last_move = None
        
        
    def biased_choice(self):
        """
        Chooses to move the bot horizontally or vertically by one step with a bias for the last move taken.
        
        Returns
        -------
        move : list of ints
    
        """
        
        move = None
        
        # If no move was taken last turn, move randomly according to the list moves. Else, the move
        # is more likely to be the last value of the list moves chosen
        if self.last_move != None:
            if random.random() < self.move_prob:
                move=self.last_move
        if move == None:
            move = random.choice(self.moves)
            
        return move
        
        
    def explore(self):
        """
        Moves the bot horizontally or vertically by one step while ensuring the move is within the board.
        
        Returns
        -------
        new_pos : list of ints
        
        """
        
        has_new_pos=False
        
        # If the bot is not in a new position, move based on the funtion biased_choice
        while not has_new_pos:
            move = self.biased_choice()
            new_pos=add_lists(self.position, move)
            has_new_pos = check_bounds(new_pos, self.grid_size)
            move = self.last_move
            
        return new_pos
        
        
    def move(self):
        """
        Sets the bot's position to the move.
    
        """
        
        # Use explore() to set position of bot on board
        self.position = self.explore()
        

class TeleportBot(WanderBot):
    """This bot will move horizontally or vertically at random one step at a time,
    and will sometimes teleport to a new location.
    
    Parameters
    ----------
    """
    
    
    def __init__(self, character = 8982, tele_prob = 0.2):
        """
        character: chr
            Character used to represent bots or space
        position: list of ints
            Position of bots on board
        moves: list of lists of ints
            Possible movement of bots
        grid_size: int
            Size of board.
        tele_prob: float
            Probability of teleportation
        """
        
        # Call superclass's constructor and initialize a variable for probability of movement via teleportation
        super().__init__(character)
        self.tele_prob = tele_prob
        
        
    def teleport(self):
        """
        Moves the bot to a random location on the board.
        
        Returns
        -------
        tp_list : list of ints
    
        """
        
        # Find a random position that is within the board
        tp_list = [random.choice(range(self.grid_size)), random.choice(range(self.grid_size))]
        
        return tp_list
    
    
    def move(self):
        """
        Sets the bot's position to the move.
    
        """
        
        # Use teleport() and wander() to set position of bot on board
        if random.random() < self.tele_prob:
            self.position = self.teleport()
        else:
            self.position = self.wander()
