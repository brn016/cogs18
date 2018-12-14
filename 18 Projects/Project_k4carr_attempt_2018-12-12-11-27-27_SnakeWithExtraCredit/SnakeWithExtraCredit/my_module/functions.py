
# coding: utf-8

# In[ ]:

import turtle
import random
import os
from time import sleep

class food():
    def __init__ (self, foodChar, terminal):               
        self.foodChar = foodChar
        self.terminal = terminal
    def foodShape(self):
        shapes = ["arrow", "turtle", "circle", "triangle", "classic"]
        food = random.choice(shapes)
        return food
    def foodColor(self):
        colors = ["red", "blue", "green", "yellow", "orange", "purple"]
        food = random.choice(colors)
        return food
    def foodStamp(self, foodChar):
        stamp = self.foodChar.stamp
        stamp
        
        
class snake(food):
    def __init__ (self, foodChar, character, terminal):
        super().__init__(foodChar, terminal) 
        self.foodChar = foodChar
        self.character = character
        self.terminal = terminal
    def spawnSnake(self, character, terminal): 
        self.character.penup()
        self.character.shape("square")
        
        
class controls(snake):
    
    collisionCount = 0
    lengthStep = 3
    speedStep = 2
    speedBrake = 32
     
    def __init__ (self, foodChar, character, terminal):
        super().__init__(foodChar, character, terminal) 
        self.foodChar = foodChar
        self.character = character
        self.terminal = terminal
    def left(self):
        if self.character.heading()!=0:
            self.character.speed(0)
            self.character.setheading(180)
            self.character.speed(self.speedStep)  #SPEED CONTROL
    def right(self):
        if self.character.heading()!=180:
            self.character.speed(0)
            self.character.setheading(0)
            self.character.speed(self.speedStep)  #SPEED CONTROL
    def up(self):
        if self.character.heading()!=270:
            self.character.speed(0)
            self.character.setheading(90)
            self.character.speed(self.speedStep)  #SPEED CONTROL
    def down(self):
        if self.character.heading()!=90:
            self.character.speed(0)
            self.character.setheading(270)
            self.character.speed(self.speedStep)  #SPEED CONTROL
    def reset(self):
        self.character.speed(0)
        self.character.goto(0,0)
        self.character.speed(self.speedStep)
    def quit(self):
        self.terminal.bye()

        
class playGame(controls): 
    
    sList = []
    
    def __init__ (self, foodChar, character, terminal):
        super().__init__(foodChar, character, terminal) 
        self.foodChar = foodChar
        self.character = character
        self.terminal = terminal        
    def insertFood(self, foodChar):
        X = random.randrange(-self.terminal.screensize()[0]+60, self.terminal.screensize()[0]-60, 20) 
        Y = random.randrange(-self.terminal.screensize()[1]+60, self.terminal.screensize()[1]-60, 20)   
        foodPos = [X,Y]
        self.foodChar.speed(0)
        self.foodChar.penup()
        self.foodChar.setpos(foodPos)
        self.foodChar.shape(self.foodShape())
        self.foodChar.color(self.foodColor())
        self.foodStamp(self.foodChar)
    def check_bounds(self):
        if abs(self.character.position()[0]) >= abs(self.terminal.screensize()[0]-50):
            self.character.speed(0)
            self.character.hideturtle()
            self.character.goto((self.character.position()[0]*-1),self.character.position()[1])
            self.character.showturtle()
            self.character.speed(self.speedStep)  #SPEED CONTROL
        if abs(self.character.position()[1]) >= abs(self.terminal.screensize()[1]-50):
            self.character.speed(0)
            self.character.hideturtle()
            self.character.goto((self.character.position()[0]),self.character.position()[1]*-1)
            self.character.showturtle()
            self.character.speed(self.speedStep) #SPEED CONTROL
    def snakePos(self, character):
        return self.character.position()
    def foodPos(self, foodChar):
        return self.foodChar.position()
    def collisionDetect(self, foodChar, character):
        food = self.foodPos(self.foodChar)
        snake = self.snakePos(self.character)
        if round((food[0]),0) == round((snake[0]),0) and round((food[1]),0) == round((snake[1]),0):
            self.terminal.delay(0)
            self.character.speed(0)
            self.foodChar.clearstamp(self.insertFood(foodChar))
            self.collisionCounter()
            self.lengthStepper()
            self.speedStepper()
            self.terminal.delay(self.speedBrake)
            self.character.speed(self.speedStep)
    def collisionCounter(self):
        self.collisionCount += 1
        return self.collisionCount
    def lengthStepper(self):   
        if (self.collisionCount%2) == 0:
            self.lengthStep += 3
    def speedStepper(self):   
        if (self.collisionCount%10) == 0:
            self.speedBrake -= 2
    def gameOver (self):
        sPosX = round((self.character.xcor()),0)
        sPosY = round((self.character.ycor()),0)
        sPos = (sPosX, sPosY)
        if len(self.sList)>= self.lengthStep and sPos in self.sList: #This loop ends the game if the snake runs into itself
            self.character.speed(0)
            self.character.hideturtle()
            self.character.goto(0,0)
            for stamp in self.sList:
                self.character.clearstamps(1)                  
            self.character.write('Game Over', move=True, align="center", font=("Arial", 32, "bold"))
            sleep(2)
            self.terminal.bye()                
    def moveSnake(self, character, terminal): 
        self.spawnSnake(self.character, self.terminal)
        while True: 
            try:
                sPosX = round((self.character.xcor()),0)
                sPosY = round((self.character.ycor()),0)
                sPos = (sPosX, sPosY)
                self.gameOver()
                self.sList.append(sPos) #add the snake head position to the body
                self.collisionDetect(self.foodChar, self.character) #clear and add new food when snake eats        
                self.character.speed(self.speedStep)  #sets base speed of snake 
                self.terminal.delay(self.speedBrake)  #set brake on speed of snake - used to increase speed 
                self.character.forward(20)                                      
                self.character.stamp()
                if len(self.sList)>self.lengthStep:  #LENGTH CONTROL
                    self.character.clearstamps(1)
                    del(self.sList[0])
                self.check_bounds()
                self.terminal.onkey(controls(self.foodChar, self.character, self.terminal).left, "Left")
                self.terminal.onkey(controls(self.foodChar, self.character, self.terminal).right, "Right")
                self.terminal.onkey(controls(self.foodChar, self.character, self.terminal).up, "Up")
                self.terminal.onkey(controls(self.foodChar, self.character, self.terminal).down, "Down")
                self.terminal.onkey(controls(self.foodChar, self.character, self.terminal).reset, "space")
                self.terminal.onkey(controls(self.foodChar, self.character, self.terminal).quit, "q")
                self.terminal.listen() 
            except:
                os._exit(0)

def snakeGame():
    random.seed()
    turtle.setup(width=700, height=500, startx=0, starty=0)
    window = turtle.Screen() 
    window.title("Hungry Python!") 
    window.bgcolor("lightgreen")
    tess = turtle.Turtle()
    snack = turtle.Turtle()
    ssssnack = playGame(snack, tess, window)
    ssssnack.insertFood(snack)
    ssss = playGame(snack, tess, window)
    ssss.moveSnake(tess, window)
    window.mainloop()
