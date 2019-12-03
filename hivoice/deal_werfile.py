# 处理云知声测试结果
import os
from common.operation_file import OperationFile
import openpyxl
from common.re_num_to_characters import  ReplaceNumCharacters

# 测试结果根路径
rootpath="D:/testresult/云之声/2019-11-28 全品类/1128/第五批/"

new_rootpath=rootpath+"new/"
excelpath=new_rootpath+"全品类第五批.xlsx"

if os.path.exists(new_rootpath)==False:
    os.makedirs(new_rootpath)

rc_obj=ReplaceNumCharacters()
of_obj=OperationFile()
file_list=os.listdir(rootpath)

#file_list=["wer_testfirstproduct_059_30_2019_11_28_10_55_38"]


wb=openpyxl.Workbook()
ws=wb.create_sheet("识别率")
allright=0
alltotal=0

for one_file in file_list:
    print(one_file)
    new_all_line = ""
    total_count = 0
    right_count = 0

    if one_file.find("wer_")==-1:
        continue

    if one_file.find("wer_")==-1:
        continue

    filpath = rootpath + one_file
    alllines = of_obj.read_fileinfo(filpath)
    i=0
    for one_line in alllines:
        print(one_line)
        print(i)
        if i==0 or one_line.find("总计")!=-1:
            print("hahahhahahah")
            new_all_line=new_all_line+one_line
            i = i + 1
            continue


        total_count=total_count+1
        print(total_count)
        line_list=one_line.split(" ")
        print(line_list)
        lastvalue=line_list[len(line_list)-1].replace("\n","")
        if lastvalue=="0.00":
            print("****************************")
            new_all_line = new_all_line + one_line
            right_count=right_count+1
            continue

        asr_value=line_list[1]   # asr 返回的值
        right_value=line_list[2]  # 正确文本

        new_asrvalue=rc_obj.replace_num_value(asr_value).replace("挡","档")
        new_right_value=rc_obj.replace_num_value(right_value).replace("挡","档")

        if new_asrvalue==new_right_value:
            a=line_list[0]+" "+ new_asrvalue +" "+ new_right_value+"  "+ "0"+"  "+"0"+"  "+"0.00"+"\n"
            new_all_line = new_all_line + a
            print(a)
            print(new_all_line)

            right_count = right_count + 1
        else:
            new_all_line = new_all_line + one_line



    if os.path.exists(new_rootpath+one_file)==True:
        os.remove(new_rootpath+one_file)

    of_obj.write_fileinfo(new_rootpath+one_file,new_all_line)

    sucess_rate = (right_count / total_count) * 100
    sucess_rate_value = "{:.2f}%".format(sucess_rate)

    namelist=one_file.split("_")
    name=namelist[2]
    ws.append([name,total_count,right_count,total_count-right_count,sucess_rate_value])
    alltotal = alltotal +total_count
    allright=allright+right_count


total_rate = (allright / alltotal) * 100
total_rate_value = "{:.2f}%".format(total_rate)
ws.append(["合计",alltotal,allright,alltotal-allright,total_rate_value])

wb.save(excelpath)






