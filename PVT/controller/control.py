import xlwings as xw
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PVT.model.CorrelacionesPVT import Bo
from PVT.model.CorrelacionesPVT import Pb
from PVT.model.CorrelacionesPVT import Rs
from PVT.model.CorrelacionesPVT import uo
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
CORRELACION_S = "Standing"
CORRELACION_AL = "AL_MARHOUN"
CORRELACION_B = "Beal"
CORRELACION_G = "Glaso"
def main():
    wb = xw.Book.caller()
    sheet = wb.sheets[SHEET_SUMMAR]

    df_TVD = (sheet[STOC_VALUES].options(pd.DataFrame, index=False, expand= "table").value)
    input_col_names = df_TVD["Valores"].to_list()
    Rs_value, Yo_value, Yg_value, T_value, P_value, API_value, BASIO, BASIO2 = tuple(input_col_names)
    inpt_idx = [CORRELACION_S, CORRELACION_AL]
    resultsBo = {}
    resultsPb = {}
    resultsRs = {}
    for col in inpt_idx:
        print(col)
        resultsBo[col] = Bo(col, Rs_value, Yg_value, Yo_value, T_value)
        resultsPb[col] = Pb(col, Rs_value, Yg_value, T_value, API_value, Yo_value)
        resultsRs[col] = Rs(col, P_value, API_value, T_value, Yg_value, Yo_value)



    #for col, idx in input_dict.items():
    #    results_dict[col] = Bo("Standing", )

    #Resultado del Bo por Standing & AL-Marhoun:
    #sheet[BO_STANDING].value = resultsBo[CORRELACION_S] #Bo("Standing", Rs_value, Yg_value, Yo_value, T_value)
    #sheet[BO_AL_MARHOUN].value = resultsBo[CORRELACION_AL] #Bo("AL_MARHOUN", Rs_value, Yg_value, Yo_value, T_value)


    #Resultado de Pb por Standing & AL-Marhoun:
    #sheet[PB_STANDING].value = resultsPb[CORRELACION_S] #Pb("Standing", Rs_value, Yg_value, T_value, API_value, Yo_value)
    #sheet[PB_AL_MARHOUN].value = resultsPb[CORRELACION_AL] #Pb("AL_MARHOUN", Rs_value, Yg_value, T_value, API_value, Yo_value)


    #Resultado del Rs por Standing & AL-Marhoun:
    #sheet[RS_STANDING].value = resultsRs[CORRELACION_S] #Rs("Standing", P_value, API_value, T_value, Yg_value, Yo_value)
    #sheet[RS_AL_MARHOUN].value = resultsRs[CORRELACION_AL] #Rs("AL_MARHOUN", P_value, API_value, T_value, Yg_value, Yo_value)

    #Caluclo de la uo por Beal & Glaso
    #sheet[UO_BEAL].value = uo("Beal", API_value, T_value)
    #sheet[UO_GLASO].value = uo("Glaso", API_value, T_value)
    PVT_summary_result = [resultsBo[CORRELACION_S], resultsBo[CORRELACION_AL], resultsPb[CORRELACION_S], resultsPb[CORRELACION_AL], resultsRs[CORRELACION_S], resultsRs[CORRELACION_AL]]
    sheet[BO_STANDING].options(transpose = True).value = PVT_summary_result
    print(PVT_summary_result)

    #Graficas Bo
    #df_resultsBo = pd.DataFrame(resultsBo)

    #eng_formatter = ticker.EngFormatter()
    #sns.set_style("white")
    #fig = plt.figure(figsize=(8, 6))
    #ax = sns.histplot(df_resultsBo[CORRELACION_S], color= "lightgray", kde=True)
    #ax.xaxis.set_major_formatter(eng_formatter)
    #plot = sheet.pictures.add(fig, name= "Histograma", left = sheet.range("J1").left)
    #print(plot)
if __name__ == "__main__":
    xw.Book("control.xlsm").set_mock_caller()
    main()

