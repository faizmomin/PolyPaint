# Allows user to select 4/6 colours.

# importing tkinter module 
from tkinter import *
from tkinter import colorchooser

colour_Base = ["#ffffff","#ffffff","#ffffff","#ffffff","#ffffff","#ffffff"]
not_end = True

# choose_color(): Gets a colour in #HEX format
#	colourNum (int) is one of the 6 colours
def choose_color(colourNum): 
	chosen = colorchooser.askcolor(title ="Choose colour #" + str(colourNum + 1) + "!")
	colour_Base[colourNum] = chosen[1]
	root.destroy()

# distinct(): Checks if colour_Base contains all unique colours, returns T/F
def distinct():
	flag = 0
	
	# using set() + len() 
	# to check all unique list elements 
	flag = len(set(colour_Base)) == len(colour_Base) 
	return flag


def close_window():	
	global not_end
	not_end = False
	root.destroy()

# Refresh every action
while (not_end):

	root = Tk()

	if (not_end):
		print(colour_Base)
	else :

		break
	
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

	if (distinct()):
		button_End = Button(root, text = "Submit", bg = "#FFF",
						command = lambda: close_window())
		
	else :
		button_End = Button(root, text = "Save changes", bg = "#FFF",
						command = lambda: root.destroy())

	button_End.grid(row=3, column=6)

	root.mainloop() 


print("done")