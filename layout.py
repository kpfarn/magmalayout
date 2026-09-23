import customtkinter as ctk

ctk.set_appearance_mode("Dark")

#GLOBAL DEFAULTS
font = ("arial", 20)
color1 = "RED"
color2 = "ORANGE"


#LEFT STOCK PANEL
class MyFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = ctk.CTkLabel(self, text="STOCKS", text_color="white")
        self.label.grid(row=0, column=0, padx=20)

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

#INSTANTIATE THE LEFT SCROLLER
frame = MyFrame(app, width=250, fg_color=color2)
frame.pack(side="left", fill="y", padx=10, pady=10)
frame.label.configure(text="PORTFOLIO")


app.mainloop()
