import customtkinter as ctk
from PIL import Image

from globals import *

from portfolio import PortfolioPage
from stock import StockPage

ctk.set_appearance_mode("Dark")

#LEFT STOCK PANEL
class MyFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = ctk.CTkLabel(self, text="STOCKS", text_color="white", font=headerfont)
        self.label.grid(row=0, column=0, padx=80)

        button = ctk.CTkButton(self, text=" STOCK NAME", height=100, 
                               width=200, fg_color = "black", border_color=color2, border_width=2,
                               font=font, command=stock_func)
        button.grid(row=1, pady = 5)

        button = ctk.CTkButton(self, text=" STOCK NAME", height=100,
                            width=200, fg_color = "black", border_color=color2, border_width=2, 
                            font=font, command=stock_func)
        button.grid(row=2, pady = 5)

        button = ctk.CTkButton(self, text=" STOCK NAME", height=100, 
                               width=200, fg_color = "black", border_color=color2, border_width=2, 
                               font=font, command=stock_func)
        button.grid(row=3, pady = 5)



app = ctk.CTk(fg_color="black") 

container = ctk.CTkFrame(app, fg_color="black")

home_page = ctk.CTkFrame(container, fg_color="black")
portfolio_page = PortfolioPage(container, fg_color="black")
stock_page = StockPage(container, fg_color="black")

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

app.geometry(f"{screen_width}x{screen_height}")

def portfolio_func():
    portfolio_page.tkraise()

def stock_func():
    stock_page.tkraise()

def home_func():
    home_page.tkraise()

#HOME PAGE CONTENT
label = ctk.CTkLabel(home_page, text="What can I help you with?", fg_color="transparent", text_color="white", font=font)
label.place(relx=0.45, rely=0.7)

#BIG IMAGE
my_image = ctk.CTkImage(dark_image=Image.open(logo),
                                  size=(400, 300))

image_label = ctk.CTkLabel(home_page, image=my_image, text="")
image_label.place(relx=.39, rely=.3)

#CONVERSATION OPTION BUTTONS
button = ctk.CTkButton(master=app, text="OPTION 1", font=font, 
                                 fg_color = "black", border_color=color1, border_width=2, height=100, width=400)
button.place(relx=0.25, rely=0.8)

button = ctk.CTkButton(master=app, text="OPTION 2", font=font, 
                                 fg_color = "black", border_color=color1, border_width=2, height=100, width=400)
button.place(relx=0.5, rely=0.8)

button = ctk.CTkButton(master=app, text="OPTION 3", font=font, 
                                 fg_color = "black", border_color=color1, border_width=2, height=100, width=400)
button.place(relx=0.75, rely=0.8)

#TOP RIGHT TOTAL PORTFOLIO
button = ctk.CTkButton(master=app, text="PORTFOLIO VALUE", font=font, 
                                 fg_color = "black", border_color=color1, border_width=2, height=90, width=300,
                                 command=portfolio_func)
button.place(relx=0.8, rely=0.05)

#INSTANTIATE THE LEFT SCROLLER
frame = MyFrame(app, width=300, fg_color="black")
frame.pack(side="left", fill="y", padx=10, pady=10)

container.pack(side="left", fill="both", expand=True)

#HOME BUTTON
button = ctk.CTkButton(master=app, text="HOME", font=font, 
                                 fg_color = "black", border_color=color1, border_width=2, height=60, width=100,
                                 command=home_func)
button.place(relx=.2, rely=.05)

#HOME PAGE CONTAINER
home_page.place(relwidth=1, relheight=1)
portfolio_page.place(relwidth=1, relheight=1)
stock_page.place(relwidth=1, relheight=1)
home_page.tkraise()


app.mainloop()
