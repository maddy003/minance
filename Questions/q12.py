from openpyxl import load_workbook

import pandas as pd

file = 'PYTHON_SAMPLE_FILE.xlsx'
df = pd.read_excel(r'PYTHON_SAMPLE_FILE.xlsx')
print(df)


def main():
    data = pd.read_excel(r'PYTHON_SAMPLE_FILE.xlsx')
    df = pd.DataFrame(data)
    df = df.groupby('SYMBOL')['CLIENT_ID'].nunique()
    print(df)


main()
