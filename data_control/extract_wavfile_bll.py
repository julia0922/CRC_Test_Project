from common.operation_file import OperationFile
from common.operation_path import Operationpath


class Extractwavfile():
      def __init__(self,audiodir,savepath,ex_typelist,expart):
          self.audio_sourepath=audiodir
          self.extrac_savepath=savepath
          self.extrac_type=ex_typelist
          self.extrac_part=expart

      def extract(self):
          ofobject=OperationFile()
          list=ofobject.getfile_dictbydir(self.audio_sourepath)  #获取目录下的文件信息,返回dict格式。
          opobject= Operationpath()
          for item in list.keys():
              middlevalue=opobject.getfilenamebynumber(item,self.extrac_part)
              if middlevalue in self.extrac_type:
                  path=list[item]
                  tagetpath=self.extrac_savepath+item
                  ofobject.start_copy_file(path,tagetpath)







