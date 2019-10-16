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
product_id = '278575321' #填入产品Id
apikey = 'x' #填入apikey

# sit环境执行地址
# 地址修改为：dds-hb.dui.ai
#后续你们测试的环境从hn.dui.ai迁到dds-hb.dui.ai，由于我们内部集群的迁移，华南环境今晚下线了@何胖橙子
#url = 'wss://hn.dui.ai/dds/v1/test?serviceType=websocket&productId='+product_id
url = 'wss://dds-hb.dui.ai/dds/v1/test?serviceType=websocket&productId=' + product_id
# 旧地址
#url = 'ws://dds.dui.ai/dds/v1/test?serviceType=websocket&productId='+product_id
#wavfile="E:/audiofile/音频/001M25_00_01_0001.wav"
wavfile="E:/新建文件夹/新建文件夹/043F/043F36_10_044M56_00_045M32_0_cmd_564.wav"
def on_message(ws, message):
   print ('Message>>>>>>>>>>>>>>>>>>>>>>>>')
   print(message)
   mJson = json.loads(message)
   text = ""
   if 'eof' in message:
       text = mJson['text']
       print(text.replace(" ",""))

   print ('Message<<<<<<<<<<<<<<<<<<<<<<<<')

def on_error(ws, error):
    print ('error>>>>>>>>>>>>>>>>>>>>>>')
    print (error)
    print ('error<<<<<<<<<<<<<<<<<<<<<<')

def on_close(ws):
    print ("### closed ###")

def on_open(ws):
    def run(*args):
        content = {
            "topic": "recorder.stream.start",
            "recordId": "21354578ijhgbvdrt33",
            "sessionId": "testaasdfas2333666",
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
                "aiType": "asr"
        }
        ws.send(json.dumps(content))
        step = 3200 #如果audioType是wav，此处需要修改为3200
        with open(wavfile, 'rb') as f:
            while True:
                data = f.read(step)
                if data:
                    ws.send(data, ABNF.OPCODE_BINARY)
                if len(data) < step:
                    break
                time.sleep(0.1)

        ws.send('', ABNF.OPCODE_BINARY)
        time.sleep(5)
        ws.close()
    _thread.start_new_thread(run, ())

def func_one():
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(url,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()

if __name__ == "__main__":
    func_one()

