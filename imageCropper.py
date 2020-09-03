# imageCropper
# Tool that allows user to crop the chosen image

# imports
import PIL.Image
from PIL import ImageTk
from tkinter import *
import sys

# global variables used for cropping coordinates
x1 = 0
y1 = 0
x2 = 0
y2 = 0

# funtions for mouse actions
def mouseDown(event):
    #print ("clicked at", event.x, event.y)
    global x1,y1
    x1 = event.x
    y1 = event.y

def mouseUp(event):
    #print ("released at", event.x, event.y)
    global x1,y1,x2,y2
    x2 = event.x
    y2 = event.y
    cropImage(x1, x2, y1, y2)
    x1, y1, x2, y2 = 0, 0, 0, 0
    imageCanvas.coords(cursor_rect, 0, 0, 0, 0)

def mouseMove(event):
    global cursor_rect, imageCanvas, x1, y1
    imageCanvas.coords(cursor_rect, x1, y1, event.x, event.y)

# functions that is used to crop image
def cropImage(x1, x2, y1, y2):
    #print(x1, y1, x2, y2)
    if(y2 < y1):
        temp = x1
        x1 = x2
        x2 = temp
        temp = y1
        y1 = y2
        y2 = temp
    
    # crops image
    cropped = img.crop((min(x1,x2), min(y1,y2), max(x1,x2), max(y1,y2)))
    cropped.show()
    return cropped

# opens image file
imageFile = "./whale.jpg"
if(len(sys.argv) == 2):
    imageFile = "./" + sys.argv[1]
fp = open(imageFile,"rb")
img = PIL.Image.open(fp)
imgWidth, imgHeight = img.size

# creates a canvas to display image
root = Tk()
imageCanvas = Canvas(root, bg="white", height=imgHeight, width=imgWidth)
imageCanvas.bind("<Button-1>", mouseDown)
imageCanvas.bind("<ButtonRelease-1>", mouseUp)
imageCanvas.bind("<B1-Motion>", mouseMove)
imageCanvas.pack()

whale = ImageTk.PhotoImage(PIL.Image.open(fp)) 
imageCanvas.create_image(0, 0, anchor=NW, image=whale)
cursor_rect = imageCanvas.create_rectangle(0,0,0,0)

root.mainloop()