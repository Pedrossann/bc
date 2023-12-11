import customtkinter as ctk
from PIL import Image


# Holds all main values for managing Formulas.
# @parent CTkFrame - visual data for ImportScreen.
# @name String
# @explanation String
class FormulaBlueprint(ctk.CTkFrame):
    def __init__(self, parent, name, explanation):
        super().__init__(parent)
        self.logo_on = ctk.CTkImage(
            Image.open("images/logo_button_on.png"), size=(25, 25)
        )
        self.logo_off = ctk.CTkImage(
            Image.open("images/logo_button_off.png"), size=(25, 25)
        )
        self.wanted = False
        self.text_switch = False
        self.switch = False
        self.name = name
        self.excel_location = None
        self.excel = None

        self.toggle_button_off = ctk.CTkButton(
            self,
            command=lambda: self.switch_state(),
            hover_color="#aa006d",
            image=self.logo_off,
            text="",
            fg_color="#dbdbdb",
            width=20,
        )

        self.toggle_button_on = ctk.CTkButton(
            self,
            command=lambda: self.switch_state(),
            hover_color="#aa006d",
            image=self.logo_on,
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
        self.toggle_button_off.grid(row=0, column=0)

        self.text_label = ctk.CTkLabel(self, text=explanation)

        self.button.grid(row=0, column=1, sticky="nsew", padx=5)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=20)

        self.pack(expand=True, fill="x", padx=5, pady=5)

    # On/off switch for showing details about formula.
    def showText(self):
        if self.text_switch == False:
            self.text_switch = True
            self.text_label.grid(row=1, column=0, columnspan=2)
            self.update()

        else:
            self.text_switch = False
            self.text_label.grid_remove()
            self.update()

    # On/off switch for selecting if formula shoud be calculated.
    def switch_state(self):
        if self.switch == False:
            self.toggle_button_on.grid(row=0, column=0)
            self.toggle_button_off.grid_remove()
            self.switch = True
        else:
            self.toggle_button_off.grid(row=0, column=0)
            self.toggle_button_on.grid_remove()
            self.switch = False

    # Try calculation. Gives "-" if calculation cant be done.
    # @return result/"-"
    def try_calculate(self):
        try:
            return self.calculate()
        except TypeError:
            return "-"
