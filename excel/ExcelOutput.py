import pandas as pd
import os


# Handles saving data into excel file.
class ExcelOutput:
    def __init__(self):
        self.data = {}

    # Create basic structure in which calculated data will be saved for excel output.
    # @wanted_formulas [String] - names of wanted formulas.
    def create_saving_structure(self, wanted_formulas):
        for formula in wanted_formulas:
            self.data[formula.name] = []

    # Add calculated data to map for saving.
    # @data {"formulaName": value}
    def add_calculated_data(self, data):
        for name in list(data.keys()):
            self.data[name].append(data[name])

    # Saves calculated data.
    # @file_name String - name of the file we want to save data to.
    def save_data(self, file_name):
        df = pd.DataFrame(self.data)
        df.to_excel(os.getcwd() + f"/output/{file_name}.xlsx", index=False)
