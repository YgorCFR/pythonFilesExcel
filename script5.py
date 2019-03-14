import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np
from openpyxl import Workbook

df = pd.DataFrame({'a': [1,2,3,4],
              'b': [4,5,6,7]})
			  
write = ExcelWriter('Pandas-Example2.xlsx')

df.to_excel(writer, 'Sheet1', index=False)
writer.save()