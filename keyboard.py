import tkinter as tk
from tkinter import ttk
from tkinter import *


class Keyboard(ttk.Frame):

    def tap(self, value):
        pass

    def __init__(self, canvas):
        super().__init__(canvas)

        photo5 = PhotoImage(file="images/delete (1).png")
        photoimage5 = photo5.subsample(7, 7)

        self.btn_list = []
        first_rows = 'QWERTYUIOP'
        second_rows = 'ASDFGHJKL'
        third_rows= 'ZXCVBNM'

        first_row_frame = tk.Frame(self)
        first_row_frame.grid(row=0, column=0, sticky='ew', padx=2)
        for row_index in range(len(first_rows)):
            value=first_rows[row_index]
            self.btn_list.append(
                tk.Button(first_row_frame, text=value, command=lambda:self.tap(value), height=3,
                width=6, bg="light grey", activebackground="light grey", bd=0, font=("arial", 10, "bold"))
                                 )
            self.btn_list[-1].grid(row=0, column=row_index, padx=3, pady=3)

        second_row_frame = tk.Frame(self)
        second_row_frame.grid(row=1, column=0, sticky='ew', padx=2)
        for row_index in range(len(second_rows)):
            value = second_rows[row_index]
            self.btn_list.append(
                tk.Button(second_row_frame, text=value, height=3, width=6, bg="light grey", activebackground="light grey",
                bd=0, font=("arial", 10, "bold"))
            )
            self.btn_list[-1].grid(row=0, column=row_index, padx=3, pady=3)

        third_row_frame = tk.Frame(self)
        third_row_frame.grid(row=2, column=0, sticky='ew', padx=2)

        self.btn_list.append(
            tk.Button(third_row_frame, text="Enter", height=3, width=6, bg="light grey", activebackground="light grey",
                      bd=0, font=("arial", 10, "bold")))
        self.btn_list[-1].grid(row=0, column=0, padx=3, pady=3)

        for row_index in range(len(third_rows)):
            value = third_rows[row_index]
            self.btn_list.append(
                tk.Button(third_row_frame, text=value, height=3, width=6, bg="light grey", activebackground="light grey", bd=0
                          , font=("arial", 10, "bold"))
            )
            self.btn_list[-1].grid(row=0, column=row_index+1, padx=3, pady=3)

        self.btn_list.append(
            tk.Button(third_row_frame, image=photoimage5, height=56, width=120, bg="light grey", activebackground="light grey", bd=0))
        self.btn_list[-1].image = photoimage5
        self.btn_list[-1].grid(row=0, column=len(third_rows)+1, padx=3, pady=3)