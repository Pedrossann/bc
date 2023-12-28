import unittest
from unittest.mock import Mock, patch
import customtkinter as ctk

from application.src import FormulasHandler
from application.src.blueprints import FormulaBlueprint
from application.src.excel import ExcelInput, ExcelOutput


def getMockSwitchStates() -> {str: bool}:
    mock_formulas = {
        'formula1': False,
        'formula2': False,
        'formula3': True
    }
    return mock_formulas


class TestFormulasHandler(unittest.TestCase):
    def setUp(self):
        self.mock_excel_input = Mock(spec=ExcelInput)
        self.mock_excel_output = Mock(spec=ExcelOutput)

        self.formulas_handler = FormulasHandler(self.mock_excel_input, self.mock_excel_output)

    def test_init(self):
        self.assertIsNotNone(self.formulas_handler)

    def test_initializing_objects(self):
        self.assertEquals(self.formulas_handler.excel_output, self.mock_excel_output)
        self.assertEquals(self.formulas_handler.excel_input, self.mock_excel_input)

    def test_switches_wanted_formulas_with_valid_formulas(self):
        valid_formulas = getMockSwitchStates()
        self.formulas_handler.formulas = {"formula1": Mock(),
                                          "formula2": Mock(),
                                          "formula3": Mock()}

        self.formulas_handler.switches_wanted_formulas(valid_formulas)

        self.assertEquals(self.formulas_handler.formulas["formula1"].wanted, False)
        self.assertEquals(self.formulas_handler.formulas["formula2"].wanted, False)
        self.assertEquals(self.formulas_handler.formulas["formula3"].wanted, True)

    def test_switches_wanted_formulas_with_invalid_formulas(self):
        invalid_formulas = {}
        self.formulas_handler.formulas = {"formula1": Mock(),
                                          "formula2": Mock(),
                                          "formula3": Mock()}

        with self.assertRaises(ValueError):
            self.formulas_handler.switches_wanted_formulas(invalid_formulas)

    def test_get_wanted_formulas(self):
        mock_formula1 = Mock(spec=FormulaBlueprint)
        mock_formula2 = Mock(spec=FormulaBlueprint)
        mock_formula3 = Mock(spec=FormulaBlueprint)

        self.formulas_handler.formulas = {"wantedFormula1": mock_formula1,
                                          "notWantedFormula": mock_formula2,
                                          "wantedFormula2": mock_formula3}
        self.formulas_handler.formulas["wantedFormula1"].wanted = True
        self.formulas_handler.formulas["notWantedFormula"].wanted = False
        self.formulas_handler.formulas["wantedFormula2"].wanted = True

        result = self.formulas_handler.get_wanted_formulas()

        self.assertEquals(result, [mock_formula1, mock_formula3])


    def test_get_all_needed_variable_names(self):
        mock_formula1 = Mock(spec=FormulaBlueprint)
        mock_formula2 = Mock(spec=FormulaBlueprint)
        mock_formula3 = Mock(spec=FormulaBlueprint)

        mock_formula1.wanted = True
        mock_formula2.wanted = False
        mock_formula3.wanted = True

        mock_formula1.variables = {"variable1": Mock(), "variable2": Mock()}
        mock_formula2.variables = {"variable2": Mock(), "variable3": Mock()}
        mock_formula3.variables = {"variable2": Mock(), "variable4": Mock()}

        self.formulas_handler.formulas = {"wantedFormula1": mock_formula1,
                                          "notWantedFormula": mock_formula2,
                                          "wantedFormula2": mock_formula3}

        result = self.formulas_handler.get_needed_data_names()

        self.assertEquals(result, ["variable1", "variable2", "variable4"])




    @patch("os.listdir")
    @patch('importlib.import_module')
    def test_create_formulas(self, mock_import_module, mock_listdir):
        mock_listdir.return_value = ['ValidFormula.py', 'InValidFormula.py', '__init__.py']

        mock_valid_module = Mock()
        mock_valid_class = Mock(return_value='Instance of ValidFormula')
        setattr(mock_valid_module, 'ValidFormula', mock_valid_class)

        def import_module_side_effect(module_name):
            if module_name == 'src.formulas.ValidFormula':
                return mock_valid_module
            raise ImportError(f"No module named {module_name}")

        mock_import_module.side_effect = import_module_side_effect

        mock_frame = Mock()
        result = self.formulas_handler.create_formulas(mock_frame)

        self.assertIn('ValidFormula', result)
        self.assertEqual(result['ValidFormula'], 'Instance of ValidFormula')
        mock_valid_class.assert_called_once_with(mock_frame)
        self.assertNotIn('InvalidFormula', result)
        self.assertNotIn('__init__', result)

