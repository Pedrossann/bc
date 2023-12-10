from blueprints.FormulaBlueprint import FormulaBlueprint


class TestFormula2(FormulaBlueprint):
    def __init__(self, parent):
        self.formulaName = "Formula2"
        self.explanation = "Vysvetleni 2. promenne"
        super().__init__(parent, self.formulaName, self.explanation)

        self.variables = {"hodnota3": None, "hodnota2": None}

    def calculate(self):
        return self.variables["hodnota3"] + self.variables["hodnota2"]
