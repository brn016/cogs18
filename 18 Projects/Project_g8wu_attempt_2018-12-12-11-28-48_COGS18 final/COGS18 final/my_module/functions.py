from math import sqrt
from skimage import data
import matplotlib.pyplot as plt
from PIL import Image, ImageTk

from tkinter.filedialog import askopenfilename
from tkinter import *

class imagePath():
    
    def __init__(self, master = None):
        self.master = master
        self.init_window()       # Start GUI window
        
    def init_window(self):
        """Intitialize GUI window using tkinter. Request user input of image file."""
        root = Tk()
        root.title("Image Pathing")
        image_File = ""             # Global container for filepath

        # Button to import image
        imgBrowse = Button(root, text="Import image",command = self.getImg)
        imgBrowse.pack(side = LEFT)
        
        root.mainloop()
    
    def getImg(self):
        """Prompts user with File Explorer to select image. 
        A Tkinter window is used to initiate but is withdrawn to show only File Explorer.
        Passes image filepath to global container image_File."""
        Tk().withdraw()
        image_File = askopenfilename()
        
        # Prints image filepath to terminal if successfully imported
        print(image_File)
        
        
        
        return (image_File)
        
    