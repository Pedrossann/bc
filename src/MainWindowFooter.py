import customtkinter as ctk


# Footer of the aplication with multiple screens.
# @parent CTkFrame - parent for the frame.
class Footer(ctk.CTkFrame):
    def __init__(self, window) -> None:
        super().__init__(window)

        self.label = ctk.CTkLabel(self, text="Mendelu FRRMS - Petr Němec")
        self.label.pack()

        self.pack(expand=True, fill="x")
