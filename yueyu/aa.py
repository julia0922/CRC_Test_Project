import multiprocessing
import  pandas as pd

def worker(d):
    global return_data
    return_data = d

    valueinfo = return_data["039M23_F01_41_0491.wav"]
    valueinfo['asr'] = "dddddd"
    valueinfo['result'] = "False"
    return_data["039M23_F01_41_0491.wav"] = valueinfo

    # print(return_data)
    print("**************************")
    print(return_data)

if __name__ == "__main__":
    manager = multiprocessing.Manager()
    d = manager.dict()
    hashvalue={}
    hashvalue["expect"]="调高一度"
    hashvalue["asr"] = ""
    hashvalue["result"] = ""

    d["039M23_F01_41_0491.wav"]=hashvalue
    processlist=[]
    for i in range(0,1):
        p = multiprocessing.Process(target=worker, args=(d,))
        p.start()
        processlist.append(p)

    for i in processlist:
        i.join()
    print(d)
