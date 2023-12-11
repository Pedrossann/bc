from blueprints.FormulaBlueprint import FormulaBlueprint


# Formula for testing
class TestFormula(FormulaBlueprint):
    def __init__(self, parent):
        self.name = "Formula1"
        self.explanation = "hodnota1 + hodnota2"
        super().__init__(parent, self.name, self.explanation)

        self.variables = {"hodnota1": None, "hodnota2": None}

    def calculate(self):
        return self.variables["hodnota1"] + self.variables["hodnota2"]
