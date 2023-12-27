import unittest
from unittest.mock import patch

from application.src import MainWindow


class TestMainWindow(unittest.TestCase):
    def setUp(self):
        with patch('application.src.main_window.Footer') as MockFooter, \
             patch('application.src.main_window.Header') as MockHeader, \
             patch('application.src.main_window.Body') as MockBody, \
             patch('application.src.main_window.ExcelInput') as MockExcelInput, \
             patch('application.src.main_window.ExcelOutput') as MockExcelOutput, \
             patch('application.src.main_window.FormulasHandler') as MockFormulasHandler:

            self.mock_footer = MockFooter
            self.mock_header = MockHeader
            self.mock_body = MockBody
            self.mock_excel_input = MockExcelInput
            self.mock_excel_output = MockExcelOutput
            self.mock_formulas_handler = MockFormulasHandler

            self.app = MainWindow()

    def testInit(self):
        self.assertIsNotNone(self.app)

    def testInitializingObjects(self):
        self.mock_footer.assert_called_once()
        self.mock_header.assert_called_once()
        self.mock_body.assert_called_once()
        self.mock_excel_input.assert_called_once()
        self.mock_excel_output.assert_called_once()
        self.mock_formulas_handler.assert_called_once()

        self.assertEquals(self.app.footer, self.mock_footer.return_value)
        self.assertEquals(self.app.header, self.mock_header.return_value)
        self.assertEquals(self.app.body, self.mock_body.return_value)
        self.assertEquals(self.app.excel_input, self.mock_excel_input.return_value)
        self.assertEquals(self.app.excel_output, self.mock_excel_output.return_value)
        self.assertEquals(self.app.formulas_handler, self.mock_formulas_handler.return_value)

if __name__ == "__main__":
    unittest.main()
