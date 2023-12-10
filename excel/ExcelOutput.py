import pandas as pd
import os


class ExcelOutput:
    def __init__(self):
        self.data = {}

    # Create basic structure in which calculated data will be saved for excel output.
    def createSavingStructure(self, wantedFormulas):
        for formula in wantedFormulas:
            self.data[formula.name] = []

    def addSavingData(self, data):
        for name in list(data.keys()):
            self.data[name].append(data[name])

    def saveData(self, fileName):
        df = pd.DataFrame(self.data)
        df.to_excel(os.getcwd() + f"/output/{fileName}.xlsx", index=False)
