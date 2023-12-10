import customtkinter as ctk


# Label for names.
class CustomLabel(ctk.CTkLabel):
    def __init__(self, parent, text):
        super().__init__(parent, text=text)
