#!/usr/bin/env python

from openpyxl import Workbook

book = Workbook()
sheet = book.active

sheet.freeze_panes = 'B2'

book.save('freezing.xlsx')
