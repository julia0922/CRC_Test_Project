import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "605007202@qq.com"  # 用户名
mail_pass = "hskvrjzemdjwbaib"  # 口令

sender = '605007202@qq.com'
receivers = ['ex_shenjf1@partner.midea.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From']=formataddr(["xiaoming",sender])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
message['To']=formataddr(["xiaohong",';'.join(receivers)])   #括号里的对应收件人邮箱昵称、收件人邮箱账号

#message['From'] = Header("菜鸟教程", 'utf-8')
#message['To'] = Header("测试", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP_SSL()
    code,messageinfo=smtpObj.connect(mail_host, 465)  # 25 为 SMTP 端口号
    print(code,messageinfo)
    smtpObj.login(mail_user, mail_pass)
    a=smtpObj.sendmail(sender, receivers, message.as_string())
    print(a)
    print("邮件发送成功")
except smtplib.SMTPConnectError as e:
    print("Error: 无法发送邮件",e.message)