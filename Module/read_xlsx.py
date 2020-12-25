# coding=UTF-8
#!/usr/bin/env python

import openpyxl

book = openpyxl.load_workbook('Resource/zhejiang2020.xlsx')

sheet = book.active

# 逐行遍历数据
for row in sheet.iter_rows(min_row=1, min_col=8, max_row=20, max_col=8):
    for cell in row:
        if cell.value.find('类') != -1:
            print(cell.value, end=" ")
    print()    