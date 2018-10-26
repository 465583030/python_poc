# coding=utf-8

import pandas as pd
# import numpy as np

# import matplotlib.pyplot as plt

file_name = "/Users/cox/Downloads/compared/20181014.xlsx"

# xls_file = pd.ExcelFile(file_name, dtype='object') # 统一先按照str读入，之后转换
# print(xls_file.head(5))

# table = xls_file.parse('Sheet1', dtype='object')

# file_name = "../源代码和数据/朝阳医院2016年销售数据.xlsx"
table = pd.read_excel(file_name, sheeetname = '20181014电子摄像', dtype='object')
print(table.tail(5))