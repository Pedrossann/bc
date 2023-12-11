from blueprints.ScreenBllueprint import ScreenBllueprint
import customtkinter as ctk


# Frame that let user choose criteria about saving the output
# @window - Parent of the frame.
# @mathHandler -connection to mathematic logic of the application.
class ExportScreen(ScreenBllueprint):
    def __init__(self, window, formulas_handler):
        super().__init__(window, formulas_handler)

        button_frame = self.create_button_frame(True, True)
        main_frame = self.create_main_frame()

        self.name_entry = self.create_entry_frame(main_frame)

        main_frame.pack()
        button_frame.pack(fill="x", expand=True)

    # Switches the screen and loads the data for the next screen.
    def next_screen(self):
        self.formulas_handler.calculation(self.name_entry.get())

    # Returns to previous screen.
    def back_screen(self):
        self.window.screens["ImportScreen"].tkraise()

    # Creates main frame.
    # @parent CTkFrame - parent for this Frame.
    def create_entry_frame(self, parent):
        entry_frame = ctk.CTkFrame(parent)
        text = ctk.CTkLabel(entry_frame, text="Output file name")
        entry = ctk.CTkEntry(entry_frame, placeholder_text="name")

        text.grid(row=0, column=0, padx=10)
        entry.grid(row=0, column=1, padx=10)
        entry_frame.pack()

        return entry
