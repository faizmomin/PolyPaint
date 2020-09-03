# Allows user to select 4/6 colours.

# importing tkinter module 
from tkinter import *
from tkinter import colorchooser

colour_Base = ["#ffffff","#ffffff","#ffffff","#ffffff","#ffffff","#ffffff"]

# choose_color(): Gets a colour in #HEX format
#	colourNum (int) is one of the 6 colours
def choose_color(colourNum): 
	chosen = colorchooser.askcolor(title ="Choose colour #" + str(colourNum + 1) + "!")
	colour_Base[colourNum] = chosen[1]
	return chosen[1]

# New canvas
root = Tk()

button_End = Button(root, text = "Confirm",
				command = lambda: root.destroy())
button_End.grid(row=2, column=0)

root.mainloop() 
