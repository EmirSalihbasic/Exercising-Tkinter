# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 17:35:02 2023

@author: Korisnik
"""

from tkinter import *   #all functions and variables from tkinter package

root = Tk ()   # TK constructor method to create new top level widget(element of GUI), assign it to the variable named root
Label (root, text= "Hello Tkinter!").pack()   #label with the text as a child of root window
root.mainloop()