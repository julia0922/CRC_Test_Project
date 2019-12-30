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
import openpyxl
from multiprocessing import Process,Manager
from xunfei.lockfile import FileLock

BASE_URL = "wss://wsapi.xfyun.cn/v1/aiui";
APPID = "5e017c12";
APIKEY = "b1c9db5797d7bd16567bb2e6a34cf075"
END_FLAG = "--end--"
param = "{\"result_level\":\"plain\",\"auth_id\":\"894c985bf8b1111c6728db79d3479aef\",\"data_type\":\"audio\",\"aue\":\"raw\",\"scene\":\"main_box\",\"sample_rate\":\"16000\"}";

FILE_PATH="E:/aaa/"
RUN_LIST={"全品类":{"20人录音第一批交付": "E:/audiofile/1/",
                 "20人录音第二批交付": "E:/audiofile/2/"}}
GEN_METHOD="全品类"
excel_path="E:/测试案例/20人录音第一批交付-全品类.xlsx"
THREAD_NUM=3

def write_fileinfo(filepath, lines):
    fileobj = FileLock(filepath)
    fileobj.acquire()
    with open(filepath, 'a+', encoding="utf-8") as f:
        f.writelines(lines)
        f.writelines("\n")
    fileobj.release()

def save(row):
    resultpath=FILE_PATH+"wer_"+sheetname+".txt"
    print("文件路径:",resultpath)
    all_lines = " ".join(str(i) for i in row)
    if os.path.exists(resultpath):
        write_fileinfo(resultpath,lines=all_lines)
    else:
        wavinfo= " ".join(str(i) for i in ["wav", "expect", "asr", "recognition result"])
        write_fileinfo(resultpath, lines=wavinfo)
        write_fileinfo(resultpath, lines=all_lines)

    '''
    if os.path.exists(resultpath):
        wb=openpyxl.load_workbook(FILE_PATH)
        if sheetname not in wb.get_sheet_names():
            ws=wb.create_sheet(sheetname)
            ws.append(["Recognition success rate"])
            ws.append(["wav","expect","asr","recognition result"])
        else:
            ws=wb[sheetname]
    else:
        wb=openpyxl.Workbook()
        ws=wb.create_sheet(sheetname)
        ws.append(["Recognition success rate"])
        ws.append(["wav", "expect", "asr", "recognition result"])
    ws.append(row)
    wb.save(FILE_PATH)
    '''

def on_message(ws, message):
   print ('Message>>>>>>>>>>>>>>>>>>>>>>>>')
   print(message)
   if 'iat' in message:
       mJson = json.loads(message)
       resultid = mJson['data']['result_id']
       if resultid == 1:
           result_txt= mJson['data']['text']
           basename=os.path.basename(audio_file_path)
           expectvalue=""
           result_value="FALSE"
           if basename in expectresultinfo:
               expectvalue=expectresultinfo[basename]
               if result_txt in expectvalue:
                   result_value="TRUE"
               else:
                   result_value = "FALSE"


           rows=[basename,expectvalue,result_txt,result_value]
           save(rows)
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


def get_small_list_tuple(all_case, thread_num):
    allcase_len = len(all_case)
    step_list = get_average_step_list(allcase_len, thread_num)
    print(step_list)
    out_list = []
    for i in range(thread_num):
        step = step_list[i]
        inner_list = all_case[:step]
        out_list.append(inner_list)
        for x in range(step_list[i]):
            del (all_case[0])
    return tuple(out_list)


def get_average_step_list(allcase_len, thread_num):
    if allcase_len <= 0 or 0 ==thread_num or allcase_len< thread_num:
        # return None
        raise Exception("[ERROR]: case_num: " + str(allcase_len) + " & thread_num: " + str(
            thread_num) + " should not < 0 and case_num must >= thread_num !!!")
    else:
        j = allcase_len / thread_num  # 除数,python除法不会四舍五入，52
        k = allcase_len % thread_num  # 余数要再被依次分配给n，直到分完,8
        step_list = []
        for i in range(allcase_len):
            # 先把除数分成n份，比如先分10分52
            step_list.append(int(j))
        if k > 0:  # 余数>0时, 除数再依次分配余数，直到分完
            for i in range(k):
                step_list[i] += 1
    return step_list

