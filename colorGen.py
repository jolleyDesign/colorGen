# colorGen.py
# RGB color generator and displayer

import random
from tkinter import *
from tkinter import ttk

redValue = random.randint(0,256)
greenValue = random.randint(0,256)
blueValue = random.randint(0,256)

# converting RGB to HEX

hexVal = "%02x%02x%02x" % (redValue, greenValue, blueValue)
hexVal = "#" + hexVal.upper()
print(hexVal)

window = Tk()
window.geometry("500x500")
window.config(background=hexVal)

label = ttk.Label(window, text=hexVal, background="white", foreground="black")
label.place(relx=.5, rely=.5, anchor=CENTER)

window.mainloop()