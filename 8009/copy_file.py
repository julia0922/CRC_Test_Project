from common.operation_excel import  OperationExcel
from common.operation_file import  OperationFile

excel_path="E:/ref/cmd_02_0002/result/cmd_02_0002.xlsx"
savepath="E:/sucess_addcmd/"
ref_path="E:/sucess_addcmd/cmd_02_0002.txt"
obj, allname = OperationExcel(excel_path).get_all_sheetnames()
of_obj=OperationFile()
for item in allname:
    print("dfsdfdsf")
    if item.lower()=="sheet":
        continue

    print("************")
    worksheet = obj.get_sheet_by_name(item)
    rows = worksheet.max_row + 1
    print(rows)
    for r in range(3,rows):
        wav_value = worksheet.cell(r, 1).value  # wav的信息
        rate_value = str(worksheet.cell(r, 10).value).strip()  # rate 信息
        print(wav_value,rate_value)
        sucessvalue="0.00"
        if rate_value==sucessvalue:
            print("开始拷贝")
            targetpath=savepath+str(wav_value).replace("E:/","")
            of_obj.start_copy_file(wav_value,targetpath)
            audiovalue="20190919/"+str(wav_value).replace("E:/","")
            of_obj.write_fileinfo(ref_path, audiovalue + "\n")
        else:
            print("不相等..")

