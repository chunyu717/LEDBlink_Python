from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

### HARDWARE DEFINITIONS ###
# LED pin definitions
led0 = LED(7)
led1 = LED(8)
led2 = LED(25)
led3 = LED(23)
led4 = LED(24)
led5 = LED(18)
led6 = LED(15)
led7 = LED(14)
# Arrange LEDs into a list
leds = [led7,led6,led5,led4,led3,led2,led1,led0]

### GUI DEFINITIONS ###
win=Tk()
win.title("LED Controller")
myFont=tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")
ledCode = StringVar()


### Event Functions ###
def ledShow():
    ledCode = code.get()
    print("LED code: ", ledCode) #Debug

    i=0 #loop-counter
    # For each character in the ledCode string, check if = 1 and if so,
    # turn on the corresponding LED
    for c in ledCode:
        if c == "1":
            leds[i].on()
        else:
            leds[i].off()
        i+=1

def close(): # Cleanly close the GUI and cleanup the GPIO
    RPi.GPIO.cleanup()
    win.destroy()


### WIDGETS ###

ledButton = Button(win, text='Load LED code', font=myFont, command=ledShow, bg='bisque2', height=1)
ledButton.grid(row=0,column=1)

code = Entry(win, font=myFont, width=10)
code.grid(row=0,column=0)

exitButton = Button(win, text='Exit', font=myFont, command=close, bg='red', height=1, width=6)
exitButton.grid(row=3,column=1, sticky=E)

win.protocol("WM_DELETE_WINDOW", close) # cleanup GPIO when user closes window

win.mainloop() # Loops forever