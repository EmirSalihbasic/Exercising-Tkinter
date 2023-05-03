# -*- coding: utf-8 -*-
"""
Created on Mon May  1 17:38:32 2023

@author: Korisnik
"""

from tkinter import *
root = Tk()

canvas = Canvas(root, width=400, height=400)

rectangle = canvas.create_rectangle(50, 50, 150, 150, fill='red')
line = canvas.create_line(0, 0, 400, 400, fill='blue', width=5)

canvas.pack()
root.mainloop()