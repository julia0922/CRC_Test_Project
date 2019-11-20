from common.operation_excel import  OperationExcel
from common.operation_file import  OperationFile
import os


rootpath="D:/aicolud_file/外部音频/Magicdata_20180127/Magicdata_20180127/"
excel_path="D:/aicolud_file/外部音频/Magicdata_20180127/（非离线）纯在线本机&场景指令词表.xlsx"
savepath="E:/audiofile/离在线音频/（非离线）纯在线本机&场景指令词表/"
obj, allname = OperationExcel(excel_path).get_all_sheetnames()
of_obj=OperationFile()
for item in allname:
    if item.lower()=="sheet":
        continue

    print("************")
    worksheet = obj.get_sheet_by_name(item)
    rows = worksheet.max_row + 1
    print(rows)
    for r in range(1,rows):
        wav_value = worksheet.cell(r, 1).value  # wav的信息
        print(wav_value)
        rate_value = str(worksheet.cell(r, 10).value).strip()  # rate 信息
        print("开始拷贝")
        spitlist = wav_value.split("_")
        child_dir=(spitlist[2]+"_"+spitlist[3].replace(".wav",""))
        wav_path=rootpath+item+"/wav/"+wav_value
        print(wav_path)
        if os.path.exists(wav_path)==False:
            wav_path="E:/audiofile/testin云测8月30号递交数据/source/"+item+"/"+wav_value
            if os.path.exists(wav_path)==False:
                wav_path = "E:/audiofile/原音频/9月20日交付空调项目数据/" + item + "/" + wav_value

        targetpath=savepath+child_dir
        if os.path.exists(targetpath)==False:
            os.makedirs(targetpath)
        of_obj.start_copy_file(wav_path,targetpath+"/"+wav_value)

