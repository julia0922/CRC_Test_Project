from data_control.extract_wavfile_bll import Extractwavfile

# 提取测试集
if __name__=="__main__":
    # 提取指定的测试集
    audio_filepath="D:/aicolud_file/外部音频/Magicdata_20180127/Magicdata_20180127/001/"
    savepath="E:/extracfile/"
    e_list=['03_0078','03_0079']
    e_type=2   # 有1 和2 两个选项。
    Extractwavfile(audio_filepath,savepath,e_list,e_type).extract()




