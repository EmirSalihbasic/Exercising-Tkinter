# -*- coding: utf-8 -*-
"""
Created on Mon May  1 17:14:16 2023

@author: Korisnik
"""

import tkinter as tk

root = tk.Tk()

# Create a menu bar
menu_bar = tk.Menu(root)

# Create a "File" menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Save")
file_menu.add_command(label="Save As")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create an "Edit" menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")

# Create a "Settings" menu
settings_menu = tk.Menu(menu_bar, tearoff=0)
settings_menu.add_command(label="Preferences")

# Add the menus to the menu bar
menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
menu_bar.add_cascade(label="Settings", menu=settings_menu)

# Attach the menu bar to the root window
root.config(menu=menu_bar)

root.mainloop()