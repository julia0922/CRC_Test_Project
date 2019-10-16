import  os

class Operationpath(object):
    def getfilenamebynumber(self,filepath,part):
        basename = os.path.basename(filepath)
        split_value = basename.split("_")
        # 例如：003M29_01_04_0031.wav  part=1表示取04值，part=2表示取04_0031

        middle_value = ""
        if part==1:
            middle_value = str(split_value[2])
        else:
            middle_value = str(split_value[2]) + "_" + str(split_value[3])
            middle_value = middle_value.replace(".wav", "")

        return middle_value