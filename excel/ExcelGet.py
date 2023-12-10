import pandas as pd
import os
import re


class ExcelGet:
    def __init__(self) -> None:
        self.variables = None
        self.excels = {}

    def openExcels(self):
        print(self.variables)
        for variableName in list(self.variables.keys()):
            self.excels[variableName] = pd.read_excel(
                os.getcwd()
                + "\\input\\"
                + self.variables[variableName]["excel"]
                + ".xlsx"
            )

    # Gets data from specific excel column based on name and row.
    def getData(self, formulaVariableNames, row):
        output = {}
        for var in formulaVariableNames:
            try:
                value = self.excels[var].iloc[
                    row
                    + self.excelColumnNumber(self.variables[var]["coordinates"])
                    - 2,
                    self.extractNumbersFromString(self.variables[var]["coordinates"])
                    - 1,
                ]
            except IndexError:
                value = "-"
            output[var] = value
        if self.checkIfVarIsNull(output):
            output = None
        return output

    # Converts column string (A, B, ..) to integer.
    def excelColumnNumber(self, column):
        strings = re.sub(r"[^A-Za-z]", "", column)
        result = 0
        for char in strings:
            result = result * 26 + (ord(char) - ord("A") + 1)
        return result

    # Gets all numbers from the string.
    def extractNumbersFromString(self, string):
        numbers = re.findall(r"\d+", string)
        numbList = [int(number) for number in numbers]
        return int("".join(map(str, numbList)))

    def checkIfVarIsNull(self, varList):
        empty = True
        for var in list(varList.keys()):
            if varList[var] != "-":
                empty = False
        return empty
