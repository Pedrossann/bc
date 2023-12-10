import customtkinter as ctk
import os
import importlib


# Body of the aplication with multiple screens.
# @param CTkFrame parent - parent for the frame
# @formulas_handler FormulasHandler
# @excel_input ExcelInput - gets data from excel files.
# TODO repair screenNames
class Body(ctk.CTkFrame):
    def __init__(self, parent, formulas_handler, excel_input):
        super().__init__(parent)
        self.formulas_handler = formulas_handler
        self.excel_input = excel_input

        self.screens = self.create_screens()

        self.grid_screens(self.screens)
        self.pack(anchor="n", expand=True)
        self.raise_screen("ChooseScreen")

    # Creates and returns all screen classes from screens folder.
    # @return {"screen_name": Screen} - Map of created screen classes.
    def create_screens(self):
        all_screens = {}
        for scr in os.listdir("screens"):
            if scr.endswith(".py"):
                all_screens[scr.split(".py")[0]] = getattr(
                    importlib.import_module("screens." + scr.split(".py")[0]),
                    scr.split(".")[0],
                )(self, self.formulas_handler)
        print(all_screens)

        return all_screens

    # Grids all screen classes.
    # @screens {"screen_name": Screen}
    def grid_screens(self, screens):
        for screen in list(screens.keys()):
            screens[screen].grid(row=0, column=0)

    # Raises screen by name.
    # @name of the Screen.
    def raise_screen(self, name):
        self.screens[name].tkraise()

    # Returns screen by name.
    # @name of the Screen.
    def get_screen_by_name(self, name):
        return self.screens[name]
