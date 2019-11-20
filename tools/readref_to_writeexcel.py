import os
import  openpyxl

reslultdir="E:/ref/cmd_02_0002/result/"
audio_path="E:/Add_CMD/cmd_02_0002/"
excelName="cmd_02_0002.xlsx"
workbook = openpyxl.Workbook()
childdirlist=os.listdir(reslultdir)
for child_dir in childdirlist:
    rootdir=reslultdir+child_dir+"/"
    if os.path.isdir(rootdir)==False:
        continue

    new_audio_path=audio_path+child_dir+"/"
    title_value=child_dir
    filelist=os.listdir(rootdir)

    worksheet = workbook.create_sheet(title=title_value)
    worksheet.append(["序号","ASR识别结果","正确文本"])
    for one_file in filelist:
        whole_filepath=rootdir+one_file
        print(whole_filepath)

        if os.path.isfile(whole_filepath)==False:
            continue

        if whole_filepath.endswith(".xlsx")==True:
            continue

        f=open(whole_filepath,"r",encoding="utf-8")
        alllines= f.readlines()
        row_count=0
        for one_line in alllines:
            print(one_line)
            print("*******************************")
            if str(one_line).find("序号")==0:
                continue

            if str(one_line).find("总计") == 0:
                continue

            wer_index=one_file.index("test")
            out_index=one_file.index(".out")
            cmd_path=new_audio_path+one_file[wer_index:out_index].replace("test","").upper()+".out/"
            print(one_file[wer_index:out_index].replace("test","")+".out")

            alist = one_line.split(" ")
            alist[0]=cmd_path+alist[0]+".wav"
            print(alist)
            worksheet.append(alist)
workbook.save(reslultdir+excelName)

