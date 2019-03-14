import xlrd

workbook = xlrd.open_workbook("tools.xlsx")

worksheet = workbook.sheet_by_index(0)

print("the value at row 4 and column2 is: {0}".format(worksheet.cell(0,0).value))

sheet_count = workbook.nsheets
print("the total number of sheets: {0}".format(sheet_count))

sheets_name = workbook.sheet_names()
print("sheet names: {0}".format(sheets_name))

total_rows = worksheet.nrows
total_cols = worksheet.ncols
print("number of rows: {0}, and number of columns: {1}".format(total_rows, total_cols))

table = list()
record = list()

for x in range(total_rows):
   for y in range(total_cols):
      record.append(worksheet.cell(x,y).value)
   table.append(record)
   record = []
   x += 1
print(table)