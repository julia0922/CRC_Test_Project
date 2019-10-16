# 计算每个sheet总的识别率
from common.operation_excel import OperationExcel
if __name__=="__main__":
    # 计算识别率
    excelpath="E:/asr测试结果/9月20日交付空调项目数据-测试结果/2019-09-27/思必驰asr识别率.xlsx"
    ratepath="E:/asr测试结果/9月20日交付空调项目数据-测试结果/2019-09-27/思必驰asr识别率rate.xlsx"
    dictinfo=OperationExcel(excelpath).getsuccessrate()
    OperationExcel(ratepath).write_ratetoexcel_bydict(dictinfo)