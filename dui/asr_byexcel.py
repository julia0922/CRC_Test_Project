#!/usr/bin/env python
# coding=utf-8
### websocket模块https://pypi.python.org/pypi/websocket-client
### wavfile是一个speex压缩的ogg文件,文件格式是Ogg data, Speex audio
import websocket
from gevent import os
from websocket import ABNF
import time
import _thread
import json
import xlrd
from xlutils.copy import copy

# sit环境执行地址
product_id = '278575321' #填入产品Id
url = 'wss://dds-hb.dui.ai/dds/v1/test?serviceType=websocket&productId=' + product_id
excel_path="D:/100人粤语-采集-批次临时普通话-执行结果1/汇总.xlsx"
#音频文件路径
root_cmd_path="E:/audiofile/100人粤语数据-第二批交付（普通话2人）/data/wav/"

# 获取sheet
table =None
data=None

index=2
except_value=""  #预期结果

currentindex=0
success_total=0
fail_total=0
total=0


def on_message(ws, message):
   print ('Message>>>>>>>>>>>>>>>>>>>>>>>>')
   print(message)
   if(message == "音频为空"):
       text = "音频为空"
   else:
       mJson = json.loads(message)
       text=""
       if 'eof' in message:
         text = mJson['text']

   global success_total,fail_total,total
   index=currentindex
   print(index)
   text=str(text).replace(' ', '').replace("，","")
   print("返回值:",text)
   table.put_cell(index, 2, 1, text, format)
   total=total+1
   except_value = table.cell(index, 1).value
   except_value = str(except_value).replace("，", "").replace("？", "").replace("（","").replace("）","")
   print("期望值：",except_value)
   if(except_value.lower()==text.lower()):
       table.put_cell(index , 3, 1, str(True), format)
       success_total=success_total+1
   else:
       table.put_cell(index , 3, 1, str(False), format)
       fail_total=fail_total+1
   print ('Message<<<<<<<<<<<<<<<<<<<<<<<<')

def on_error(ws, error):
    print ('error>>>>>>>>>>>>>>>>>>>>>>')
    print (error)
    save_sucessrate()
    print ('error<<<<<<<<<<<<<<<<<<<<<<')

def on_close(ws):
    print ("### closed ###")
    save_sucessrate()
    if isEnd==False:
        ws = websocket.WebSocketApp(url,
                                    on_message=on_message,
                                    on_error=on_error,
                                    on_close=on_close)
        ws.on_open = on_open
        ws.run_forever()

def save_sucessrate():
    if total != 0:
        sucess_rate = (success_total / total) * 100
        sucess_rate_value = "{:.2f}%".format(sucess_rate)
        table.put_cell(0, 1, 1, sucess_rate_value, format)
        wb = copy(data)
        wb.save(excel_path)


def on_open(ws):
    def run(*args):
        global currentindex, table, data
        global success_total, fail_total, total
        global isEnd
        isEnd=False

        # 获取数据
        data = xlrd.open_workbook(excel_path)
        # 获取所有的names
        names = data.sheet_names()
        for name in names:
            # 获取sheet
            success_total = 0
            fail_total = 0
            total = 0

            print("总案例数:" + str(total))
            table = data.sheet_by_name(name)
            print("当前sheet：" + name)
            # 获取总行数
            nrows = table.nrows
            print("总行数:" + str(nrows))
            cmd_path = root_cmd_path+name
            print(cmd_path)
            currentindex = 0
            for i in range(index, nrows):
                wav_value = table.cell(i, 0).value  # wav文件值
                if wav_value.strip() == '':
                    continue
                print("path:" + wav_value)
                result_value =str(table.cell(i, 3).value)  # 预期结果值
                print(result_value)
                if result_value.strip()!="" and result_value!="None":
                    print("dddddddddddddddddddddddd")
                    continue

                '''
                ret = wav_value.find(name)
                ret1 = wav_value.find(".wav")
                if ret == -1:
                    wav_value = name + "_" + wav_value + ".wav"
                elif(ret1==-1):
                    wav_value = wav_value + ".wav"
                '''

                #wav_value=sheetName+"_"+wav_value+".wav"
                #wav_value =  wav_value + ".wav"
                ret1 = wav_value.find(".wav")
                if ret1 == -1:
                    wav_value=wav_value+".wav"
                wav_path = cmd_path + "/" + wav_value  # wav 路径
                print("***************************************")
                print(wav_path)
                currentindex = i
                print("当前index" + str(currentindex))
                if (os.path.exists(wav_path) == False):
                    print("音频路径为空")
                    #on_message(ws,"音频为空")
                    continue
                print("index:"+str(i))
                except_value = table.cell(i, 1).value  # 预期结果值
                content = {
                    "topic": "recorder.stream.start",
                    "recordId": "21354578ijhgbvdrt02",
                    "audio": {
                        "audioType": "wav",
                        "sampleRate": 16000,
                        "channel": 1,
                        "sampleBytes": 2
                    },
                    "asrParams": {
                        "enableVAD": False,
                        "realBack": False,
                        "toneEnable": True
                    },
                    "aiType":"asr"
                }
                ws.send(json.dumps(content))
                step = 3200 #如果audioType是wav，此处需要修改为3200
                with open(wav_path, 'rb') as f:
                    while True:
                        wave_data = f.read(step)
                        if wave_data:
                            ws.send(wave_data, ABNF.OPCODE_BINARY)
                        if len(wave_data) < step:
                            break
                        time.sleep(0.1)
                ws.send('', ABNF.OPCODE_BINARY)
                time.sleep(0.6)
            save_sucessrate()
        isEnd=True
        ws.close()
    _thread.start_new_thread(run, ())

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(url,
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()