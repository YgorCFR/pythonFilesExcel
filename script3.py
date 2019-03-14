import pandas as pd
file = 'example.xlsx'

xl = pd.ExcelFile(file)

print(xl.sheet_names)

df1 = xl.parse('Sheet1')