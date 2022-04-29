import tkinter
from tkinter import *
from tkinter import ttk


class Container(ttk.Frame):

    def no_operation(self):
        pass

    def __init__(self, canvas):
        super().__init__(canvas)

        photo1 = PhotoImage(file="images/menu.png")
        photo2 = PhotoImage(file=r"images/question (3).png")
        photo3 = PhotoImage(file=r"images/graph.png")
        photo4 = PhotoImage(file=r"images/setting.png")

        photoimage1 = photo1.subsample(6, 6)
        photoimage2 = photo2.subsample(9, 9)
        photoimage3 = photo3.subsample(6, 6)
        photoimage4 = photo4.subsample(6, 6)

        menu_button = Button(
            self, image=photoimage1, command=lambda:self.no_operation(), bg="white", height=40, width=40,
            relief="flat", activebackground="white", bd=0
        )
        menu_button.image = photoimage1
        menu_button.grid(row=0, column=0, sticky="ns")

        question_button = Button(
            self, image=photoimage2, command=lambda:self.no_operation(), bg="white", height=40, width=40,
            relief="flat", activebackground="white", bd=0
        )
        question_button.image = photoimage2
        question_button.grid(row=0, column=1, sticky="ns")

        game_label = Label(
            self, text="Wordle", bg="white", fg="black", font=("times new roman", 30, "bold")
        )
        game_label.grid(row=0, column=2, sticky="ew")

        stats_button = Button(
            self, image=photoimage3, command=lambda:self.no_operation(), bg="white", height=40, width=40,
            relief="flat", activebackground="white", bd=0
        )
        stats_button.image = photoimage3
        stats_button.grid(row=0, column=3, sticky="ns")

        setting_button = Button(
            self, image=photoimage4, command=lambda:self.no_operation(), bg="white", height=40, width=40,
            relief="flat", activebackground="white", bd=0
        )
        setting_button.image = photoimage4
        setting_button.grid(row=0, column=4, sticky="ns")

        sep = ttk.Separator(self, orient="horizontal")
        sep.grid(sticky="ew", columnspan=5)