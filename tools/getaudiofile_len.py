import  os


import wave
import contextlib
from common.operation_file import  OperationFile

import numpy as np
filepath="E:/audiofile/wav音频/9月20日交付空调项目数据-wav/019魏建雄空调/019M20_07_42_0001.wav"
with contextlib.closing(wave.open(filepath, 'r')) as f:
    print(f.getparams())    # 输出信息（声道，采样宽度，采样率，总帧数，唯一标识，无损）
    # 总帧数 =帧率/时间
    num_frame=f.getnframes()
    num_channel=f.getnchannels()
    framerate = f.getframerate()  # 获取帧速率
    print(num_frame)
    str_data = f.readframes(num_frame)  # 读取全部的帧
    wave_data = np.fromstring(str_data, dtype=np.short)  # 将声音文件数据转换为数组矩阵形式
    wave_data.shape = -1, num_channel  # 按照声道数将数组整形，单声道时候是一列数组，双声道时候是两列的矩阵
    wave_data = wave_data.T  # 将矩阵转置
    wave_data = wave_data
    print(wave_data, framerate)





'''
of_obj=OperationFile()
dir_path="D:/audio_file/source音频/美的第一批递交/全品类/068/"
dirlist=os.listdir(dir_path)

copypath="D:/全品类/068/"
if os.path.exists(copypath)==False:
    os.makedirs(copypath)
for one_file in dirlist:
    if one_file.endswith(".wav")==False:
        continue

    filepath=dir_path+one_file
    with contextlib.closing(wave.open(filepath,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        print(float(duration))
        if float(duration)<=1.30:
            print("*********************************************************")
            of_obj.start_copy_file(filepath,copypath+one_file)
'''

