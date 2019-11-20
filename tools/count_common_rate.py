# 计算命令词的识别率
from common.operation_excel import OperationExcel
if __name__=="__main__":
    excelpath = "E:/test_result/星空/2019-11-11/20人录音第一批交付-全品类.xlsx"
    rate_excelpath = "E:/test_result/星空/2019-11-11/命令词识别率-220人录音第一批交付-全品类.xlsx"
    valueinfo=OperationExcel(excelpath).get_common_rate()
    OperationExcel(rate_excelpath).write_ratetoexcel_bydict(valueinfo)
