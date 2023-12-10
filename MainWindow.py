import customtkinter as ctk
from MainWindowBody import Body
from MainWindowHeader import Header
from MainWindowFooter import Footer
from FormulasHandler import FormulasHandler
from excel.ExcelGet import ExcelGet
from excel.ExcelOutput import ExcelOutput


# Main window of the application. This is the backbone of the application
class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x600+300+100")
        self.title("Bakalarka")

        self.excelGet = ExcelGet()
        self.excelOutput = ExcelOutput()
        self.formulasHandler = FormulasHandler(self.excelGet, self.excelOutput)

        self.header = Header(self)
        self.body = Body(self, self.formulasHandler, self.excelGet)
        self.footer = Footer(self)
