import os
import importlib
from blueprints.FormulaBlueprint import FormulaBlueprint


# Handles all main logic for the calculation and saving the Formulas.
# @excel_input ExcelInput - handles getting data from excel files.
# @excel_output ExcelOutput - handles saving calculated data to file.
class FormulasHandler:
    def __init__(self, excel_input, excel_output):
        self.formulas = {}
        self.excel_input = excel_input
        self.excel_output = excel_output

    # Saves to formulas which formulas we need for calculation and creates map structure in excel_output.
    # @switch_states {"formula_name": True/False}
    def switches_wanted_formulas(self, switch_states):
        for name in list(self.formulas.keys()):
            self.formulas[name].wanted = switch_states[name]
        self.excel_output.create_saving_structure(self.get_wanted_formulas())

    # Returns all the formulas needed for calculation.
    # @return [Formulas] - wanted formulas.
    def get_wanted_formulas(self):
        wanted_formulas = []
        for name in list(self.formulas.keys()):
            if self.formulas[name].wanted:
                wanted_formulas.append(self.formulas[name])
        return wanted_formulas

    # Loads all variables, that are needed for calculating all selected formulas.
    # @return [String] - list of needed variable names.
    def get_all_needed_data_names(self) -> [str]:
        needed_data = []
        for name in list(self.formulas.keys()):
            if self.formulas[name].wanted == True:
                for variable in list(self.formulas[name].variables.keys()):
                    needed_data.append(variable)

        return needed_data

    # @return [str] - all variable names.
    def get_all_variable_names(self) -> [str]:
        variables = []
        for name in list(self.formulas.keys()):
            for variable in list(self.formulas[name].variables.keys()):
                variables.append(variable)
        return variables

    # Creates all formulas from folder formulas.
    # @frame CTkFrame - frame in which formula will be located.
    # @return [Formula] - created formulas.
    def create_formulas(self, frame) -> [FormulaBlueprint]:
        for formula_name in os.listdir("src/formulas"):
            if formula_name.endswith(".py"):
                self.formulas[formula_name] = getattr(
                    importlib.import_module("formulas." + formula_name.split(".py")[0]),
                    formula_name.split(".")[0],
                )(frame)
        return self.formulas

    # Searches and returns forula based on given name.
    # @name String - name of the formula.
    # @return String/None - found formula.
    def get_formula_by_name(self, formula_name: str) -> str:
        for name in list(self.formulas.keys()):
            if self.formulas[name] == formula_name:
                return self.formulas[formula_name]
        return None

    # Gets all excel files in inport folder.
    # @return [String] - Names of the files without ".xlsx".
    def get_import_excel_names(self) -> [str]:
        excel_names = []
        for excel in os.listdir("src/input"):
            if excel.endswith(".xlsx"):
                excel_names.append(excel.rsplit(".xlsx")[0])
        return excel_names

    # Runs calculation for each selected frame until there are no data for calculation and saves the results to ExcelOutput.
    # @output_file_name String - name of output excel file.
    def calculation(self, output_file_name: str) -> None:
        run = True
        row = 0
        while run:
            output = self.excel_input.get_data(self.get_all_needed_data_names(), row)
            row += 1
            if output == None:
                run = False
                self.excel_output.save_data(output_file_name)
            else:
                formula_output = {}
                for formula in self.get_wanted_formulas():
                    for var in list(formula.variables.keys()):
                        formula.variables[var] = output[var]
                    formula_output[formula.name] = formula.try_calculate()
                self.excel_output.add_calculated_data(formula_output)
