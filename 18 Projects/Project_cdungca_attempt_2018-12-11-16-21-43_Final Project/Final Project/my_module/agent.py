import random

from time import sleep
from IPython.display import clear_output


def add_lists(list1, list2):
    """Adds 2 lists together.

    This function is external code from A4.
    Link: https://cogs18.github.io/assignments/A4-ArtificialAgents/

    Inputs
    ----------
    list1 : list
        Any list.

    list2 : list
        Any list.

    Returns
    ----------
    output : list
        The summation of list1 and list2
    """

    output = []

    for it1, it2 in zip(list1, list2):
        summation = it1 + it2

        output.append(summation)

    return output


def check_bounds(grid_list, new_position, size):
    """Check if a position exists within grid boundaries.
        Note that all positions on the board are positive numbers.

        This function contains external code from A4, but is modified to
        check for additional conditions.

        Link: https://cogs18.github.io/assignments/A4-ArtificialAgents/

    Inputs
    ----------
    grid_list : list of list
        The grid itself. This input is used to check for walls.
    new_position : list of int
        Coordinates on the grid.

    size : int
        The grid's dimensions. This input is used to check for borders.

    Returns
    ----------
    boolean
    """

    # Checks if new position is within grid boundaries
    for element in new_position:
        if element < 0 or element >= size:
            return False

    # Checks if the new position is a wall in the grid_list
    if grid_list[new_position[0]][new_position[1]] == 'X':
        return False

    return True


class MazeBot():
    """This is the artificial agent that finds its way through the maze.

    This bot is based on the ExploreBot from A4, but is significantly modified to navigate
    the project's maze.
    Link: https://cogs18.github.io/assignments/A4-ArtificialAgents/

    Attributes
    ----------
    character: int
        A unicode character that shows up as the artificial agent.
    position: list of int
        Denotes a position in the maze grid.
    moves: list of list
        Denotes potential moves in the grid.
    grid_size: int.
        Specifies the n x n dimensions of the maze.
    move_prob: float
        The likelihood of the agent repeating its last move.
    last_move: list of int
        The last move of the bot.
    """

    def __init__(self, character=9632, move_prob=0.999):
        self.character = chr(character)
        self.position = [1, 1]
        self.moves = [[1, 0], [0, -1], [0, 1]]
        self.grid_size = None
        self.move_prob = move_prob
        self.last_move = None

    def biased_choice(self, grid_list):
        """Assigns the next move of the artificial agent based on
        specified conditions.

        inputs
        ----------
        grid_list : list of list
            A list of characters that when printed together, creates a maze.

        returns
        ----------
        move : list of int
            The next move of the agent.
        """

        move = None

        if self.last_move is not None:

            # Moves the character into a blank space if there is one under it.
            if grid_list[self.position[0] + 1][self.position[1]] == ' ':
                move = [1, 0]

            # If not, repeat the last move a specified probability
            elif random.random() < self.move_prob:
                move = self.last_move

        # Choose a random move if the above code doesn't run
        if move is None:
            move = random.choice(self.moves)
        return move

    def explore(self, grid_list):
        """Updates the agent's position in the grid and checks if it's allowed

        inputs
        ----------
        grid_list : list of int
            A list of characters that when printed together, creates a maze.

        returns
        ----------
        new_pos : list of int
            The new coordinates of the agent on the grid.
        """

        has_new_pos = False
        while not has_new_pos:
            move = self.biased_choice(grid_list)
            new_pos = add_lists(move, self.position)
            has_new_pos = check_bounds(grid_list, new_pos, self.grid_size)
            self.last_move = move
        return new_pos

    def move(self, grid_list):
        """When called on the agent, updates position and checks if next move is allowed.

        inputs
        ----------
        grid_list : list of list
            A list of characters that when printed together, creates a maze.

        """
        self.position = self.explore(grid_list)

    def final_choice(self):
        """When about to complete maze, update the bot's next move manually.
            This is because finishing the maze will make the agent try to
            check for positions which are outside the maze boundaries.
        """
        final_position = add_lists([1, 0], self.position)
        return final_position

    def final_move(self):
        """Updates the bot's final position on the maze board."""
        self.position = self.final_choice()


