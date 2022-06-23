import xlwings as xw
from PVT.model.BO import BO


def main():
    wb = xw.Book.caller()




if __name__ == "__main__":
    xw.Book("control.xlsm").set_mock_caller()
    main()

