from application.src.blueprints.FormulaBlueprint import FormulaBlueprint
import customtkinter as ctk


"""
Formula for testing
TODO change code so formula and name of the class can be different
TODO maybe create universal error system if calculation isnt succesfull
"""
class formula1(FormulaBlueprint):
    def __init__(self, parent: ctk.CTkScrollableFrame) -> None:
        self.name = "Formula +"
        self.explanation = "hodnota1 + hodnota2"
        super().__init__(parent, self.name, self.explanation)

        self.variables = {"hodnota1": None, "hodnota2": None}

    def calculate(self) -> int:
        return self.variables["hodnota1"] + self.variables["hodnota2"]
