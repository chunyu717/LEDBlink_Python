from tkinter import *

win = Tk()
win.title("Menu bar demo")


def placeholder():
    popup = Toplevel()
    popup.title("placeholder")
    # Fill the popup window with the Canvas() example image
    C = Canvas(popup, bg="blue", height=250, width=300)
    coord = 10, 50, 240, 210
    arc = C.create_arc(coord, start=0, extent=150, fill="red")
    C.pack()
    popup.mainloop()
    


menubar = Menu(win)

# Create menu entry and sub-options
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=placeholder)
filemenu.add_command(label="Save", command=placeholder)
filemenu.add_command(label="Save as...", command=placeholder)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=win.quit)
menubar.add_cascade(label="File", menu=filemenu)

# Create more menus
commandmenu = Menu(menubar, tearoff=0)
commandmenu.add_command(label="Irrigation Manager", command=placeholder)
commandmenu.add_command(label="Dog Walker", command=placeholder)
commandmenu.add_command(label="Calculator", command=placeholder)
menubar.add_cascade(label="Command", menu=commandmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="How-To", command=placeholder)
helpmenu.add_separator()
helpmenu.add_command(label="About", command=placeholder)
menubar.add_cascade(label="Help", menu=helpmenu)

# Display the menu
win.config(menu=menubar)