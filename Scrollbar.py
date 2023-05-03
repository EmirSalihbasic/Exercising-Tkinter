# -*- coding: utf-8 -*-
"""
Created on Mon May  1 17:22:55 2023

@author: Korisnik
"""
import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

# Create a scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a text widget
text_widget = tk.Text(root, yscrollcommand=scrollbar.set)
text_widget.pack(side=tk.LEFT, fill=tk.BOTH)

# Configure the scrollbar to scroll the text widget
scrollbar.config(command=text_widget.yview)

root.mainloop()