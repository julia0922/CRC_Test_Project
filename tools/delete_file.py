from common.operation_file import OperationFile
from common.operation_excel import OperationExcel
import os

rootdir="D:/audio_file/wav音频/美的第一批递交/空调儿童/"
excelpath="D:/audio_file/source音频/美的第一批递交/空调儿童和全品类空音频列表.xlsx"
of_obj=OperationFile()
oe_obj=OperationExcel(excelpath)
listvalue=oe_obj.getcell_value(excelName="空调儿童",index=1)
print(listvalue)

list=of_obj.getfilelistbydir(rootdir)
print(list)
for filepath in list:
    basename_value=os.path.basename(filepath)
    print(basename_value)
    if basename_value in listvalue:
        print("**********************************************",filepath)
        os.remove(filepath)