#/Users/ma073146/Desktop/Minance

import xlrd
from collections import Counter
from openpyxl import load_workbook
import pandas as pd



def main():
    #file = 'PYTHON_SAMPLE_FILE.xlsx'
    #xl = pd.ExcelFile(file)
    #print(xl.sheet_names)
    # Load a sheet into a DataFrame by name: df1
   # df1 = xl.parse('Sheet1')

    wb = load_workbook('./PYTHON_SAMPLE_FILE.xlsx')
    print(wb.get_sheet_names())
    choice = int(input("Intput for unique 1. CLIENT-ID 2. DATE 3. TRADEs"))



main()




def FindDuplicates(in_list):
    counts = Counter(in_list)
    two_or_more = [item for item, count in counts.items() if count >= 2]
    print two_or_more
    return len(two_or_more) > 0

workbook = xlrd.open_workbook(r"input.xls")
sheet = workbook.sheet_by_index(0)
col_a = [sheet.row(row)[choice].value for row in range(sheet.nrows)] # Read in all rows

print FindDuplicates(col_a)

