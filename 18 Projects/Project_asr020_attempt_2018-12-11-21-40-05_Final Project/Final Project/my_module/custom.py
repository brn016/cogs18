from IPython.display import Image, display
import random

# lists of images I want the Chatbot to be able to display 
pos_images = ["img/Smiling Weenie.png", "img/Baby Hippo.jpg", "img/Fennec.png", "img/Kitty and Deer.jpg"]
word_images = ["img/Feelings.jpg", "img/Your Best.jpg", "img/Taco.png", "img/Attack .jpg"]

# list of lists;
both_images =  [pos_images, word_images] 

# def pos_pic() - External code; Prof Tom
def pos_pic():
    """  If we want an image from pos_images , choose a random one and show it """
    
    show_pos_pic = True
    if show_pos_pic:
        display(Image(random.choice(pos_images)))
        
def word_pic():
    """  If we want an image from word_images , choose a random one and show it """
    
    show_word_pic = True
    if show_word_pic: 
        display(Image(random.choice(word_images)))
          
def either_pic():
    """  If we want an image from either word_images or pos_images , choose a random one and show it """
    
    rand_images = random.choice(both_images)
    show_any_pic = True
    if show_any_pic:
        display(Image(random.choice(rand_images)))