# colourPicker
# Sets up a GUI for users to pick 4 colours of their choice.
# Automatically chooses the most common colour and an overall 
# colour of the entire picture.


# imports
from tkinter import *
from tkinter import choosecolor 
  
# Function that will be invoked when the 
# button will be clicked in the main window 
def choose_color(): 
  
    # variable to store hexadecimal code of color 
    color_code = colorchooser.askcolor(title ="Choose color")  
    print(color_code) 
  
root = Tk() 
button = Button(root, text = "Select color", 
                   command = "choose_color") 
button.pack() 
root.geometry("300x300") 
root.mainloop() 