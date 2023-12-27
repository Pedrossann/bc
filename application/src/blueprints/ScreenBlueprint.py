from application.src.widgets import customButton
import customtkinter as ctk
from application.src.FormulasHandler import FormulasHandler


# Blueprint for common parts for all Screens.
# @window CTkFrame- Parent of the frame.
# @formulas_handler FormulasHandler - connection formulas logic of the application.
class ScreenBlueprint(ctk.CTkFrame):
    def __init__(self, window: ctk.CTkFrame, formulas_handler: FormulasHandler) -> None:
        super().__init__(window, width=800, height=400)
        self.window = window
        self.formulas_handler = formulas_handler

    # Creates frame for next/back buttons
    # @param next_screen True(creates next_button)/False
    # @param back_screen True(creates back_button)/False
    # @return Frame
    def create_button_frame(self, next_screen: bool, back_screen: bool) -> ctk.CTkFrame:
        button_frame = ctk.CTkFrame(self, width=720)

        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)

        if next_screen:
            next_button = ctk.CTkButton(
                button_frame,
                text="Další",
                command=lambda: self.next_screen(),
            )
            next_button.grid(row=0, column=1, sticky="e", pady=10, padx=10)

        if back_screen:
            back_button = ctk.CTkButton(
                button_frame,
                text="Zpět",
                command=lambda: self.back_screen(),
            )
            back_button.grid(row=0, column=0, sticky="w", pady=10, padx=10)

        return button_frame

    # Creates main scrollable frame for screen.
    def create_main_frame(self) -> ctk.CTkScrollableFrame:
        return ctk.CTkScrollableFrame(self, width=720, height=350)

    def next_screen(self):
        pass

    def back_screen(self):
        pass
