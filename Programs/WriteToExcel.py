# To write data to excel file

import openpyxl
import os

cwd=os.getcwd()

path=cwd+"\\"+"ProjectFiles"+"\\"+"WriteFile.xlsx"

workbook=openpyxl.load_workbook(path)
sheet=workbook.get_sheet_by_name("Sheet1")

for r in range(1,6):
    for c in range(1,5):
        sheet.cell(row=r,column=c).value=str(r)+" "+str(c)
workbook.save(path)