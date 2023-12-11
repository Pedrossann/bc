import customtkinter as ctk


# Button for changing Frames.
class customButton(ctk.CTkButton):
    def __init__(self, parent: ctk.CTkFrame, **kwargs) -> None:
        super().__init__(parent, **kwargs)
        self.configure(fg_color="#aa006d")
