import tkinter as tk
from tkinter import ttk
from tkinter import *
from row import Row
from keyboard import Keyboard


class Display(ttk.Frame):

    def __init__(self, canvas):
        super().__init__(canvas)

        self.dict_for_row = {}

        for i in range(0,6,1):
            self.dict_for_row[i] = Row(self)
            self.dict_for_row[i].grid(row=i + 1, column=0, sticky="N")
            self.dict_for_row[i].rowconfigure(i, weight=1)
            self.dict_for_row[i].columnconfigure(i, weight=1)

        keyboard = Keyboard(self)
        keyboard.grid(row=6, column=0, sticky="S")