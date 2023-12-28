from application.src.blueprints.ScreenBlueprint import ScreenBlueprint
import customtkinter as ctk


# This Frame lets user to specify, where program should take data.
# @window CTkFrame- Parent of the frame.
# @formulas_handler FormulasHandler - connection formulas logic of the application.
# TODO get rid of self.excel_input
class ImportScreen(ScreenBlueprint):
    def __init__(self, window: ctk.CTkFrame, formulas_handler: 'FormulasHandler') -> None:
        super().__init__(window, formulas_handler)

        self.specific_variable_frame = {}
        self.excel_input = window.excel_input

        button_frame = self.create_button_frame(True, True)
        main_frame = self.create_main_frame()

        main_frame.pack()
        button_frame.pack(fill="x", expand=True)
        self.create_variable_frame(main_frame)

    # Creates frames for all variables.
    # @return {CTkFrames} - Map of specific variable frames.
    def create_variable_frame(
        self, main_variables_frame: {ctk.CTkFrame}
    ) -> ctk.CTkFrame:
        excel_names = ["-"]
        for excel_name in self.formulas_handler.get_import_excel_names():
            excel_names.append(excel_name)
        for variable_name in self.formulas_handler.get_all_variable_names():
            variable_frame = ctk.CTkFrame(main_variables_frame)
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
    def grid_needed_variables(self) -> None:
        no_needed_variables = [
            item
            for item in self.formulas_handler.get_all_variable_names()
            if item not in self.formulas_handler.get_needed_data_names()
        ]
        for variable in no_needed_variables:
            self.specific_variable_frame[variable]["frame"].pack_forget()

        for variable in self.formulas_handler.get_needed_data_names():
            self.specific_variable_frame[variable]["frame"].pack(pady=5)

    # Goes to next screen and runs necessary logic for it.
    # TODO change variable_info to variables_info
    def next_screen(self) -> None:
        variable_info = {}
        for variable_name in self.formulas_handler.get_needed_data_names():
            variable_info[variable_name] = {
                "excel": self.specific_variable_frame[variable_name]["excel"].get(),
                "coordinates": self.specific_variable_frame[variable_name][
                    "coordinates"
                ].get(),
            }
        self.excel_input.variables = variable_info
        self.excel_input.open_excels()
        self.window.screens["ExportScreen"].tkraise()

    # Goes to previous Screen
    def back_screen(self) -> None:
        self.window.screens["ChooseScreen"].tkraise()
