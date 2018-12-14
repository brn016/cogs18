
# coding: utf-8

# In[3]:


import turtle
from my_module.functions import food, snake, controls, playGame, snakeGame

tess = turtle.Turtle()
tess.hideturtle()
snack = turtle.Turtle()
snack.hideturtle()
window = turtle.Screen()

foodClass = food(snack, window)
snakeClass = snake(snack, tess, window)
controlsClass = controls(snack, tess, window)
playGameClass = playGame(snack, tess, window)

def test_foodClass():
    
    assert foodClass.foodShape()
    assert callable (foodClass.foodShape)
    assert isinstance(foodClass.foodShape(), str)

    assert foodClass.foodColor()
    assert callable (foodClass.foodColor)
    assert isinstance(foodClass.foodColor(), str)

    assert callable (foodClass.foodStamp)

def test_snakeClass():
    assert isinstance(snakeClass, snake)

    assert snakeClass.foodChar == snack
    assert snakeClass.character == tess
    assert snakeClass.terminal == window

    assert callable (snakeClass.spawnSnake)

def test_controlsClass():
    assert isinstance(controlsClass, controls)

    assert isinstance(controlsClass.collisionCount, int)
    assert controlsClass.collisionCount == 0

    assert isinstance(controlsClass.lengthStep, int)
    assert controlsClass.lengthStep == 3

    assert isinstance(controlsClass.speedStep, int)
    assert controlsClass.speedStep == 2

    assert isinstance(controlsClass.speedBrake, int)
    assert controlsClass.speedBrake == 32

    assert callable (controlsClass.left)

    assert callable (controlsClass.right)

    assert callable (controlsClass.up)

    assert callable (controlsClass.down)

    assert callable (controlsClass.reset)

    assert callable (controlsClass.quit)

def test_playGameClass():
    assert isinstance(playGameClass, playGame)
    assert playGameClass.foodChar == snack
    assert playGameClass.character == tess
    assert playGameClass.terminal == window


    assert isinstance (playGameClass.sList, list)
    assert callable (playGameClass.insertFood)
    assert callable (playGameClass.check_bounds)
    assert callable (playGameClass.snakePos)
    assert playGameClass.snakePos(tess) ==(0,0)
    assert playGameClass.foodPos(snack) ==(0,0)
    assert callable (playGameClass.foodPos)
    assert callable (playGameClass.collisionDetect)
    assert callable (playGameClass.collisionCounter)

    assert callable (playGameClass.lengthStepper)

    assert callable (playGameClass.speedStepper)
    assert callable (playGameClass.gameOver)
    assert callable (playGameClass.moveSnake)

