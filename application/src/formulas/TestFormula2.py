from application.src.blueprints.FormulaBlueprint import FormulaBlueprint
import customtkinter as ctk


# TODO bug with -
class TestFormula2(FormulaBlueprint):
    def __init__(self, parent: ctk.CTkScrollableFrame) -> None:
        self.name = "Formula -"
        self.explanation = "hodnota2 - hodnota3"
        super().__init__(parent, self.name, self.explanation)

        self.variables = {"hodnota3": None, "hodnota2": None}

    def calculate(self) -> None:
        return self.variables["hodnota2"] - self.variables["hodnota3"]
