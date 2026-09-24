import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("Dark")

#GLOBAL DEFAULTS
headerfont = ("arial", 32)
font = ("arial", 20)
color1 = "RED"
color2 = "DARK ORANGE"
logo = "/mnt/chromeos/MyFiles/Downloads/magmaLogo.png"


#LEFT STOCK PANEL
class MyFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = ctk.CTkLabel(self, text="PORTFOLIO", text_color="white", font=headerfont)
        self.label.grid(row=0, column=0, padx=50)

        button = ctk.CTkButton(self, text=" STOCK NAME", height=100, width=200, fg_color = color2, font=font)
        button.grid(row=1, pady = 5)

        button = ctk.CTkButton(self, text=" STOCK NAME", height=100, width=200, fg_color = color2, font=font)
        button.grid(row=2, pady = 5)

        button = ctk.CTkButton(self, text=" STOCK NAME", height=100, width=200, fg_color = color2, font=font)
        button.grid(row=3, pady = 5)



app = ctk.CTk(fg_color="black") 

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

app.geometry(f"{screen_width}x{screen_height}")

def button_function():
    portfolio_page.tkraise()

def back_function():
    main_page.tkraise()

#PAGE CONTAINER (right of stock panel)
container = ctk.CTkFrame(app, fg_color="black")
container.pack(side="left", fill="both", expand=True)

main_page = ctk.CTkFrame(container, fg_color="black")
portfolio_page = ctk.CTkFrame(container, fg_color="black")
main_page.grid(row=0, column=0, sticky="nsew")
portfolio_page.grid(row=0, column=0, sticky="nsew")
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

#HOME PAGE (MAIN)
#LABEL TO INDICATE ACTION
label = ctk.CTkLabel(main_page, text="What can I help you with?", fg_color="transparent", text_color="white", font=font)
label.place(relx=0.55, rely=0.7)

#BIG IMAGE
my_image = ctk.CTkImage(light_image=Image.open(logo),
                                  dark_image=Image.open(logo),
                                  size=(400, 300))

image_label = ctk.CTkLabel(main_page, image=my_image, text="")
image_label.place(relx=.5, rely=.3)

#CONVERSATION OPTION BUTTONS
button = ctk.CTkButton(master=main_page, text="OPTION 1", font=font, 
                                 fg_color=color1, height=100, width=400)
button.place(relx=0.25, rely=0.8)

button = ctk.CTkButton(master=main_page, text="OPTION 2", font=font, 
                                 fg_color=color1, height=100, width=400)
button.place(relx=0.5, rely=0.8)

button = ctk.CTkButton(master=main_page, text="OPTION 3", font=font, 
                                 fg_color=color1, height=100, width=400)
button.place(relx=0.75, rely=0.8)

#TOP RIGHT TOTAL PORTFOLIO
button = ctk.CTkButton(master=main_page, text="PORTFOLIO VALUE", font=font, 
                                 fg_color=color1, height=90, width=300, command=button_function)
button.place(relx=0.8, rely=0.05)

#PORTFOLIO PAGE
pf_label = ctk.CTkLabel(portfolio_page, text="PORTFOLIO", text_color="white", font=headerfont)
pf_label.place(relx=0.5, rely=0.3, anchor="center")

back_button = ctk.CTkButton(master=portfolio_page, text="BACK", font=font,
                            fg_color=color1, height=60, width=200, command=back_function)
back_button.place(relx=0.5, rely=0.5, anchor="center")

#INSTANTIATE THE LEFT SCROLLER
frame = MyFrame(app, width=300, fg_color="black")
frame.pack(side="left", fill="y", padx=10, pady=10)


app.mainloop()