import customtkinter as ctk


"""
Label for names.
"""
class CustomLabel(ctk.CTkLabel):
    def __init__(self, parent: ctk.CTkFrame, text: str) -> None:
        super().__init__(parent, text=text)
