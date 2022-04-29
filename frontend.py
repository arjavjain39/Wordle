import tkinter as tk
import tkinter.font as font
from tkinter import ttk
from container import Container
from display import Display


class Window(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("WORDLE GAME")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        font.nametofont("TkDefaultFont").configure(size=12)

        main_frame = tk.Frame(self)
        main_frame.grid(row=0, column=0, sticky="NSEW")
        main_frame.rowconfigure((1), weight=1)
        main_frame.columnconfigure(0, weight=1)

        container = Container(main_frame)
        container.grid(row=0,column=0, sticky="NSEW")
        container.rowconfigure(0, weight=0)
        container.columnconfigure(2, weight=1)

        display = Display(main_frame)
        display.grid(row=1, column=0, sticky="NS", pady=5)
        display.rowconfigure(6, weight=1)
        display.columnconfigure(0, weight=1)


root = Window()
root.mainloop()