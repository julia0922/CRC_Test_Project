from data_control.gen_refcase import Genrefcase

# 生成excel格式的用例信息.
if __name__=="__main__":
    #excepath = "D:/audio_file/测试案例/20人录音第一批交付-全品类-wav.xlsx"  # 用例文件保存的路
    savepath="D:/audio_file/测试案例/云知声/"
    #Genrefcase(excepath,savepath).write_ref()

    Genrefcase().gen_configfile(savepath+"/config.txt",savepath,"/data1/audio_file/wav/20人录音第一批交付-全品类/","20人录音第一批交付-全品类")
