from application.src.blueprints.FormulaBlueprint import FormulaBlueprint
import customtkinter as ctk

"""
Formula for testing
"""
class TestFormula(FormulaBlueprint):
    def __init__(self, parent: ctk.CTkScrollableFrame) -> None:
        self.name = "Formula +"
        self.explanation = "hodnota1 + hodnota2"
        super().__init__(parent, self.name, self.explanation)

        self.variables = {"hodnota1": None, "hodnota2": None}

    def calculate(self) -> None:
        return self.variables["hodnota1"] + self.variables["hodnota2"]
