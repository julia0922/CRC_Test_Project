class Commonservice(object):
    # 平均分配每个进程执行的条数
    def getavage(self,nrows,threadNum):
        step_list = []
        if nrows < threadNum:
            step_list = [nrows]
        else:
            j = nrows / threadNum  # 除数,python除法不会四舍五入，52
            q = nrows % threadNum
            # k = m % n  # 余数要再被依次分配给n，直到分完,8
            for i in range(threadNum):
                step_list.append(int(j))
            if q > 0:  # 余数>0时, 除数再依次分配余数，直到分完
                for i in range(q):
                    step_list[i] += 1

        return step_list

    def get_value(self,value):
        if value=="None":
            return ""

    def getdict_byexcelsheet(self,startindex,worksheetobj):
        import multiprocessing
        manager = multiprocessing.Manager()
        hash = manager.dict()
        list=[]
        r_index=0
        for i in range(startindex, worksheetobj.max_row + 1):
            wav_value = str(worksheetobj.cell(i, 1).value)
            expect_value=str(worksheetobj.cell(i, 2).value)  #expect_value 信息
            asr_value = str(worksheetobj.cell(i, 3).value)  # asr_value 信息
            result_value = str(worksheetobj.cell(i,4).value)  # result_value 信息
            if wav_value in hash:
                continue

            value_hash={}

            value_hash["expect"]=expect_value
            value_hash["asr"] = self.get_value(asr_value)
            value_hash["result"] =self.get_value(result_value)
            hash[wav_value]=value_hash

            temphash={}
            temphash[wav_value] = value_hash
            list.append(temphash)
            r_index=r_index+1

        return hash,list