import customtkinter as ctk
from PIL import Image
from globals import *

portfolio_chart = "/mnt/chromeos/MyFiles/Downloads/multi_stock.png"


class PortfolioPage(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        my_image = ctk.CTkImage(dark_image=Image.open(portfolio_chart),
                                      size=(500, 300))
    
        image_label = ctk.CTkLabel(self, image=my_image, text="")
        image_label.place(relx=.09, rely=.2)