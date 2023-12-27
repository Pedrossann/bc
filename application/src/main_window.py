import customtkinter as ctk
from .elements.MainWindowBody import Body
from .elements.MainWindowHeader import Header
from .elements.MainWindowFooter import Footer
from .FormulasHandler import FormulasHandler
from .excel.ExcelInput import ExcelInput
from .excel.ExcelOutput import ExcelOutput


"""
Main window of the application. This is the backbone of the application.
"""
class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x600+300+100")
        self.title("Bakalarka")

        self.excel_input = ExcelInput()
        self.excel_output = ExcelOutput()
        self.formulas_handler = FormulasHandler(self.excel_input, self.excel_output)

        self.header = Header(self)
        self.body = Body(self, self.formulas_handler, self.excel_input)
        self.footer = Footer(self)
