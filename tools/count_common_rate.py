# 计算命令词的识别率
from common.operation_excel import OperationExcel
if __name__=="__main__":
    excelpath = "E:/asr测试结果/9月20日交付空调项目数据-测试结果/2019-09-27/思必驰asr识别率.xlsx"
    rate_excelpath = "E:/asr测试结果/9月20日交付空调项目数据-测试结果/2019-09-27/命令词思必驰asr识别率.xlsx"
    valueinfo=OperationExcel(excelpath).get_common_rate()
    OperationExcel(rate_excelpath).write_ratetoexcel_bydict(valueinfo)
