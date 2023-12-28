import unittest
from unittest.mock import Mock
from mock.mock import patch

from application.src.formulas.formula2 import formula2

"""
@TODO change FormulaBlueprint after renaming
"""
class TestFormula1(unittest.TestCase):
    @patch("application.src.blueprints.FormulaBlueprint.__init__")
    def setUp(self, mock__init__):
        mock_frame = Mock()
        self.formula = formula2(mock_frame)

    def test_init(self):
        self.assertIsNotNone(self.formula)

    def test_init_values(self):
        self.assertEquals(self.formula.name, "Formula -")
        self.assertEquals(self.formula.explanation, "hodnota2 - hodnota3")
        self.assertEquals(self.formula.variables, {"hodnota2": None, "hodnota3": None})

    def test_calculation(self):
        self.formula.variables = {"hodnota2": 3, "hodnota3": 2}

        result = self.formula.calculate()

        self.assertEquals(result, 1)

