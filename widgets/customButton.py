import customtkinter as ctk


# Button for changing Frames
class customButton(ctk.CTkButton):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.configure(fg_color="#aa006d")
