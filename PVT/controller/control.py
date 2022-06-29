import xlwings as xw
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PVT.model.BO import Bo
from PVT.model.Pb import Pb
from PVT.model.Rs import Rs
#from PVT.model.uo import uo
#------------------------------------
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
VALUES = "Valores"
def main():
    wb = xw.Book.caller()
    sheet = wb.sheets[SHEET_SUMMAR]

    df_TVD = (sheet[STOC_VALUES].options(pd.DataFrame, index=False, expand= "table").value)
    input_col_names = df_TVD["Valores"].to_list()
    Rs_value, Yo_value, Yg_value, T_value, P_value, API_value, BASIO, BASIO2 = tuple(input_col_names)


    #Calculo del Bo por Standing & AL-Marhoun:
    sheet[BO_STANDING].value = Bo("Standing", Rs_value, Yg_value, Yo_value, T_value)
    sheet[BO_AL_MARHOUN].value = Bo("AL_MARHOUN", Rs_value, Yg_value, Yo_value, T_value)


    #Calculo de Pb por Standing & AL-Marhoun:
    sheet[PB_STANDING].value = Pb("Standing", Rs_value, Yg_value, T_value, API_value, Yo_value)
    sheet[PB_AL_MARHOUN].value = Pb("AL_MARHOUN", Rs_value, Yg_value, T_value, API_value, Yo_value)


    #Calculo del Rs por Standing & AL-Marhoun:
    sheet[RS_STANDING].value = Rs("Standing", P_value, API_value, T_value, Yg_value, Yo_value)
    sheet[RS_AL_MARHOUN].value = Rs("AL_MARHOUN", P_value, API_value, T_value, Yg_value, Yo_value)

    #Caluclo de la uo por Beal & Glaso
    #sheet[UO_BEAL].value = uo("Beal", API_value, T_value)
    #sheet[UO_GLASO].value = uo("Glaso", API_value, T_value)


if __name__ == "__main__":
    xw.Book("control.xlsm").set_mock_caller()
    main()

