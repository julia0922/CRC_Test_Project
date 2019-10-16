
from common.operation_excel import OperationExcel
from common.operation_file import OperationFile
import os
class Genrefcase(object):
    def __init__(self,excelpath=None,refpath=None):
        self.ex_path=excelpath;
        self.ref_path=refpath

    def write_ref(self):
       ofobject=OperationFile()
       obj,names= OperationExcel(self.ex_path).get_all_sheetnames()
       for item in names:
           ws_sheet=obj.get_sheet_by_name(item)
           filepath=self.ref_path+"/"+item+".ref"
           for r in range(3,ws_sheet.max_row+1):
               audiovalue=ws_sheet.cell(r,1).value
               exceptvalue =str(ws_sheet.cell(r, 2).value)
               exceptvalue=exceptvalue.replace("三十分钟","30分钟").replace("六十分钟","60分钟").replace("四十五分钟","45分钟").replace("四碗","4碗").replace("五碗","5碗")\
                   .replace("两碗","2碗").replace("九十分钟","90分钟")

               print(exceptvalue)
               lines=audiovalue+" "+exceptvalue+"\n"
               ofobject.write_fileinfo(filepath,lines)


    def gen_configfile(self,configsavepath,refpath,ser_audiorootpath,ser_refpath):
        ofobject=OperationFile()
        list=ofobject.getfilelistbydir(refpath,suffix=".ref")
        testsetlines=""
        pathlines=""
        for item in list:
            if str(item).endswith(".ref"):
                temp_item=str(item).replace(".ref","")
                lines="test"+temp_item+"= modelType=general,home_md|audioFormat=pcm16k|voiceField=md|id_1028=8" +"\n"
                testsetlines=testsetlines+lines

                plines = "test" + temp_item + "="+ser_audiorootpath+temp_item+"/|./"+ser_refpath+"/"+item + "\n"
                pathlines=pathlines+plines

        ofobject.write_fileinfo(configsavepath,testsetlines)

        ofobject.write_fileinfo(configsavepath, pathlines)






