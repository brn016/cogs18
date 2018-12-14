import py.test

import RobotFunctions as rb

def test1():
    
    assert rb.check_bounds([5, 6], 4) == False
    assert rb.add_lists([3, 6], [4, 6]) == [7, 12]

def test2():
    bot = rb.ExploreBot()
    assert bot.name == "ExploreBot"

def test3():
    assert rb.HorizontalBot
    bot3 = rb.HorizontalBot()
    assert bot3.name == "HorizontalBot"
    rb.play_board(bot3)

def test4():
    
    assert rb.DiagonalBot
    
    bot = rb.DiagonalBot ()
    assert bot.name == 'DiagonalBot'

# test block for BotEater
def test5():
    
    assert rb.BotEater()
    
def test6():
    
    bot1 = rb.BotEater(character = 1127)
    bot2 = rb.WanderBot()
    assert bot1.name == "BotEater"

def test7():
    bot2 = rb.BotEater()
    bot2.grid_size = 5
    bots = [rb.WanderBot(), rb.ExploreBot(), rb.TeleportBot(), bot2]
    assert isinstance(bot2.move(bots), list)