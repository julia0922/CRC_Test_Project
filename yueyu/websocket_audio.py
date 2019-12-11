#!/usr/bin/env python
# coding=utf-8
### websocket模块https://pypi.python.org/pypi/websocket-client
### wavfile是一个speex压缩的ogg文件,文件格式是Ogg data, Speex audio
import websocket
from websocket import ABNF
import time
import _thread
import json
import ssl
import uuid
product_id = '278571807' #填入产品Id
apikey = 'x' #填入apikey
#url = 'ws://dds.dui.ai/dds/v1/test?serviceType=websocket&productId='+product_id
#url = "ws://127.0.0.1:10002/cloud/connect"
url="ws://linksit.aimidea.cn:10000/cloud/connect"
#url = "ws://linksit.aimidea.cn:10000/cloud/connect"
#url = "ws://101.37.187.252:10000/cloud/speech/trans"
#url = "ws://120.55.103.222:9080/v1/audio"
# url = "ws://localhost:9080/v1/audio"
# wavfile = '/Users/kiefer/Downloads/weather.wav' #ogg文件的绝对路径
# wavfile = '/Users/kiefer/Downloads/startautocooking.wav' #ogg文件的绝对路径

# weather,music
# startquickrice startautocooking cookerfastrice  opensmartlight livingroomcookerstartwork
#comhome
# tired skin how-fish cantonese eatwhat onekeycooking2
#wavfile = 'E:/audiofile/100人粤语-采集-0910/结果数据/100人粤语-采集-批次2-0910/wav/G30037/037F21_F01_41_0415.wav'
wavfile="诗.wav"

def get_time_stamp():
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "%s.%03d" % (data_head, data_secs)
    return time_stamp

def on_message(ws, message):
   print ('Message>>>>>>>>>>>>>>>>>>>>>>>>')
   print (get_time_stamp())
   print (message)
   return message
#  print ('Message<<<<<<<<<<<<<<<<<<<<<<<<')
#    if json.loads(message)["eof"] == 1: 
#        print "terminate now!!"
#        ws.close()
   
def on_error(ws, error):
    print ('error>>>>>>>>>>>>>>>>>>>>>>')
    print( get_time_stamp())
    print (error)
    print ('error<<<<<<<<<<<<<<<<<<<<<<')
   
def on_close(ws):
    print (get_time_stamp())
    print ("### closed ###")
     
# def on_data(ws, resp, datatype, ctnu):
#     print datatype
   
def on_open(ws):
    def run(*args):
        content = {
            "topic": "cloud.speech.trans",
            "mid": "1508232047194123",
            "version": "1.0",
            "request": {
                "timestamp": 1508232047199,
                "sessionId": "aaaadsfasdffsdf123"
            },
            "params": {
                "audio": {
                    "audioType": "wav",
                    "sampleRate": 16000,
                    "channel": 1,
                    "sampleBytes": 2
                },
                "asrIsp": "xfyun",
                "ttsIsp": "xfyun"
            }
        }
        opencontent = {
            "topic": "cloud.connect",
            "mid": "1508232047154",
            "version": "1.0",
            "request": {
                "apiVer": "1.0.0",
                "timestamp": 1508232047194,
                "pki":"aaaadsfasdffqwe"
            },
            "params": {
                "sn": "0000DB11138104887174101101744561",
                    "category": "B1",
                "model": "456",
                "id": "1099511840456",
                "ip": "0.0.0.0",
                "mac": "88e9fe5d3456",
                "random": "545123"
            }
        }
        print ("send start: ",get_time_stamp())
        ws.send(json.dumps(opencontent), ABNF.OPCODE_TEXT)
        ws.send(json.dumps(content), ABNF.OPCODE_TEXT)
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
        print ("send end: " + get_time_stamp())
    _thread.start_new_thread(run, ())

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(url,
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
