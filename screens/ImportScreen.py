from widgets.customButton import customButton
import customtkinter as ctk


# This Frame lets user to specify, where program should take data.
# @window - Parent of the frame.
# @mathHandler -connection to mathematic logic of the application.
class ImportScreen(ctk.CTkFrame):
    def __init__(self, window, fHandler):
        super().__init__(window, width=800, height=400)
        self.excel = window.excel

        self.name = "import"
        self.window = window

        self.fHandler = fHandler
        self.variableInfo = {}
        self.specificVariableFrame = {}

        self.buttonFrame = self.createButtonFrame()
        self.variablesFrame = ctk.CTkScrollableFrame(self, width=720, height=350)

        self.variablesFrame.pack()
        self.buttonFrame.pack(fill="x", expand=True)
        self.createVariableFrame()

    # Creates frame for next/back buttons
    def createButtonFrame(self) -> ctk.CTkFrame:
        buttonFrame = ctk.CTkFrame(self, width=720)
        nextButton = customButton(
            buttonFrame,
            text="Další",
            command=lambda: self.nextScreen(),
        )
        backButton = customButton(
            buttonFrame,
            text="Zpět",
            command=lambda: self.window.raiseScreen("choose"),
        )
        buttonFrame.grid_columnconfigure(0, weight=1)
        buttonFrame.grid_columnconfigure(1, weight=1)
        nextButton.grid(row=0, column=1, sticky="e", pady=10, padx=10)
        backButton.grid(row=0, column=0, sticky="w", pady=10, padx=10)

        return buttonFrame

    # Creates frames for all variables.
    def createVariableFrame(self) -> ctk.CTkFrame:
        excelNames = ["-"]
        for excelName in self.fHandler.getImportExcelNames():
            excelNames.append(excelName)
        for variableName in self.fHandler.getAllDataNames():
            specificVariableFrame = ctk.CTkFrame(self.variablesFrame)
            self.specificVariableFrame[variableName] = {
                "frame": specificVariableFrame,
                "coordinates": ctk.CTkEntry(
                    specificVariableFrame, placeholder_text="A1", width=30
                ),
                "excel": ctk.CTkComboBox(specificVariableFrame, values=excelNames),
            }

            label = ctk.CTkLabel(specificVariableFrame, text=variableName)

            label.grid(row=0, column=0, padx=50)
            self.specificVariableFrame[variableName]["coordinates"].grid(
                row=0, column=1, padx=50
            )
            self.specificVariableFrame[variableName]["excel"].grid(
                row=0, column=2, padx=50
            )
        return specificVariableFrame

    # Places all needed variables in the frame.
    def gridNeededVariables(self):
        dontNeededVariables = [
            item
            for item in self.fHandler.getAllDataNames()
            if item not in self.fHandler.getAllNeededDataNames()
        ]
        for variable in dontNeededVariables:
            self.specificVariableFrame[variable]["frame"].pack_forget()

        for variable in self.fHandler.getAllNeededDataNames():
            self.specificVariableFrame[variable]["frame"].pack(pady=5)

    # Goes to next screen.
    def nextScreen(self):
        for variableName in self.fHandler.getAllNeededDataNames():
            self.variableInfo[variableName] = {
                "excel": self.specificVariableFrame[variableName]["excel"].get(),
                "coordinates": self.specificVariableFrame[variableName][
                    "coordinates"
                ].get(),
            }
        self.excel.variables = self.variableInfo
        self.excel.openExcels()
        self.window.raiseScreen("export")
