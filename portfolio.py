import customtkinter as ctk
from globals import *

class PortfolioPage(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        button = ctk.CTkButton(master=self, text="PORT TEST")
        button.place(relx=0.65, rely=0.8)

    