def build_maze_walls(grid_size, wall_type='X'):
    """Builds a maze with walls in every other row.

    Parameters
    ----------
    grid_size : int
        Specifies the dimensions of the grid.
    wall_type : char, optional. default = 'X'
        The character that shows up as the "walls" of the maze.

    Returns
    ----------
    grid_list : list
        A list of lists. Alternates between white space and "walls".
    """

    grid_list = []

    # Creates an empty grid list with no walls
    for ncols in range(grid_size):
        grid_list.append([' '] * grid_size)

    # Turns every other row into a wall
    for row in grid_list[0::2]:

        for column in range(grid_size):
            row[column] = wall_type

    # Selects empty rows and adds walls to the edges
    for row in grid_list[1::2]:

        for column in range(grid_size):
            row[0] = wall_type
            row[-1] = wall_type

    return grid_list


def hole_list_generator(grid_size):
    """Generates the positions of the holes in the maze walls.
    This function exists so that each maze is randomized.

    Inputs
    ----------
    grid_size : int
        The size of the grid.

    Returns
    ----------
    my_lst : list
        A set of random numbers that denote hole positions which ranges based on grid size.
    """
    grid_list = build_maze_walls(grid_size)
    my_lst = []

    for item in grid_list[0::2]:
        my_lst.append(random.randint(1, grid_size - 2))

    return my_lst


def play_board_maze(bots, grid_size, sleep_time):
    """Run a bot across a procedural maze board.

    This function contains external code from A4, but is significantly
    modified to account for the MazeBot's behavior.
    Link: https://cogs18.github.io/assignments/A4-ArtificialAgents/

    Parameters
    ----------
    bots : Bot() class type.
        The artificial agent to be used in the maze.
    grid_size : int, optional
        Board size.
    sleep_time : float, optional.
        Amount of time to pause between moves.
    """

    # If input is a single bot, put it in a list so that procedures work
    if not isinstance(bots, list):
        bots = [bots]

    # Update each bot to know about the grid_size they are on
    for bot in bots:
        bot.grid_size = grid_size

    # Initialize hole positions in maze to be used later
    hole_positions = hole_list_generator(grid_size)

    for bot in bots:
        # The number of moves. This prints when the maze is solved.
        n_iter = 0

        # Moves the bot across the maze until 1 iteration before completion
        while bot.position[0] != grid_size - 1:

            # Generate the maze with walls
            grid_list = build_maze_walls(grid_size)

            # Edit the maze to include predetermined holes
            for wall_list, hole_position in zip(grid_list[0::2], hole_positions):
                wall_list[hole_position] = ' '

            # Add bot(s) to the grid in certain position
            for bot in bots:
                grid_list[bot.position[0]][bot.position[1]] = bot.character

            # Clear the previous iteration, print the new grid (as a string), and wait
            clear_output(True)
            print('\n'.join([' '.join(lst) for lst in grid_list]))
            sleep(sleep_time)

            # Update bot position(s) for next turn
            for bot in bots:
                bot.move(grid_list)

            n_iter += 1

        # Moves the bot into place for the final iteration
        for bot in bots:
            bot.final_move()

            grid_list[bot.position[0] - 2][bot.position[1]] = ' '
            grid_list[bot.position[0] - 1][bot.position[1]] = bot.character

            clear_output(True)

            sleep(sleep_time)

            # Print final maze and victory messages
            print('\n'.join([' '.join(lst) for lst in grid_list]))
            print('\n', 'Congratulations! Maze completed in', n_iter, 'moves.')
            print('\n', 'Time to complete:', sleep_time * n_iter, 'seconds')