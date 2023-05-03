# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 18:00:49 2023

@author: Korisnik
"""

from tkinter import *
from tkinter import ttk

root = Tk ()
button = ttk.Button(root, text = 'Click me')
button.pack()
button['text'] = 'Press me'

button.config(text = 'Push me')

str(button)

str(root)

ttk.Label(root, text = 'Hello Tkinter').pack()