import customtkinter as ctk
from PIL import Image
import os


# Header of the aplication with multiple screens.
# @parent CTkFrame - parent for the frame
class Header(ctk.CTkFrame):
    def __init__(self, window) -> None:
        super().__init__(window, height=100)

        background = ctk.CTkLabel(self, text="", bg_color="#aa006d")
        background.place(relwidth=1, relheight=1)

        logo_image = ctk.CTkImage(Image.open(os.getcwd() + "\\application\\src\\images\\logo.png"), size=(80, 80))
        logo_header = ctk.CTkLabel(self, image=logo_image, text="")
        logo_header.place(relx=1, x=-100, y=10)

        self.pack(expand=True, anchor="n", fill="x")
