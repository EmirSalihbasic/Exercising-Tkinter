# -*- coding: utf-8 -*-
"""
Created on Mon May  1 18:09:39 2023

@author: Korisnik
"""

import tkinter as tk
from tkinter import filedialog


root = tk.Tk()   # Create the root window
root.geometry("300x300")


def get_file():   #function for a file
    file_path = filedialog.askopenfilename()
    print(file_path)

button = tk.Button(root, text="Open File", command=get_file)  #create a button
button.pack()

# Start the main loop
root.mainloop()