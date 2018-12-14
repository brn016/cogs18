"""Test for my functions."""
from my_module.agent import add_lists, check_bounds, MazeBot, build_maze_walls, hole_list_generator


def test_hole_generator():
    output_maze = build_maze_walls(6)
    grid_list = build_maze_walls(6)
    grid_size = 6
    hole_list = hole_list_generator(grid_size)

    assert len(output_maze) == 6
    assert len(hole_list) == 3

    assert isinstance(hole_list, list)

    for item in hole_list:
        assert isinstance(item, int)


def test_check_bounds():
    """This test contains external code tests from A4, but is
    modified to also check for walls.

    Link: https://cogs18.github.io/assignments/A4-ArtificialAgents/
    """
    assert callable(check_bounds)

    grid_list = [['X', 'X', ' ', 'X', 'X'],
                 ['X', ' ', ' ', ' ', 'X'],
                 ['X', ' ', 'X', 'X', 'X'],
                 ['X', ' ', ' ', ' ', 'X'],
                 ['X', 'X', 'X', ' ', 'X']]

    assert check_bounds(grid_list, [1, 1], 5)
    assert not check_bounds(grid_list, [1, -1], 5)
    assert not check_bounds(grid_list, [1, 5], 5)

    bot = MazeBot()  # Initial position is [1, 1]

    # Moves to add to the bot's position
    move_into_wall = [0, -1]
    move_into_space = [1, 0]

    # Moves bot into wall
    invalid_position = add_lists(bot.position, move_into_wall)
    assert invalid_position == [1, 0]

    # Moves bot into empty space
    valid_position = add_lists(bot.position, move_into_space)
    assert valid_position == [2, 1]

    assert not check_bounds(grid_list, invalid_position, 5)
    assert check_bounds(grid_list, valid_position, 5)
    assert grid_list[invalid_position[0]][invalid_position[1]] == 'X'
    assert grid_list[valid_position[0]][valid_position[1]] == ' '


def test_maze_bot():
    """This test contains external code from A4's base bot class
    asserts, but is refactored and slightly modified.

    Link: https://cogs18.github.io/assignments/A4-ArtificialAgents/
    """
    assert MazeBot()

    bot = MazeBot()

    assert bot.position == [1, 1]
    assert bot.character == chr(9632)
    assert bot.moves == [[1, 0], [0, -1], [0, 1]]


def test_maze_bot_behavior():
    assert MazeBot()
    mbot = MazeBot()
    assert mbot
    assert mbot.move_prob == 0.999
    assert MazeBot(move_prob=0.999)

    # Build a sample maze of size 5 to interact with
    mbot.grid_size = 5
    grid_list = build_maze_walls(mbot.grid_size)
    hole_positions = hole_list_generator(mbot.grid_size)

    for wall_list, hole_position in zip(grid_list[0::2], hole_positions):
        wall_list[hole_position] = ' '

    # Test if the bot can move
    assert mbot.explore(grid_list)
    assert isinstance(mbot.explore(grid_list), list)
    mbot.move(grid_list)
    assert mbot.position != [1, 1]


def test_final_choice():
    """Tests if the bot moves into the final position correctly.
    The code will update the final position of the bot to be 1 row below.
    """

    # Initialize a grid of size 5
    grid_list = [['X', 'X', ' ', 'X', 'X'],
                 ['X', ' ', ' ', ' ', 'X'],
                 ['X', ' ', 'X', 'X', 'X'],
                 ['X', ' ', ' ', ' ', 'X'],
                 ['X', 'X', 'X', ' ', 'X']]

    grid_size = 5

    # Initialize test bot
    mbot = MazeBot()

    # Reassign bot position to 1 move before completion of maze
    mbot.position = [3, 4]
    assert mbot.position == [3, 4]

    # Check if the space below is empty
    assert grid_list[mbot.position[0] + 1][3] == ' '

    # Reassign bot position to the maze finish position
    mbot.final_move()

    # Check if the bot's position is a list and is accurate
    assert isinstance(mbot.position, list)
    assert mbot.position == [4, 4]



