# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 23:53:39 2023

@author: Korisnik
"""

from tkinter import *
from tkinter import ttk

class HelloApp:

    def __init__(self, master):

        self.label = ttk.Label(master, text = "Hello, Tkinter!")
        self.label.grid(row = 0, column = 0, columnspan = 3)
        
        ttk.Button(master, text = "Texas",
                   command = self.texas_hello).grid(row = 1, column = 0)

        ttk.Button(master, text = "Hawaii",
                   command = self.hawaii_hello).grid(row = 1, column = 1)
        
        ttk.Button(master, text = "New York",
                   command = self.newyork_hello).grid(row = 1, column = 2)

    def texas_hello(self):
        self.label.config(text = 'Howdy, Tkinter!')

    def hawaii_hello(self):
        self.label.config(text = 'Aloha, Tkinter!')

    def newyork_hello(self):
        self.label.config(text = 'Ayo, Tkinter!')

            
def main():            
    
    root = Tk()
    app = HelloApp(root)
    root.mainloop()
    
if __name__ == "__main__": main()