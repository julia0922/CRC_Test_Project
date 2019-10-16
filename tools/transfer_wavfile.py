#!/usr/bin/python
# -*- coding: utf-8 -*-

# 转换音频文件,包括转换的wav格式和pcm格式的文件
from data_control.transfile_bll import  Transfileobj
if __name__=="__main__":
    rootPath = "E:/audiofile/test/"    # 原音频文件路径
    wav_new_rootPath = "E:/audiofile/temp/"   # 转换为wav文件后存放的路径
    pcm_new_rootPath = "E:/audiofile/temp/"  # 转换为pcm文件后存放的路径
    is_trans_pcm=True   # 是否需要转换pcm格式

    # 开始转换wav为 16000HZ,16-bit,mono 后缀为.wav格式.
    obj=Transfileobj(rootPath,wav_new_rootPath,"wav")
    obj.run_trans()

    # 开始转换wav为 16000HZ,16-bit,mono 后缀为.pcm格式.
    if is_trans_pcm:
        obj = Transfileobj(rootPath, wav_new_rootPath, "pcm")
        obj.run_trans()
