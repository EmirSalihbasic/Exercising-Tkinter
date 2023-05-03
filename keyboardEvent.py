# -*- coding: utf-8 -*-
"""
Created on Mon May  1 22:59:34 2023

@author: Korisnik
"""

import tkinter as tk

def on_enter_pressed(event):
    # Code to be executed when Enter key is pressed
    print("Enter key pressed")

root = tk.Tk()

# Create a text widget
text_widget = tk.Text(root)
text_widget.pack()

# Bind the Enter key to the on_enter_pressed function
text_widget.bind("<Return>", on_enter_pressed)

root.mainloop()