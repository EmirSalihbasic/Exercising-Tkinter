# -*- coding: utf-8 -*-
"""
Created on Mon May  1 01:34:02 2023

@author: Korisnik
"""



from tkinter import *
from tkinter import ttk

root = Tk()

progress = ttk.Progressbar(root, orient="horizontal", length=200)
progress.pack()
progress.config(mode = 'indeterminate')
# start moving the progress bar
progress.start()



root.mainloop()



