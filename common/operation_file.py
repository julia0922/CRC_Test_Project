import os
import shutil

class OperationFile(object):
    def getchild_dirlist(self,rootdir,dirlist=None):
        if dirlist==None:
            dirlist=[]


        isExistWavFile=False
        list = os.listdir(rootdir)
        for dirname in list:
            path = rootdir + dirname
            if os.path.isdir(path):
                self.getchild_dirlist(path + "/", dirlist)
            else:
                if str(dirname).endswith(".wav"):
                    isExistWavFile=True

        if isExistWavFile and rootdir not in dirlist:
           dirlist.append(rootdir)

        return dirlist

    # 循环获取目录下的文件列表,并返回列表信息
    def getfilelistbydir(self,rootdir,filelist=None):
        if filelist==None:
            filelist=[]

        list = os.listdir(rootdir)
        print(list)
        for dirname in list:
            path = rootdir + dirname
            print(path)
            if os.path.isdir(path):
                self.getchild(path + "/",filelist)
            else:
                if str(dirname).endswith(".wav"):
                    filelist.append(dirname)

        return filelist


    def getfile_dictbydir(self,rootdir,filedict=None):
        if filedict==None:
            filedict={}

        list = os.listdir(rootdir)
        print(list)
        for dirname in list:
            path = rootdir + dirname
            print(path)
            if os.path.isdir(path):
                self.getfile_dictbydir(path + "/",filedict)
            else:
                if str(dirname).endswith(".wav"):
                    if dirname not in filedict:
                        filedict[dirname]=path

        return filedict

    # 拷贝列表中的文件到指定目录。
    def copy_file_todir(self,c_list,sourcedir="",targetdir=""):
        if sourcedir=="":
            print("指定的原拷贝目录为空")
            return  False

        if targetdir =="":
            print("指定的目标目录为空")
            return False

        if targetdir != "" and os.path.exists(targetdir) == False:
            os.makedirs(targetdir)

        try:
            for item in c_list:
                s_path=sourcedir+"/"+item
                taget_path=targetdir+item
                print(taget_path)
                self.start_copy_file(s_path,taget_path)
            return True

        except:
            print("拷贝文件异常")
            return  False

    # 拷贝某一个文件
    def start_copy_file(self,s_path,taget_path):
         if os.path.exists(s_path) == True:
             root_dirpath = os.path.dirname(taget_path)
             print(root_dirpath)
             if os.path.exists(root_dirpath)==False:
                 os.makedirs(root_dirpath)
             shutil.copyfile(s_path, taget_path)

    def write_fileinfo(self):

        pass


if __name__=="__main__":
    dirname = os.path.dirname("D:\\aa\\1.txt")
    print(dirname)

