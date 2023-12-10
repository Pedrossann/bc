from widgets.customButton import customButton
import customtkinter as ctk


# First Frame, that lets user to choose which variables he wantsto calculate.
# @window - Parent of the frame.
# @mathHandler -connection to mathematic logic of the application.
class ChooseScreen(ctk.CTkFrame):
    def __init__(self, window, fHandler):
        super().__init__(window, width=800, height=400)

        self.name = "choose"
        self.window = window
        self.fHandler = fHandler

        self.buttonFrame = self.createButtonFrame()
        self.mainFrame = self.createMainFrame()

        self.mainFrame.pack()
        self.buttonFrame.pack(fill="x", expand=True)

    # Creates frame with next/back buttons.
    def createButtonFrame(self) -> ctk.CTkFrame:
        buttonFrame = ctk.CTkFrame(self, width=720)
        nextButton = customButton(
            buttonFrame,
            text="Další",
            command=lambda: self.nextScreen(),
        )
        buttonFrame.grid_columnconfigure(1, weight=1)
        nextButton.grid(row=0, column=1, sticky="e", pady=10, padx=10)

        return buttonFrame

    # Creates Scrollable frame with all formulas inside.
    # @return created frame with forulas.
    def createMainFrame(self):
        mainFrame = ctk.CTkScrollableFrame(self, width=720, height=350)
        self.fHandler.createAllFormulas(mainFrame)
        return mainFrame

    # Gets the data(on = true/ off = false) of the switches and saves chosed formulas into the math handler.
    def getStatesOfFormulas(self):
        states = {}
        for formula in self.fHandler.formulas:
            states[formula.name] = formula.switch
        self.fHandler.saveWantedFormulas(states)

    # Switches the screen and loads the data for the next screen.
    def nextScreen(self):
        self.getStatesOfFormulas()
        self.window.getScreenByName("import").gridNeededVariables()
        self.window.raiseScreen("import")
