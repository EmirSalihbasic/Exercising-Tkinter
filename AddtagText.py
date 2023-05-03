# -*- coding: utf-8 -*-
"""
Created on Mon May  1 15:26:17 2023

@author: Korisnik
"""

from tkinter import *

root = Tk()


text = Text(root, width=30, height=10)
text.insert(END, "Hello, world!")
text.pack()


text.tag_add("first_word", "1.0", "1.5")
text.tag_config("first_word", foreground="blue")

root.mainloop()