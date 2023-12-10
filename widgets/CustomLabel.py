import customtkinter as ctk


class CustomLabel(ctk.CTkLabel):
    def __init__(self, parent, text):
        super().__init__(parent, text=text)
