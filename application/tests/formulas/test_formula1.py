import unittest
from unittest.mock import Mock
from mock.mock import patch

from application.src.formulas.formula1 import formula1

"""
@TODO change FormulaBlueprint after renaming
"""
class TestFormula1(unittest.TestCase):
    @patch("application.src.blueprints.FormulaBlueprint.__init__")
    def setUp(self, mock__init__):
        mock_frame = Mock()
        self.formula = formula1(mock_frame)

    def test_init(self):
        self.assertIsNotNone(self.formula)

    def test_init_values(self):
        self.assertEquals(self.formula.name, "Formula +")
        self.assertEquals(self.formula.explanation, "hodnota1 + hodnota2")
        self.assertEquals(self.formula.variables, {"hodnota1": None, "hodnota2": None})

    def test_calculation(self):
        self.formula.variables = {"hodnota1": 1, "hodnota2": 2}

        result = self.formula.calculate()

        self.assertEquals(result, 3)

