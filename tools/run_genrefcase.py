from data_control.gen_refcase import Genrefcase
import os

'''
# 生成excel格式的用例信息.
if __name__=="__main__":
    rootpath="E:/ref/cmd_02_0005/excel/"
    dir_list=os.listdir(rootpath)
    for i in dir_list:
        excepath =rootpath+i  # 用例文件保存的路
        name_value=i.replace(".xlsx","")
        savepath="E:/ref/cmd_02_0005/ref/" +name_value
        if os.path.exists(savepath)==False:
            os.mkdir(savepath)

        Genrefcase(excepath,savepath).write_ref()

        Genrefcase().gen_configfile(savepath+"/config.txt",savepath,"/data1/audio_file/Add_CMD/cmd_02_0005/"+name_value+"/","cmd_02_0005/"+name_value)
'''



