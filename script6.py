import xlwt

wb = xlwt.Workbook()

ws = wb.add_sheet("A Test Sheet")


font0 = xlwt.Font()
font0.name = "Times New Roman"
font0.colour_index = 2
font0.bold = True

style1 = xlwt.XFStyle()
style1.num_format_str = "D-MMMM-YY"
style1.font = font0

from datetime import datetime
ws.write(1,0, datetime.now(), style1)
ws.write(2,0,1)
ws.write(2,1,1)
ws.write(2,2, xlwt.Formula("A3+B3"))
#ws.write(0,0, "Test Value")
#
wb.save("dateWrite.xls")

