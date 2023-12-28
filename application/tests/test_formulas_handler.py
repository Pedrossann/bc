import unittest
from unittest.mock import Mock, patch, ANY
import customtkinter as ctk

from application.src import FormulasHandler
from application.src.blueprints import FormulaBlueprint
from application.src.excel import ExcelInput, ExcelOutput


def get_mock_switch_states() -> {str: bool}:
    mock_formulas = {
        'wantedFormula1': False,
        'notWantedFormula': False,
        'wantedFormula2': True
    }
    return mock_formulas


def get_mock_formulas():
    mock_formula1 = Mock(spec=FormulaBlueprint)
    mock_formula2 = Mock(spec=FormulaBlueprint)
    mock_formula3 = Mock(spec=FormulaBlueprint)

    mock_formula1.wanted = True
    mock_formula2.wanted = False
    mock_formula3.wanted = True

    mock_formula1.variables = {"variable1": Mock(), "variable2": Mock()}
    mock_formula2.variables = {"variable2": Mock(), "variable3": Mock()}
    mock_formula3.variables = {"variable2": Mock(), "variable4": Mock()}

    return {"wantedFormula1": mock_formula1,
            "notWantedFormula": mock_formula2,
            "wantedFormula2": mock_formula3}


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
        valid_formulas = get_mock_switch_states()
        self.formulas_handler.formulas = get_mock_formulas()

        self.formulas_handler.switches_wanted_formulas(valid_formulas)

        self.assertEquals(self.formulas_handler.formulas["wantedFormula1"].wanted, False)
        self.assertEquals(self.formulas_handler.formulas["notWantedFormula"].wanted, False)
        self.assertEquals(self.formulas_handler.formulas["wantedFormula2"].wanted, True)

        self.formulas_handler.excel_output.create_saving_structure.assert_called_once()

    def test_switches_wanted_formulas_with_invalid_formulas(self):
        invalid_formulas = {}
        self.formulas_handler.formulas = get_mock_formulas()

        with self.assertRaises(ValueError):
            self.formulas_handler.switches_wanted_formulas(invalid_formulas)

    def test_get_wanted_formulas(self):
        self.formulas_handler.formulas = get_mock_formulas()

        result = self.formulas_handler.get_wanted_formulas()

        self.assertEquals(result, [self.formulas_handler.formulas["wantedFormula1"],
                                   self.formulas_handler.formulas["wantedFormula2"]])

    def test_get_all_needed_data_names(self):
        self.formulas_handler.formulas = get_mock_formulas()

        result = self.formulas_handler.get_needed_data_names()

        self.assertEquals(result, ["variable1", "variable2", "variable4"])

    def test_get_all_variable_names(self):
        self.formulas_handler.formulas = get_mock_formulas()

        result = self.formulas_handler.get_all_variable_names()

        self.assertEquals(result, ["variable1", "variable2", "variable3", "variable4"])

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

    def test_get_formula_by_name_with_valid_request(self):
        self.formulas_handler.formulas = get_mock_formulas()

        result = self.formulas_handler.get_formula_by_name("wantedFormula2")

        self.assertEquals(self.formulas_handler.formulas["wantedFormula2"], result)

    def test_get_formula_by_name_with_invalid_request(self):
        result = self.formulas_handler.get_formula_by_name(None)

        self.assertEquals(None, result)

    @patch("os.listdir")
    def test_get_import_excel_names(self, mock_listdir):
        mock_listdir.return_value = ["Test1.xlsx", "Test2.xlsx", "Invalid"]

        result = self.formulas_handler.get_import_excel_names()

        self.assertEquals(result, ["Test1", "Test2"])

    def test_calculation(self):
        self.formulas_handler.excel_input.get_data.side_effect = [
            {'var1': 1, 'var2': 2, 'var3': 3},
            {'var1': 4, 'var2': 5, 'var3': 6},
            None
        ]

        mock_formula1 = Mock()
        mock_formula1.variables = {'var1': None, 'var2': None}
        mock_formula1.name = "Formula1"

        mock_formula2 = Mock()
        mock_formula2.variables = {'var1': None, 'var3': None}
        mock_formula2.name = "Formula2"

        self.formulas_handler.get_wanted_formulas = Mock(return_value=[mock_formula1, mock_formula2])

        self.formulas_handler.calculation("TestOutputFile")

        self.formulas_handler.excel_output.save_data.assert_called_once()
        self.assertEquals(mock_formula1.try_calculate.call_count, 2)
        self.assertEquals(mock_formula2.try_calculate.call_count, 2)
        self.assertEquals(self.formulas_handler.excel_output.add_calculated_data.call_count, 2)
