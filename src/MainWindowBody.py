import customtkinter as ctk
import os
import importlib

from blueprints.ScreenBlueprint import ScreenBlueprint


# Body of the aplication with multiple screens.
# @param CTkFrame parent - parent for the frame
# @formulas_handler FormulasHandler
# @excel_input ExcelInput - gets data from excel files.
class Body(ctk.CTkFrame):
    def __init__(
        self,
        parent,
        formulas_handler,
        excel_input,
    ) -> None:
        super().__init__(parent)
        self.formulas_handler = formulas_handler
        self.excel_input = excel_input

        self.screens = self.create_screens()

        self.grid_screens(self.screens)
        self.pack(anchor="n", expand=True)
        self.screens["ChooseScreen"].tkraise()

    # Creates and returns all screen classes from screens folder.
    # @return {"screen_name": Screen} - Map of created screen classes.
    def create_screens(self) -> {str: ScreenBlueprint}:
        all_screens = {}
        for scr in os.listdir("src/screens"):
            if scr.endswith(".py"):
                all_screens[scr.split(".py")[0]] = getattr(
                    importlib.import_module("screens." + scr.split(".py")[0]),
                    scr.split(".")[0],
                )(self, self.formulas_handler)
        return all_screens

    # Grids all screen classes.
    # @screens {"screen_name": Screen}
    def grid_screens(self, screens: {str: ScreenBlueprint}) -> None:
        for screen in list(screens.keys()):
            screens[screen].grid(row=0, column=0)
