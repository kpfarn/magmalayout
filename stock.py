import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("Dark")

app = ctk.CTk(fg_color="black") 

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

app.geometry(f"{screen_width}x{screen_height}")

def button_function():
    print("button pressed")


app.mainloop()
