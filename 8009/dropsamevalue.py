import pandas as pd

excelath=pd.read_excel("D:/MyData/ex_shenjf1/Desktop/13.xlsx")
print(excelath['wav'].drop_duplicates())

