import customtkinter

customtkinter.set_appearance_mode("Dark")

#GLOBAL DEFAULTS
font = ("arial", 20)
color1 = "RED"
color2 = "ORANGE"

app = customtkinter.CTk() 

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

app.geometry(f"{screen_width}x{screen_height}")

def button_function():
    print("button pressed")

#LABEL TO INDICATE ACTION
label = customtkinter.CTkLabel(app, text="What can I help you with?", fg_color="transparent", text_color="white", font=font)
label.place(relx=0.55, rely=0.7)


#CONVERSATION OPTION BUTTONS
button = customtkinter.CTkButton(master=app, text="OPTION 1", font=font, 
                                 fg_color=color1, command=button_function, height=100, width=400)
button.place(relx=0.25, rely=0.8)

button = customtkinter.CTkButton(master=app, text="OPTION 2", font=font, 
                                 fg_color=color1, command=button_function, height=100, width=400)
button.place(relx=0.5, rely=0.8)

button = customtkinter.CTkButton(master=app, text="OPTION 3", font=font, 
                                 fg_color=color1, command=button_function, height=100, width=400)
button.place(relx=0.75, rely=0.8)

#LEFT STOCK PANEL
ctk_textbox_scrollbar = customtkinter.CTkScrollbar(app)
ctk_textbox_scrollbar.grid(row=0, column=700, sticky="ns")


app.mainloop()
