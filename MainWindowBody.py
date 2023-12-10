import customtkinter as ctk
import os
import importlib


# Body of the aplication with multiple screens.
class Body(ctk.CTkFrame):
    def __init__(self, parent, fHandler, excel):
        super().__init__(parent)
        self.fHandler = fHandler
        self.excel = excel

        self.screens = self.createScreenClasses()

        self.gridClasses()
        self.pack(anchor="n", expand=True)
        self.raiseScreen("choose")

    # Creates and returns all screen classes from screens folder.
    # @return [Screen] - List of classes from screens folder.
    def createScreenClasses(self) -> [object]:
        all_screens = []
        for scr in os.listdir("screens"):
            if scr.endswith(".py"):
                all_screens.append(
                    getattr(
                        importlib.import_module("screens." + scr.split(".py")[0]),
                        scr.split(".")[0],
                    )(self, self.fHandler)
                )
        return all_screens

    # Grids all screen classes.
    def gridClasses(self):
        for cls in self.screens:
            cls.grid(row=0, column=0)

    # Raises screen by name.
    def raiseScreen(self, name):
        for screen in self.screens:
            if screen.name == name:
                screen.tkraise()

    # Returns screen by name.
    def getScreenByName(self, name) -> object:
        for screen in self.screens:
            if screen.name == name:
                return screen
        return None
