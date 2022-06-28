import xlwings as xw
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PVT.model.BO import Bo

#Create names for sheets
SHEET_SUMMAR = "Datos"
SHEET_RESULTS = "Resultados"

# Name of columns for distribution definitions
VARIABLES = "Variables"
VALORES = "Valores"
PARAMETROS= "Parametros"
CORRELACION= "Correlación"

# Data
STOC_VALUES = "df_bo_calculator"
# Result cells # Call range cells from MS Excel
BO_STANDING = "Bo_STANDING"
BO_AL_MARHOUN = "Bo_Al_Marhoun"
RS_STANDING = "Rs_Standing"
RS_AL_MARHOUN = "Rs_Al_Marhoun"
PB_STANDING = "Pb_Standing"
PB_AL_MARHOUN = "Pb_Al_Marhoun"
UO_BEAL = "uo_Beal"
UO_GLASO = "uo_Glaso"
VALUES = "values"
def main():
    wb = xw.Book.caller()
    sheet = wb.sheets[SHEET_SUMMAR]


    PARAMETROS = sheet[VALUES].options(np.array, transpose=True).value
    print(PARAMETROS)
    sheet[BO_STANDING].value = Bo(*PARAMETROS)


if __name__ == "__main__":
    xw.Book("control.xlsm").set_mock_caller()
    main()

