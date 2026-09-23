import customtkinter as ctk

ctk.set_appearance_mode("Dark")

#GLOBAL DEFAULTS
headerfont = ("arial", 32)
font = ("arial", 20)
color1 = "RED"
color2 = "DARK ORANGE"


#LEFT STOCK PANEL
class MyFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = ctk.CTkLabel(self, text="PORTFOLIO", text_color="white", font=headerfont)
        self.label.grid(row=0, column=0, padx=20)

        button = ctk.CTkButton(self, text=" STOCK NAME", height=40, fg_color = color2)
        button.grid(row=1, pady = 5)

        button = ctk.CTkButton(self, text=" STOCK NAME", height=40, fg_color = color2)
        button.grid(row=2, pady = 5)

        button = ctk.CTkButton(self, text=" STOCK NAME", height=40, fg_color = color2)
        button.grid(row=3, pady = 5)



app = ctk.CTk() 

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

app.geometry(f"{screen_width}x{screen_height}")

def button_function():
    print("button pressed")

#LABEL TO INDICATE ACTION
label = ctk.CTkLabel(app, text="What can I help you with?", fg_color="transparent", text_color="white", font=font)
label.place(relx=0.55, rely=0.7)


#CONVERSATION OPTION BUTTONS
button = ctk.CTkButton(master=app, text="OPTION 1", font=font, 
                                 fg_color=color1, height=100, width=400)
button.place(relx=0.25, rely=0.8)

button = ctk.CTkButton(master=app, text="OPTION 2", font=font, 
                                 fg_color=color1, height=100, width=400)
button.place(relx=0.5, rely=0.8)

button = ctk.CTkButton(master=app, text="OPTION 3", font=font, 
                                 fg_color=color1, height=100, width=400)
button.place(relx=0.75, rely=0.8)

#TOP RIGHT TOTAL PORTFOLIO
button = ctk.CTkButton(master=app, text="PORTFOLIO VALUE", font=font, 
                                 fg_color=color1, height=90, width=300)
button.place(relx=0.8, rely=0.05)

#INSTANTIATE THE LEFT SCROLLER
frame = MyFrame(app, width=250, fg_color="black")
frame.pack(side="left", fill="y", padx=10, pady=10)


app.mainloop()
