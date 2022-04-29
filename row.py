import tkinter as tk
from tkinter import ttk
from tkinter import *


class Row(ttk.Frame):

    def __init__(self, canvas):
        super().__init__(canvas)

        self.first = tk.StringVar()
        self.second = tk.StringVar()
        self.third = tk.StringVar()
        self.fourth = tk.StringVar()
        self.fifth = tk.StringVar()

        self.first_entry = Entry(self, textvariable=self.first, width="10", bg="white")
        self.first_entry.grid(row=0, column=0, padx=5, pady=5, ipady=20)

        self.second_entry = Entry(self, textvariable=self.second, width="10", bg="white")
        self.second_entry.grid(row=0, column=1, padx=5, pady=5, ipady=20)

        self.third_entry = Entry(self, textvariable=self.third, width="10", bg="white")
        self.third_entry.grid(row=0, column=2, padx=5, pady=5, ipady=20)

        self.fourth_entry = Entry(self, textvariable=self.fourth, width="10", bg="white")
        self.fourth_entry.grid(row=0, column=3, padx=5, pady=5, ipady=20)

        self.fifth_entry = Entry(self, textvariable=self.fifth, width="10", bg="white")
        self.fifth_entry.grid(row=0, column=4, padx=5, pady=5, ipady=20)