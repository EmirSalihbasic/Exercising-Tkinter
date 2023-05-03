# -*- coding: utf-8 -*-
"""
Created on Mon May  1 01:20:14 2023

@author: Korisnik
"""

from tkinter import *
from tkinter import ttk
root = Tk()

frame = tk.Frame(root)
frame.pack()

button1 = tk.Button(frame, text="Button 1")
button1.pack(side="left", padx=10)

button2 = tk.Button(frame, text="Button 2")
button2.pack(side="left", padx=10)

button3 = tk.Button(frame, text="Button 3")
button3.pack(side="left", padx=10)

root.mainloop()