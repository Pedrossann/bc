from widgets.customButton import customButton
import customtkinter as ctk


# This Frame lets user to specify, where program should take data.
# @window CTkFrame- Parent of the frame.
# @formulas_handler FormulasHandler - connection formulas logic of the application.
# TODO remove self.name, self.variable_info?, self.variables_frame,self.button_frame
class ImportScreen(ctk.CTkFrame):
    def __init__(self, window, formulas_handler):
        super().__init__(window, width=800, height=400)
        self.window = window
        self.formulas_handler = formulas_handler

        self.excel_input = window.excel_input

        self.variable_info = {}

        self.specific_variable_frame = {}

        self.button_frame = self.create_button_frame()
        self.variables_frame = ctk.CTkScrollableFrame(self, width=720, height=350)

        self.variables_frame.pack()
        self.button_frame.pack(fill="x", expand=True)
        self.create_variable_frame()

    # Creates frame for next/back buttons
    # @return Frame
    def create_button_frame(self) -> ctk.CTkFrame:
        button_frame = ctk.CTkFrame(self, width=720)
        next_button = customButton(
            button_frame,
            text="Další",
            command=lambda: self.next_screen(),
        )
        back_button = customButton(
            button_frame,
            text="Zpět",
            command=lambda: self.window.screens["ChooseScreen"].tkraise(),
        )
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)
        next_button.grid(row=0, column=1, sticky="e", pady=10, padx=10)
        back_button.grid(row=0, column=0, sticky="w", pady=10, padx=10)

        return button_frame

    # Creates frames for all variables.
    # @return {CTkFrames} - Map of specific variable frames.
    def create_variable_frame(self) -> ctk.CTkFrame:
        excel_names = ["-"]
        for excel_name in self.formulas_handler.get_import_excel_names():
            excel_names.append(excel_name)
        for variable_name in self.formulas_handler.get_all_variable_names():
            variable_frame = ctk.CTkFrame(self.variables_frame)
            self.specific_variable_frame[variable_name] = {
                "frame": variable_frame,
                "coordinates": ctk.CTkEntry(
                    variable_frame, placeholder_text="A1", width=30
                ),
                "excel": ctk.CTkComboBox(variable_frame, values=excel_names),
            }

            label = ctk.CTkLabel(variable_frame, text=variable_name)

            label.grid(row=0, column=0, padx=50)
            self.specific_variable_frame[variable_name]["coordinates"].grid(
                row=0, column=1, padx=50
            )
            self.specific_variable_frame[variable_name]["excel"].grid(
                row=0, column=2, padx=50
            )
        return variable_frame

    # Places all needed variables in the frame.
    def grid_needed_variables(self):
        no_needed_variables = [
            item
            for item in self.formulas_handler.get_all_variable_names()
            if item not in self.formulas_handler.get_all_needed_data_names()
        ]
        for variable in no_needed_variables:
            self.specific_variable_frame[variable]["frame"].pack_forget()

        for variable in self.formulas_handler.get_all_needed_data_names():
            self.specific_variable_frame[variable]["frame"].pack(pady=5)

    # Goes to next screen and runs necessary logic for it.
    def next_screen(self):
        for variable_name in self.formulas_handler.get_all_needed_data_names():
            self.variable_info[variable_name] = {
                "excel": self.specific_variable_frame[variable_name]["excel"].get(),
                "coordinates": self.specific_variable_frame[variable_name][
                    "coordinates"
                ].get(),
            }
        self.excel_input.variables = self.variable_info
        self.excel_input.open_excels()
        self.window.screens["ExportScreen"].tkraise()
