import customtkinter as ctk
from PIL import Image


# Header of the application with logo.
class Header(ctk.CTkFrame):
    def __init__(self, window):
        super().__init__(window, height=100)

        background = ctk.CTkLabel(self, text="", bg_color="#aa006d")
        background.place(relwidth=1, relheight=1)

        logoImage = ctk.CTkImage(Image.open("images/logo.png"), size=(80, 80))
        logoHeader = ctk.CTkLabel(self, image=logoImage, text="")
        logoHeader.place(relx=1, x=-100, y=10)

        self.pack(expand=True, anchor="n", fill="x")
