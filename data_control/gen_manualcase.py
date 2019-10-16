
import  os
from common.operation_excel import OperationExcel
from common.operation_file import OperationFile
import  openpyxl

# 生成用例文件
class Genmanualcase(object):
    def __init__(self,savedir,audiofiledir,gentype):
        self.excel_savedir=savedir    # 生产的用例用例保存的路径
        self.audio_dirdict=audiofiledir    # 音频文件所在目录,类型为dict格式
        self.gen_type=gentype          # 映射文件类型，是空调的还是全品类的。1 表示空调，2 表示全品类.

    # 生成excel格式的用例文件
    def gen_excelcase(self):
        for current_rootdir in self.audio_dirdict:
            if os.path.exists(self.excel_savedir)==False:
                os.makedirs(self.excel_savedir)

            current_name = str(self.audio_dirdict[current_rootdir])   # 文件名称
            current_excelPath = self.excel_savedir + current_name + ".xlsx"  # excel 文件路径

            dirlist=OperationFile().getchild_dirlist(current_rootdir)
            print(dirlist)

            workbook = openpyxl.Workbook()
            for diritem in dirlist:
               oe_object=OperationExcel(current_excelPath)
               oe_object.write_excel(workbook, diritem, self.gen_type)  # 写入excel文件
               oe_object.remove_sheetbyname("Sheet")           # 删除Sheet

    # 生成ref格式的用例文件
    def gen_refcase(self):
        pass