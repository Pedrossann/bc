import customtkinter as ctk
from PIL import Image


# Formula for testing
# Frame with all the Visual logic for TestFormula 2.
class FormulaBlueprint(ctk.CTkFrame):
    def __init__(self, parent, name, explanation):
        super().__init__(parent)
        self.logoOn = ctk.CTkImage(
            Image.open("images/logo_button_on.png"), size=(25, 25)
        )
        self.logoOff = ctk.CTkImage(
            Image.open("images/logo_button_off.png"), size=(25, 25)
        )
        self.wanted = False
        self.textSwitch = False
        self.switch = False
        self.name = name
        self.excelLocation = None
        self.excel = None

        self.toggleButtonOff = ctk.CTkButton(
            self,
            command=lambda: self.switchState(),
            hover_color="#aa006d",
            image=self.logoOff,
            text="",
            fg_color="#dbdbdb",
            width=20,
        )

        self.toggleButtonOn = ctk.CTkButton(
            self,
            command=lambda: self.switchState(),
            hover_color="#aa006d",
            image=self.logoOn,
            text="",
            fg_color="#dbdbdb",
            width=20,
        )

        self.button = ctk.CTkButton(
            self,
            command=lambda: self.showText(),
            text=name,
            hover_color="#aa006d",
            fg_color="#C8C8C8",
            text_color="black",
            anchor="w",
        )
        self.toggleButtonOff.grid(row=0, column=0)

        self.textLabel = ctk.CTkLabel(self, text=explanation)

        self.button.grid(row=0, column=1, sticky="nsew", padx=5)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=20)

        self.pack(expand=True, fill="x", padx=5, pady=5)

    # On/off switch for showing details about TestFormula2
    def showText(self):
        if self.textSwitch == False:
            self.textSwitch = True
            self.textLabel.grid(row=1, column=0, columnspan=2)
            self.update()

        else:
            self.textSwitch = False
            self.textLabel.grid_remove()
            self.update()

    # On/off switch for selecting if TestFormula2 shoud be calculated.
    def switchState(self):
        if self.switch == False:
            self.toggleButtonOn.grid(row=0, column=0)
            self.toggleButtonOff.grid_remove()
            self.switch = True
        else:
            self.toggleButtonOff.grid(row=0, column=0)
            self.toggleButtonOn.grid_remove()
            self.switch = False
