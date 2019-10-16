import  os

class Transfileobj(object):
    def __init__(self,sourcepath,transpath,transtype):
        self.s_path=sourcepath
        self.taget_path=transpath
        self.tran_stype=transtype

    def run_trans(self):
        if os.path.exists(self.s_path)==False:
            print("转换的源标路径为空:"+self.s_path)

        if os.path.exists(self.taget_path)==False:
            print("转换的目标路径为空:"+self.taget_path)

        if os.path.isfile(self.s_path):
            new_filepath=self.taget_path+os.path.basename(self.s_path)
            self.run_common(self.s_path,new_filepath)
        else:
            self.cycledir_transfer(self.s_path)

    def cycledir_transfer(self,filedir):
       dirlist= os.listdir(filedir)
       for item in dirlist:
           temppath=filedir+item
           newroot_dir = self.taget_path + str(temppath).replace(self.s_path,"")
           print(temppath,newroot_dir)
           if os.path.isfile(temppath) and item.endswith(".wav"):
               new_filepath=newroot_dir
               if self.tran_stype=="pcm":
                   new_filepath=new_filepath.replace(".wav",".pcm")
               print("newfilepath",new_filepath)
               self.run_common(temppath, new_filepath)
           elif os.path.isdir(temppath):
               if os.path.exists(newroot_dir)==False:
                   os.makedirs(newroot_dir)
               self.cycledir_transfer(temppath+"/")


    def run_common(self,file_path,new_filepath):
        if self.tran_stype=="pcm":
            commonline = "sox -t wav " + file_path + " -t raw -r 16000 -c 1 -b 16 " + new_filepath + ""
            os.system(commonline)
        else:
            commonline = "sox " + file_path + " -r 16000 -c 1 -b 16 " + new_filepath + ""
            os.system(commonline)
