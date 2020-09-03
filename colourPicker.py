# Allows user to select 4/6 colours using Tkinter

# Imports tkinter modules
from tkinter import *
from tkinter import colorchooser

# Some gross globals
colour_Base = ["#ffffff","#ffffff","#ffffff","#ffffff","#ffffff","#ffffff"] # Default white
not_end = True

# choose_color(colourNum): Gets a colour in #HEX format
#	colourNum (int) is one of the 6 colours
def choose_color(colourNum): 

	# Gets RBG and HEX
	chosen = colorchooser.askcolor(title ="Choose colour #" + str(colourNum + 1) + "!")

	# Takes Hex
	colour_Base[colourNum] = chosen[1]

	# Refreshes canvas with new colour(s)
	root.destroy()

# distinct(): Checks if colour_Base contains all unique colours, returns T/F
def distinct():
	flag = 0
	
	# Big brain check for uniqueness
	flag = len(set(colour_Base)) == len(colour_Base) 

	return flag

# close_window(): stops the program from refreshing the canvas
def close_window():	
	global not_end
	not_end = False
	root.destroy()


# Refresh every action
while (not_end):
	# New canvas
	root = Tk()

	# Just checking changes of colours in output
	if (not_end):
		print(colour_Base)
	else :
		break
	
	# 6 colour buttons coloured based on the chosen colours
	button0 = Button(root, text = "Select color #1", bg = colour_Base[0],
					command = lambda: choose_color(0))
	button0.grid(row=1, column=0)

	button1 = Button(root, text = "Select color #2",bg = colour_Base[1],
					command = lambda: choose_color(1))
	button1.grid(row=1, column=1)

	button2 = Button(root, text = "Select color #3",bg = colour_Base[2],
					command = lambda: choose_color(2))
	button2.grid(row=1, column=2)

	button3 = Button(root, text = "Select color #4",bg = colour_Base[3],
					command = lambda: choose_color(3))
	button3.grid(row=1, column=3)

	button4 = Button(root, text = "Select color #5",bg = colour_Base[4],
					command = lambda: choose_color(4))
	button4.grid(row=1, column=4)

	button5 = Button(root, text = "Select color #6", bg = colour_Base[5],
					command = lambda: choose_color(5))
	button5.grid(row=1, column=5)

	# If all 6 colours are distinct, we are ready to submit
	if (distinct()):
		button_End = Button(root, text = "Submit", bg = "#FFF",
						command = lambda: close_window())
	# Otherwise, we can save our changes (just refreshes the canvas)
	else :
		button_End = Button(root, text = "Save changes", bg = "#FFF",
						command = lambda: root.destroy())
	button_End.grid(row=3, column=6)

	# Creates canvas
	root.mainloop() 

