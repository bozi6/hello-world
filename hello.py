from openpyxl import Workbook
from openpyxl.utils import get_column_letter
import math

wb = Workbook()
dest_filename = 'sample.xlsx'

ws1 = wb.active
ws1.title = "range names"

for row in range(1, 35):
    ws1.append(range(28))
ws2 = wb.create_sheet(title="Pi")

ws2['B2'] = 3.14
ws2['F5'] = math.pi

ws3 = wb.create_sheet(title="Data")
for row in range(4, 20):
     for col in range(3, 10):
         _ = ws3.cell(column=col, row=row, value="{0}".format(get_column_letter(col)))
print(ws3['E11'].value)
wb.save(filename = dest_filename)