
from data_control.gen_manualcase import Genmanualcase

# 生成excel格式的用例信息.
if __name__=="__main__":
    saveExcel = "E:/"  # 用例文件保存的路径
    audiofiledirdict = {"E:/audiofile/testin云测8月30号递交数据/source/": "空调830",
                        "E:/audiofile/第一批数据17人的交付-空调相关录音/testin云测录音交付_source/": "空调17",
                        "E:/audiofile/testin云测8月30号递交数据/source/023王娇/": "023王娇"}
    gentype = 1  # 空调
    Genmanualcase(saveExcel, audiofiledirdict, gentype).gen_excelcase()



