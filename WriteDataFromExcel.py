from openpyxl import Workbook
from openpyxl.reader.excel import load_workbook

wb = load_workbook(filename="excelfile.xlsx")

sh = wb['Sheet']

print(sh['A1'].value)
