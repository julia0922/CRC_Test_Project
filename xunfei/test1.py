

'''
def read_fileinfo(filepath):
    list=[]
    with open(filepath, 'r', encoding="utf-8") as f:
        for line in f:
            firstvalue = line.split(" ")[0]
            print(firstvalue)
            if firstvalue != "wav":
                list.append(firstvalue)
    return list
'''

import multiprocessing
def func(num):
    num.value = num.value+1 # 子进程改变数值的值，主进程跟着改变
    print(num.value)


if __name__=="__main__":
    '''
    filpath="E:/project/Test_project/wer_20人录音第一批交付-全品类_G00001.txt"
    alllines=read_fileinfo(filpath)
    print(alllines)
    if "001M35_F01_80_0003.wav" in alllines:
        print("ddddddddddddddddddd")
    '''

    num = multiprocessing.Value("d", 10.0)  # d表示数值,主进程与子进程共享这个value。（主进程与子进程都是用的同一个value）
    print(num.value)

    plist=[]
    for i in range(0,5):
        p = multiprocessing.Process(target=func, args=(num,))
        p.start()
        plist.append(p)

    for j in plist:
        p.join()

    #print(num.value)

