# -*- coding: utf-8 -*-
"""
Created on Mon May  1 01:22:25 2023

@author: Emir
"""

#create a widget to enter the text with entry.

from tkinter import *
from tkinter import ttk

root = Tk()

entry = ttk.Entry(root,width=30)
entry.pack()

root.mainloop()