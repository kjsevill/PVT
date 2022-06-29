import xlwings as xw
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PVT.model.BO import BO

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
PVT_RESULTS = "pvt_results"
# Indexes of summary results
BO_STANDING_IDX, BO_AL_MARHOUN_IDX, RS_STANDING_IDX, RS_AL_MARHOUN_IDX, PB_STANDING_IDX, PB_AL_MARHOUN_IDX, UO_BEAL_IXD, UO_GLASO_IDX = 0, 1, 2, 3, 4, 5, 6, 7

def main():
    wb = xw.Book.caller()
    sheet = wb.sheets["Datos"]


    # Import dataframe from Ms. Excel
    df_bo_calculator = (
        sheet[STOC_VALUES].options(pd.DataFrame, index=False, expand="table").value
    )


if __name__ == "__main__":
    xw.Book("control.xlsm").set_mock_caller()
    main()

