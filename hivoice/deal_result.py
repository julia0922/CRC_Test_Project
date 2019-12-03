# 处理云知声测试结果
import os
from common.operation_file import OperationFile
import openpyxl

# 测试结果根路径
rootpath="D:/testresult/云之声/2019-11-28 全品类/全品类第二批/"
mark="testsecondproduct"

workbook=openpyxl.Workbook()
work_sheet=workbook.create_sheet("识别率")
work_sheet.append(["音频","总数","成功数","失败数","成功率","WER/SER"])

of_obj=OperationFile()
file_list=os.listdir(rootpath)

alltotal=0
allright=0
for one_file in file_list:
    print(one_file)
    if one_file.find("ASR_Result")==-1:
        continue

    if one_file.find(mark)==-1:
        continue

    filpath=rootpath+one_file
    alllines=of_obj.read_fileinfo(filpath)
    lastvalue=alllines[9]
    print(lastvalue)

    last_list=lastvalue.split(" ")
    print(last_list)

    total=int(str(last_list[2]).replace(",",""))
    right=int((last_list[5]).replace(",",""))
    fail=total-right

    sucess_rate = (right / total) * 100
    sucess_rate_value = "{:.2f}%".format(sucess_rate)

    '''
    name=one_file.replace(mark,"").replace("ASR_Result_test","")
    namelist=name.split("_")

    item_name=namelist[1]
    print(item_name)
    '''
    alltotal=alltotal+total
    allright=allright+right

    item_name=alllines[0].replace("=","").replace("test","")
    work_sheet.append([item_name,total,right,fail,sucess_rate_value,last_list[7]])

total_rate = (allright / alltotal) * 100
total_rate_value = "{:.2f}%".format(total_rate)
work_sheet.append(["合计",alltotal,allright,alltotal-allright,total_rate_value])
workbook.save(rootpath+"全品类第二批识别率.xlsx")

