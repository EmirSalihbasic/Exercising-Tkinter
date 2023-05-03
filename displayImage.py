# -*- coding: utf-8 -*-
"""
Created on Mon May  1 00:26:20 2023

@author: Korisnik
"""

from tkinter import *
from tkinter import ttk

root = Tk()
label = ttk.Label (root, text = "Hello Tkinter!")
label.pack()
label.config(text = "Howdy Tkinter")
label.config(text = "Howdy Tkinter! It\'s been a while since we last met. Great to see you again")
label.config(wraplength = 150)
label.config(justify = CENTER)
label.config(foreground = 'blue')
label.config(font = ('Courier',18,'bold'))
label.config(text = "Howdy Tkinter")

PhotoImage(file = 'C:/Users/Korisnik/Desktop/Ex_Files_Python_GUI_Dev_Tkinter/Ex_Files_Python_GUI_Dev_Tkinter/Exercise Files/Ch03/python_logo.gif' )
logo = PhotoImage(file = 'C:/Users/Korisnik/Desktop/Ex_Files_Python_GUI_Dev_Tkinter/Ex_Files_Python_GUI_Dev_Tkinter/Exercise Files/Ch03/python_logo.gif' )
label.config (image = logo)
label.config (compound = 'text')
label.config (compound = 'center')
label.config (compound = 'left')
label.img = logo
label.config (image = label.img)