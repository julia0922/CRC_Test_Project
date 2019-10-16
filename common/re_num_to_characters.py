import re

# 替换数字为汉字
class ReplaceNumCharacters(object):
    def __init__(self):
        self.number_dict = {"0": "零", "1": "一", "2": "二", "3": "三", "4": "四", "5": "五", "6": "六", "7": "七","8": "八", "9": "九", "10": "十",
                "11": "十一", "12": "十二", "13": "十三", "14": "十四", "15": "十五","16": "十六", "17": "十七", "18": "十八", "19": "十九",
                "20": "二十", "21": "二十一", "22": "二十二", "23": "二十三","24": "二十四", "25": "二十五", "26": "二十六", "27": "二十七", "28": "二十八", "29": "二十九",
                "30": "三十", "31": "三十一", "32": "三十二", "33": "三十三", "34": "三十四", "35": "三十五", "36": "三十六", "37": "三十七","38": "三十八", "39": "三十九",
                "40": "四十", "41": "四十一", "42": "四十二", "43": "四十三", "44": "四十四", "45": "四十五","46": "四十六","47": "四十七", "48": "四十八", "49": "四十九",
                "50": "五十", "51": "五十一", "52": "五十二", "53": "五十三", "54": "五十四", "55": "五十五", "56": "五十六","57": "五十七", "58": "五十八", "59": "五十九",
                "60": "六十", "61": "六十一", "62": "六十二", "63": "六十三", "64": "六十四", "65": "六十五", "66": "六十六","67": "六十七", "68": "六十八", "69": "六十九",
                "70": "七十", "71": "七十一", "72": "七十二", "73": "七十三", "74": "七十四", "75": "七十五", "76": "七十六","77": "七十七", "78": "七十八", "79": "七十九",
                "80": "八十", "81": "八十一", "82": "八十二", "83": "八十三", "84": "八十四", "85": "八十五", "86": "八十六", "87": "八十七", "88": "八十八", "89": "八十九",
                "90": "九十", "91": "九十一", "92": "九十二", "93": "九十三", "94": "九十四", "95": "九十五", "96": "九十六","97": "九十七", "98": "九十八", "99": "九十九",
                "100": "一百"
                }

    def is_existkey(self, key_value):
        tempvalue = ""
        if key_value in self.number_dict:
            tempvalue = self.number_dict[key_value]
        else:
            tempvalue = key_value

        return tempvalue

    def is_contain_dot(self,key_value):
        itemvalue=""
        if key_value.find(".") != -1:
            value_list = key_value.split(".")
            first_value = value_list[0]
            last_value = value_list[1]
            last_temp_value=""
            for i in last_value:
                last_temp_value += self.is_existkey(i)
            itemvalue = self.is_existkey(first_value) + "点" + last_temp_value
        return itemvalue

    def is_contain_negative(self,key_value):
        replaceValue = ""
        if key_value.find("-") != -1:
            r_value = key_value.replace("-", "")
            # 判断是否包含点号
            if r_value.find(".") != -1:
                replaceValue = self.is_contain_dot(r_value)
                print(replaceValue)
            elif len(r_value) == 3:
                replaceValue=self.is_three_len(r_value)
            else:
                replaceValue = self.is_existkey(r_value)

        if replaceValue != "":
            replaceValue = "零下" + replaceValue

        return replaceValue


    def is_three_len(self,key_value):
        if len(key_value) == 3:
                first_value = key_value[0]
                last_value = key_value[1:]
                print("lastvalue:",last_value)
                if str(last_value)=="00":
                    replaceValue = self.is_existkey(first_value) + "百"
                    print("dddddddddddddddddddd",replaceValue)
                elif str(last_value[0])=="0":
                    replaceValue= self.is_existkey(first_value) + "百零"+ self.is_existkey(last_value[1])
                elif str(last_value)=="10":
                    replaceValue = self.is_existkey(first_value) + "百一十"
                elif str(last_value[0])=="1":
                    replaceValue = self.is_existkey(first_value) + "百一十"+ self.is_existkey(last_value[1])
                else:
                    replaceValue = self.is_existkey(first_value) + "百" + self.is_existkey(last_value)

        return replaceValue

    def is_contain_percent_sign(self,key_value):
        replaceValue=""
        if  key_value.find("%") != -1:
           r_value = key_value.replace("%", "")
           # 判断是否包含点号
           if r_value.find(".") !=-1:
               replaceValue = self.is_contain_dot(r_value)
               print(replaceValue)
           elif len(r_value)==3:
               replaceValue=self.is_three_len(r_value)
           else:
               replaceValue = self.is_existkey(r_value)

        if replaceValue!="":
           replaceValue="百分之"+replaceValue

        return replaceValue


    def replace_num_value(self,info):
        value = str(info)
        if value == None or value == "":
            return value
        #num_list = re.findall('\d+\.?\%?\d*', value)
        num_list = re.findall('\-?\d*\.?\d+\%?', value)
        print(num_list)
        for i in num_list:
            key_value= str(i)
            print(key_value)
            if key_value.find("%") !=-1:
                replaceValue = self.is_contain_percent_sign(key_value)
            elif key_value.find("-")!=-1:
                replaceValue=self.is_contain_negative(key_value)
            elif key_value.find(".") !=-1:
                replaceValue=self.is_contain_dot(key_value)
            elif len(key_value)==3:
                 replaceValue=self.is_three_len(key_value)
            else:
                replaceValue = self.is_existkey(key_value)
                print(replaceValue)

            value = value.replace(key_value, replaceValue)
            print(value)
        return value



if __name__=="__main__":
    #key_value="120"
    #print(key_value[0])
    #print(key_value[1:])
    #value="-20度99.36%风速0.5调低80还有200度5,-9999,-99.63,235"
    #num_list = re.findall('\-?\d*\.?\d+\%?', value)
    #print(num_list)
    value=ReplaceNumCharacters().replace_num_value("微蒸烤一体机上下烧烤加热风240度1小时")
    print(value)
