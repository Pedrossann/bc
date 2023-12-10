from widgets.customButton import customButton
import customtkinter as ctk


# Frame that let user choose criteria about saving the output
# @window - Parent of the frame.
# @mathHandler -connection to mathematic logic of the application.
class ExportScreen(ctk.CTkFrame):
    def __init__(self, window, fHandler):
        super().__init__(window, width=800, height=400)

        self.name = "export"
        self.window = window
        self.fHandler = fHandler

        self.buttonFrame = self.createButtonFrame()
        self.mainFrame = ctk.CTkScrollableFrame(self, width=720, height=350)

        self.mainFrame.pack()
        self.buttonFrame.pack(fill="x", expand=True)

    def createButtonFrame(self) -> ctk.CTkFrame:
        buttonFrame = ctk.CTkFrame(self, width=720)
        backButton = customButton(
            buttonFrame,
            text="Zpět",
            command=lambda: self.window.raiseScreen("import"),
        )
        doneButton = customButton(
            buttonFrame,
            text="Hotovo",
            command=lambda: self.clickDone(),
        )
        buttonFrame.grid_columnconfigure(0, weight=1)
        buttonFrame.grid_columnconfigure(1, weight=1)
        backButton.grid(row=0, column=0, sticky="w", pady=10, padx=10)
        doneButton.grid(row=0, column=1, sticky="e", pady=10, padx=10)

        return buttonFrame

    def clickDone(self):
        self.fHandler.calculation()
