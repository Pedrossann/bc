import unittest
from unittest.mock import  Mock

from application.src import FormulasHandler
from application.src.excel import ExcelInput, ExcelOutput


class TestFormulasHandler(unittest.TestCase):
    def setUp(self):
        self.mock_excel_input = Mock(spec=ExcelInput)
        self.mock_excel_output = Mock(spec=ExcelOutput)

        self.formulas_handler = FormulasHandler(self.mock_excel_input, self.mock_excel_output)

    def test_init(self):
        self.assertIsNotNone(self.formulas_handler)
