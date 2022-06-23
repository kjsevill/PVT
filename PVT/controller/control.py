import xlwings as xw
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PVT.model.BO import BO

#Create names for sheets
SHEET_SUMMAR = "Datos"
SHEET_RESULTS = "Resultados"
#Name of columns

VALORES = "Valores"
VARIABLES = "Variables"


DET_VALUES = "BO_Valores"
DET_BO = "Bo"

def main():
    wb = xw.Book.caller()
    sheet = wb.sheets["Datos"]

    #Calculate Bo
    params = sheet[DET_VALUES].options(np.array, transpose=True).value
    print(params)
    sheet[DET_BO].value = BO(*params)




if __name__ == "__main__":
    xw.Book("control.xlsm").set_mock_caller()
    main()

