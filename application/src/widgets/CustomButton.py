import customtkinter as ctk


"""
Button for changing Frames.
TODO choose design and maybe delete this class
"""
class CustomButton(ctk.CTkButton):
    def __init__(self, parent: ctk.CTkFrame, **kwargs) -> None:
        super().__init__(parent, **kwargs)
        self.configure(fg_color="#aa006d")
