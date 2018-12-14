"""Test for my functions."""

from functions import change_speed, Bot, DiagBot, BounceBot, SquareBot

##
##

def test_change_speed():
    
    assert isinstance(change_speed(0.3, []), float)
    assert change_speed(0.3, []) == 0.3 - 0.01
    assert change_speed(0.1, [0.04]) == 0.1 + 0.01
    assert change_speed(0.04, []) == 0.04 + 0.01
    
def test_diagbot():
    
    assert DiagBot
    
    diag_bot = DiagBot()
    diag_bot.grid_size = 10
    
    assert isinstance(diag_bot, DiagBot)
    assert isinstance(diag_bot.position, list)
    assert isinstance(diag_bot.moves, list)
    assert isinstance(diag_bot.grid_size, int)
    
    assert diag_bot.diag()
    assert isinstance(diag_bot.diag(), list)
    diag_bot.move()
    assert diag_bot.position != [0, 0]
    
def test_bouncebot():
    
    assert BounceBot
    
    bounce_bot = BounceBot()
    bounce_bot.grid_size = 10
    
    assert isinstance(bounce_bot, BounceBot)
    assert isinstance(bounce_bot.position, list)
    assert isinstance(bounce_bot.moves, list)
    assert isinstance(bounce_bot.grid_size, int)
    assert bounce_bot.move_var == 0
    
    assert bounce_bot.bounce()
    assert isinstance(bounce_bot.bounce(), list)
    bounce_bot.move()
    assert bounce_bot.position != [0, 0]
    
def test_squarebot():
    
    assert SquareBot
    
    square_bot = SquareBot()
    square_bot.grid_size = 10
    
    assert isinstance(square_bot, SquareBot)
    assert square_bot.move_var == 1
    assert isinstance(square_bot.position, list)
    assert isinstance(square_bot.moves, list)
    assert isinstance(square_bot.grid_size, int)
    assert isinstance(square_bot.move_list, list)
    
    assert square_bot.square()
    assert isinstance(square_bot.square(), list)
    square_bot.move()
    assert square_bot.position != [0, 0]
    
