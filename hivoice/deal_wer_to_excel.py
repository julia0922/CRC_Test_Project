

import openpyxl
import os
from common.operation_file import OperationFile


aa="088F27_00_62_0132 微蒸烤一体机中高火快捷微波六分钟  微蒸烤一体机中高火快捷微波六分钟  0  0  0.00"

line_list = aa.split(" ")
print(line_list)


reslultdir="D:/testresult/云之声/2019-11-28 全品类/云知声测试结果/"
excelName="cmd_02_0002.xlsx"



of_obj=OperationFile()

workbook = openpyxl.Workbook()
worksheet = workbook.create_sheet(title="aaa")
worksheet.append(["序号", "正确文本", "ASR识别结果", "识别率"])

childdirlist=os.listdir(reslultdir)
for child_dir in childdirlist:
    rootdir=reslultdir+child_dir+"/"
    if os.path.isdir(rootdir)==False:
        continue

    new_audio_path=reslultdir+child_dir+"/"
    filelist=os.listdir(new_audio_path)


    for filename in filelist:
        filpath=new_audio_path+"/"+filename
        alllines = of_obj.read_fileinfo(filpath)
        i = 0
        for one_line in alllines:
            print(one_line)
            print(i)
            if i == 0 or one_line.find("总计") != -1:
                print("hahahhahahah")
                i = i + 1
                continue

            line_list = one_line.split(" ")
            exceptvalue=""
            if line_list[2]=="":
                exceptvalue=line_list[3]
            else:
                exceptvalue = line_list[2]

            lastvalue=line_list[len(line_list)-1].replace("\n","")
            result_value=True
            if lastvalue!="0.00":
                result_value = False

            worksheet.append([line_list[0],exceptvalue,line_list[1],result_value])

workbook.save(reslultdir+excelName)

