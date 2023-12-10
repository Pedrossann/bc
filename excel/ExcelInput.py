import pandas as pd
import os
import re


# Handles getting data from excel files and process them.
class ExcelInput:
    def __init__(self) -> None:
        self.variables = None
        self.excels = {}

    # Loads and saves all excel files from input folder.
    def open_excels(self):
        for variable_name in list(self.variables.keys()):
            self.excels[variable_name] = pd.read_excel(
                os.getcwd()
                + "\\input\\"
                + self.variables[variable_name]["excel"]
                + ".xlsx"
            )

    # Gets data from specific excel column based on name and row.
    def get_data(self, formula_variable_names, row):
        output = {}
        for variable in formula_variable_names:
            try:
                value = self.excels[variable].iloc[
                    row
                    + self.excel_column_number(self.variables[variable]["coordinates"])
                    - 2,
                    self.extract_numbers_from_string(
                        self.variables[variable]["coordinates"]
                    )
                    - 1,
                ]
            except IndexError:
                value = "-"
            output[variable] = value
        if self.check_if_var_is_null(output):
            output = None
        return output

    # Converts column to integer.
    # @column String ("B2", "C3", ...)
    # @return Integer column integer
    def excel_column_number(self, column):
        strings = re.sub(r"[^A-Za-z]", "", column)
        result = 0
        for char in strings:
            result = result * 26 + (ord(char) - ord("A") + 1)
        return result

    # Gets all numbers from the string.
    # string ("A1", "B2", ...)
    # @return Integer
    def extract_numbers_from_string(self, string) -> int:
        numbers = re.findall(r"\d+", string)
        numbers_list = [int(number) for number in numbers]
        return int("".join(map(str, numbers_list)))

    # Check if all data in this map are null.
    # @varList {"name": value}
    # @return True = empty/False
    def check_if_var_is_null(self, var_map):
        empty = True
        for var in list(var_map.keys()):
            if var_map[var] != "-":
                empty = False
        return empty
