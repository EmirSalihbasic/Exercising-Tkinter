# -*- coding: utf-8 -*-
"""
Created on Mon May  1 15:06:41 2023

@author: Korisnik
"""

# Text widget is similar to entry. THe difference is that we can write a text in multiple lines.
from tkinter import *

root = Tk()

text = Text(root, width=30, height=10) #This is how many lines of codes we wabt to use
text.pack()

root.mainloop()