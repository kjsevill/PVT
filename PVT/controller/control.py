import xlwings as xw
from PVT.model.BO import BO

#Create names for sheets
SHEET_SUMMAR = "Datos"
SHEET_RESULTS = "Resultados"
#Name of columns

VALORES = "Valores"
VARIABLES = "Variables"



def main():
    wb = xw.Book.caller()
    sheet = wb.sheets["Datos"]




if __name__ == "__main__":
    xw.Book("control.xlsm").set_mock_caller()
    main()

