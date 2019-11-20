
from data_control.gen_manualcase import Genmanualcase

# 生成excel格式的用例信息.
if __name__=="__main__":
    #saveExcel = "E:/audiofile/testin云测8月30号递交数据/source/aa.xlsx"  # 用例文件保存的路径
    #audiofiledirdict={"E:/audiofile/testin云测8月30号递交数据/source/":"王娇-空调"}

    #saveExcel = "E:/audiofile/原音频/9月20日交付空调项目数据/9月20日交付空调项目数据.xlsx"  # 用例文件保存的路径
    #audiofiledirdict={"E:/audiofile/原音频/9月20日交付空调项目数据/":"9月20日交付空调项目数据"}

    saveExcel = "D:/aicolud_file/外部音频/Magicdata_20180127/"  # 用例文件保存的路径
    audiofiledirdict={"D:/aicolud_file/外部音频/Magicdata_20180127/Magicdata_20180127/014/wav/":"014",
                      "D:/aicolud_file/外部音频/Magicdata_20180127/Magicdata_20180127/205/wav/": "205",
                      "D:/aicolud_file/外部音频/Magicdata_20180127/Magicdata_20180127/206/wav/": "206",
                      "D:/aicolud_file/外部音频/Magicdata_20180127/Magicdata_20180127/207/wav/": "207",
                      "D:/aicolud_file/外部音频/Magicdata_20180127/Magicdata_20180127/208/wav/":"208",
                      "D:/aicolud_file/外部音频/Magicdata_20180127/Magicdata_20180127/201/wav/": "201",
                      "D:/aicolud_file/外部音频/Magicdata_20180127/Magicdata_20180127/202/wav/": "202",
                      "D:/aicolud_file/外部音频/Magicdata_20180127/Magicdata_20180127/203/wav/": "203",
                      "D:/aicolud_file/外部音频/Magicdata_20180127/Magicdata_20180127/209/wav/": "209",
                      "D:/aicolud_file/外部音频/Magicdata_20180127/Magicdata_20180127/210/wav/": "210"}

    #audiofiledirdict = {"E:/Add_CMD/cmd_01_0125/45r1-5m/": "cmd_01_0125_45r1-5m"}
    gentype = 7# 空调
    Genmanualcase(saveExcel, audiofiledirdict, gentype).gen_excelcase()



