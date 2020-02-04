## Demonstrate a small list-style menu with mouse-click events
from tkinter import *
import tkinter.font

### GUI DEFINITIONS ###
win = Tk()
win.title("List menu demo")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

menuFrame = Frame(win)
menuFrame.pack(side = LEFT)
irrFrame = Frame(win)
dogFrame = Frame(win)
calcFrame = Frame(win)

### EVENT FUNCTIONS ###
def buttonPress(): # Placeholder button event
    print("Button Pressed")


def callback(event):
    print("clicked at", event.x, event.y)


def menuManage(dummy): # Manage what options are visible
    # Start by hiding all buttons
    sel = Lb.curselection()
    irrFrame.pack_forget()
    dogFrame.pack_forget()
    calcFrame.pack_forget()

    # Show the relevant buttons depending on list selection
    if sel[0] == 0:
        irrFrame.pack(side=RIGHT)
    elif sel[0] == 1:
        dogFrame.pack(side=RIGHT)
    elif sel[0] == 2:
        calcFrame.pack(side=RIGHT)



### WIDGETS ###

# Listbox for text-item selection
Lb = Listbox(menuFrame)
Lb.insert(1,"Irrigation Controller")
Lb.insert(2,"Dog Walker")
Lb.insert(3,"Calculator")
Lb.bind("<Double-Button-1>", menuManage) # Attach double-click event
##Lb.bind("<Double-Button-1>", callback) # Try running this line instead of the above
Lb.pack()

# Placeholder buttons for functionality
irrOn = Button(irrFrame, text='On', font=myFont, command=buttonPress, bg='bisque2', height=1)
irrOff = Button(irrFrame, text='Off', font=myFont, command=buttonPress, bg='bisque2', height=1)
irrOn.pack(side = TOP)
irrOff.pack(side = BOTTOM)

dogOn = Button(dogFrame, text='Walk', font=myFont, command=buttonPress, bg='bisque2', height=1)
dogOff = Button(dogFrame, text='No-Walk', font=myFont, command=buttonPress, bg='bisque2', height=1)
dogOn.pack(side = TOP)
dogOff.pack(side = BOTTOM)

calcPlus = Button(calcFrame, text='+', font=myFont, command=buttonPress, bg='bisque2', height=1)
calcMinus = Button(calcFrame, text='-', font=myFont, command=buttonPress, bg='bisque2', height=1)
calcPlus.pack(side = TOP)
calcMinus.pack(side = BOTTOM)

win.mainloop()