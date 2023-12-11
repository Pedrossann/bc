from blueprints.FormulaBlueprint import FormulaBlueprint


class TestFormula2(FormulaBlueprint):
    def __init__(self, parent):
        self.name = "Formula2"
        self.explanation = "hodnota3 - hodnota2"
        super().__init__(parent, self.name, self.explanation)

        self.variables = {"hodnota3": None, "hodnota2": None}

    def calculate(self):
        return self.variables["hodnota3"] - self.variables["hodnota2"]
