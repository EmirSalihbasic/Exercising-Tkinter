# -*- coding: utf-8 -*-
"""
Created on Mon May  1 15:38:47 2023

@author: Korisnik
"""

import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Create a Treeview widget
tree = ttk.Treeview(root)
tree["columns"] = ("Name", "Salary")

# Define the columns
tree.column("#0", width=50, minwidth=50)
tree.column("Name", width=150, minwidth=150)
tree.column("Salary", width=50, minwidth=50)

# Define the column headings
tree.heading("#0", text="ID")
tree.heading("Name", text="Name")
tree.heading("Salary", text="Salary")

# Insert some sample data
tree.insert("", tk.END, text="1", values=("John", "2500"))
tree.insert("", tk.END, text="2", values=("Jane", "3000"))
tree.insert("", tk.END, text="3", values=("Bob", "4500"))

# Pack the Treeview widget
tree.pack()

root.mainloop()