def gen_case(filelist,expect_resultlist,rootpath,key):
    global audio_file_path,expectresultinfo,sheetname
    expectresultinfo=expect_resultlist
    sheetname=key

    for one_file in filelist:
        if one_file not in expect_resultlist:
            print(one_file,"不存在")
            continue

        audio_file_path = rootpath + one_file
        print(audio_file_path)

        url = BASE_URL + getHandShakeParams()
        print(url)
        websocket.enableTrace(True)
        ws = websocket.WebSocketApp(url,
                                    on_message=on_message,
                                    on_error=on_error,
                                    on_close=on_close)
        ws.on_open = on_open
        ws.run_forever()


def start_run_websocket(genlist,dict_infovalue):
    for key in genlist:
        rootpath=genlist[key]
        print(rootpath)
        filelist = os.listdir(rootpath)
        small_list_tuple=get_small_list_tuple(filelist,THREAD_NUM)
        print(small_list_tuple)
        processlist = []
        for i in range(len(small_list_tuple)):
            p_one = Process(target=gen_case, args=(small_list_tuple[i],dict_infovalue,rootpath,key,))
            processlist.append(p_one)
            p_one.start()

        for i in processlist:
            i.join()

    # 计算识别率
    #marge_excel(FILE_PATH)

def marge_excel(save_manual_path):
    mywb = openpyxl.Workbook()
    new_sheet = mywb.create_sheet(index=0, title='sheet1')
    row1 = ["音频", "案例总数", "成功数", "失败数","识别率"]
    new_sheet.append(row1)
    count_rate_path=os.path.split(save_manual_path)[0]+os.path.basename(save_manual_path).replace(".xlsx","")+"_rate.xlsx"
    print("ddddddddddddd:",count_rate_path)
    data = openpyxl.load_workbook(save_manual_path)
    names = data.sheetnames
    for name in names:
        table = data.get_sheet_by_name(name)
        row2=[]
        row2.append(name)
        sum=0
        sucesscount=0
        failcount=0
        sucess_rate_value=0.0

        for row in range(3,table.max_row+1):
            result_value=str(table.cell(row, 4).value)
            sum=sum+1
            if result_value.lower()=="true" or result_value=="1":
                sucesscount=sucesscount+1
            else:
                failcount=failcount+1

        row2.append(sum)
        row2.append(sucesscount)
        row2.append(failcount)
        print(sum)
        print(sucesscount)
        print(failcount)
        if sum != 0:
            sucess_rate = (sucesscount / sum) * 100
            sucess_rate_value = "{:.2f}%".format(sucess_rate)
            row2.append(sucess_rate_value)
            table.cell(1,2).value=sucess_rate_value
        new_sheet.append(row2)
        data.save(save_manual_path)

    #mywb.save(count_rate_path)

def returndictinfobyexcel(excel_path):
    workbook = openpyxl.load_workbook(excel_path)
    allname = workbook.get_sheet_names()
    dictinfo={}
    for one_sheet in allname:
        table = workbook.get_sheet_by_name(one_sheet)
        # 获取总行数
        nrows = table.max_row + 1
        for i in range(3, nrows):
            wav_value = table.cell(i,1).value  # wav文件值
            result_value = table.cell(i, 2).value  # 预期结果值
            dictinfo[wav_value]=result_value

    return dictinfo

if __name__ == "__main__":
    # 读取excel文件，并存储到dict中.
    temp_resultinfo = returndictinfobyexcel(excel_path)
    print(temp_resultinfo)
    if GEN_METHOD=="all":
        pass
    else:
       genlist=RUN_LIST[GEN_METHOD]
       start_run_websocket(genlist,temp_resultinfo)



