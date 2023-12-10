import os
import importlib
import pandas as pd


# Handles all main logic for the calculation of the Formulas.
class FormulasHandler:
    def __init__(self, excelGet, excelOutput):
        self.formulas = []
        self.excelGet = excelGet
        self.excelOutput = excelOutput

    # Saves switch states of wanted formulas.
    def saveWantedFormulas(self, switchStates):
        for formula in self.formulas:
            formula.wanted = switchStates[formula.name]
        self.excelOutput.createSavingStructure(self.getWantedFormulas())

    # Loads all variables, that are needed for calculating all selected formulas.
    def getAllNeededDataNames(self) -> [str]:
        neededData = []
        for formula in self.formulas:
            if formula.wanted == True:
                for variable in list(formula.variables.keys()):
                    neededData.append(variable)

        return neededData

    # Returns all variables.
    def getAllDataNames(self) -> [str]:
        allvariables = []
        for formula in self.formulas:
            for variable in list(formula.variables.keys()):
                allvariables.append(variable)
        return allvariables

    # Creates all formulas from folder formulas.
    def createAllFormulas(self, window) -> [object]:
        for scr in os.listdir("formulas"):
            if scr.endswith(".py"):
                self.formulas.append(
                    getattr(
                        importlib.import_module("formulas." + scr.split(".py")[0]),
                        scr.split(".")[0],
                    )(window)
                )
        return self.formulas

    # Searches and returns forula based on given name.
    def getFormulaByName(self, name):
        for formula in self.formulas:
            if formula.name == name:
                return formula
        return None

    # Gets all excel files in inport folder.
    def getImportExcelNames(self):
        excelNames = []
        for excel in os.listdir("input"):
            if excel.endswith(".xlsx"):
                excelNames.append(excel.rsplit(".xlsx")[0])
        return excelNames

    # Runs calculation for each selected frame until there are no data for calculation.
    def calculation(self):
        calc = True
        row = 0
        while calc:
            output = self.excelGet.getData(self.getAllNeededDataNames(), row)
            row += 1
            if output == None:
                calc = False
                self.excelOutput.saveData("outputName")
            else:
                formulaOutput = {}
                for formula in self.getWantedFormulas():
                    for var in list(formula.variables.keys()):
                        formula.variables[var] = output[var]
                    formulaOutput[formula.name] = formula.calculate()
                self.excelOutput.addSavingData(formulaOutput)

    # Gets all wanted formulas.
    def getWantedFormulas(self):
        wantedFormulas = []
        for formula in self.formulas:
            if formula.wanted:
                wantedFormulas.append(formula)
        return wantedFormulas
