from data_control.gen_refcase import Genrefcase
import  os
# 生成excel格式的用例信息.
if __name__=="__main__":
    rootdir = "D:/MyData/ex_shenjf1/Desktop/云知声/a/"
    alist = os.listdir(rootdir)
    allcount = 0
    for item in alist:
        excel_path = rootdir + item
        print(excel_path)
        if excel_path.endswith(".xlsx"):
            excepath = "D:/MyData/ex_shenjf1/Desktop/云知声/a/"+item  # 用例文件保存的路
            item=item.replace(".xlsx","")
            if item == "90quiet-3m":
                tempitem = "90-3m-cmd-quiet"
            elif item == "90quiet-5m":
                tempitem = "90-5m-cmd-quiet"
            else:
                tempitem = item
            savepath="D:/MyData/ex_shenjf1/Desktop/云知声/txt文件/"+tempitem+".txt"
            service_dir="20190919/"+tempitem+"/"

            Genrefcase(excepath,savepath).write_txtfile(lastvalue=".out",s_dir=service_dir)