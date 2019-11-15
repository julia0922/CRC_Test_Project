import  os


import wave
import contextlib
from common.operation_file import  OperationFile


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



filepath=dir_path+"059M18_06_46_0056.wav"
with contextlib.closing(wave.open(filepath, 'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
    print(duration)
