#!/usr/bin/env python
# coding=utf-8
### websocket模块https://pypi.python.org/pypi/websocket-client
### wavfile是一个speex压缩的ogg文件,文件格式是Ogg data, Speex audio
import websocket
from gevent import os
from websocket import ABNF
import time
import _thread
import base64
import hashlib
import os
import json

BASE_URL = "wss://wsapi.xfyun.cn/v1/aiui";
APPID = "5e017c12";
APIKEY = "b1c9db5797d7bd16567bb2e6a34cf075"
END_FLAG = "--end--"
param = "{\"result_level\":\"plain\",\"auth_id\":\"894c985bf8b1111c6728db79d3479aef\",\"data_type\":\"audio\",\"aue\":\"raw\",\"scene\":\"main_box\",\"sample_rate\":\"16000\"}";

audio_file_path="/data1/audio_file/wav/20人录音第一批交付-全品类/G00001/001M35_F01_80_0001.wav"

def on_message(ws, message):
   print ('Message>>>>>>>>>>>>>>>>>>>>>>>>')
   print(message)
   if 'iat' in message:
       mJson = json.loads(message)
       resultid = mJson['data']['result_id']
       if resultid == 1:
          print(message)
   print ('Message<<<<<<<<<<<<<<<<<<<<<<<<')

def on_error(ws, error):
    print ('error>>>>>>>>>>>>>>>>>>>>>>')
    print (error)
    print ('error<<<<<<<<<<<<<<<<<<<<<<')

def on_close(ws):
    print ("### closed ###")

def on_open(ws):
    def run(*args):
        step = 3000 #如果audioType是wav，此处需要修改为3200
        print(audio_file_path)
        with open(audio_file_path, 'rb') as f:
            while True:
                data = f.read(step)
                if data:
                    ws.send(data, ABNF.OPCODE_BINARY)
                if len(data) < step:
                    break
                time.sleep(0.1)

        ws.send(END_FLAG, ABNF.OPCODE_BINARY)
        time.sleep(0.6)
        ws.close()
    _thread.start_new_thread(run, ())

def getHandShakeParams():
    temp_data =base64.b64encode(bytes(param,'utf-8'))
    print(temp_data)
    paramBase64 = temp_data.decode(encoding='utf-8', errors='ignore')
    print(temp_data)
    curtime=str(time.time()).split(".")[0]
    print(curtime)
    signtype = "sha256";
    originStr = APIKEY + curtime + paramBase64;
    checksum =  sha256hex(originStr)
    handshakeParam = "?appid=" + APPID + "&checksum=" + checksum + "&curtime=" + curtime + "&param=" + paramBase64 + "&signtype=" + signtype;
    return handshakeParam

def sha256hex(data):
    sha256 = hashlib.sha256()
    sha256.update(data.encode())
    res = sha256.hexdigest()
    print("sha256加密结果:", res)
    return res

if __name__ == "__main__":
    url = BASE_URL + getHandShakeParams()
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(url,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()


