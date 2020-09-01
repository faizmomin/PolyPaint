# imports
import PIL.Image
from PIL import ImageTk
from tkinter import *

x1 = 0
y1 = 0
x2 = 0
y2 = 0

# funtions for mouse actions
def mouseDown(event):
    print ("clicked at", event.x, event.y)
    global x1, x2
    x1 = event.x
    y1 = event.y

def mouseUp(event):
    print ("released at", event.x, event.y)
    x2 = event.x
    y2 = event.y

    print(x1, y1, x2, y2)
    cropped = img.crop((x1, y1, x2, y2))
    cropped.show()

fp = open("./whale.jpg","rb")
img = PIL.Image.open(fp)
imgWidth, imgHeight = img.size

root = Tk()
imageCanvas = Canvas(root, bg="white", height=imgHeight, width=imgWidth)
imageCanvas.bind("<Button-1>", mouseDown)
imageCanvas.bind("<ButtonRelease-1>", mouseUp)
imageCanvas.pack()

whale = ImageTk.PhotoImage(PIL.Image.open(fp)) 
imageCanvas.create_image(0, 0, anchor=NW, image=whale)

root.mainloop()