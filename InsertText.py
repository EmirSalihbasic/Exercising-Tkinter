# -*- coding: utf-8 -*-
"""
Created on Mon May  1 15:15:23 2023

@author: Korisnik
"""

from tkinter import *

root = Tk()

# Create a text widget with some initial text
text = Text(root, width=30, height=10)
text.insert(END, "Hello, world!")
text.pack()

root.mainloop()