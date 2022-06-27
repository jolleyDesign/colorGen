# colorGen.py
# RGB color generator and displayer

import random
from tkinter import *
from tkinter import ttk

redValue = random.randint(0,256)
greenValue = random.randint(0,256)
blueValue = random.randint(0,256)

# defining newButton function
## definitely a simpler way to incorporate this, just lazy right now

def newColor():
    redValue = random.randint(0,256)
    greenValue = random.randint(0,256)
    blueValue = random.randint(0,256)
    hexVal = "%02x%02x%02x" % (redValue, greenValue, blueValue)
    hexVal = "#" + hexVal.upper()
    print(hexVal)

    window.title(hexVal)
    window.geometry("500x500")
    window.config(background=hexVal)
    
    entryLabel = Entry(window, bg="white", fg="black")
    entryLabel.place(relx=.5, rely=.5, anchor=CENTER)
    entryLabel.insert(0, hexVal)
    entryLabel.configure(state="readonly", justify="center")


# converting RGB to HEX

hexVal = "%02x%02x%02x" % (redValue, greenValue, blueValue)
hexVal = "#" + hexVal.upper()
print(hexVal)

window = Tk()
window.title(hexVal)
window.geometry("500x500")
window.config(background=hexVal)

entryLabel = Entry(window, bg="white", fg="black")
entryLabel.place(relx=.5, rely=.5, anchor=CENTER)
entryLabel.insert(0, hexVal)
entryLabel.configure(state="readonly", justify="center")

newButton = Button(window, text="New color", background="white", command=newColor)
newButton.place(relx=.5, rely=.8, anchor=CENTER)

window.mainloop()
