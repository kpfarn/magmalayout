import customtkinter as ctk
from PIL import Image
from globals import *

stock_chart = "/mnt/chromeos/MyFiles/Downloads/single_stock.png"

class StockPage(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        label = ctk.CTkLabel(self, text="STOCK NAME: STOCK", fg_color="transparent", text_color="white", font=font)
        label.place(relx=0.13, rely=0.51)

        my_image = ctk.CTkImage(dark_image=Image.open(stock_chart),
                                  size=(500, 300))

        image_label = ctk.CTkLabel(self, image=my_image, text="")
        image_label.place(relx=.05, rely=.2)

        box = ctk.CTkTextbox(self, width=800, height=600, 
                             font=font, border_color=color1, border_width=2)
        box.insert("0.0", "Example text, this is where the llm conversation replies land\n" * 50)
        box.place(relx=0.42, rely=0.18)

        