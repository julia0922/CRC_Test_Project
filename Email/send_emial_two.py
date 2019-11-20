import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

# 第三方 SMTP 服务
mail_host = "smtp.midea.com"  # 设置服务器
mail_user = "ex_shenjf1@partner.midea.com"  # 用户名
mail_pass = "fang@1011"  # 口令

sender = 'ex_shenjf1@partner.midea.com'
receivers = ['605007202@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From']=formataddr(["申菊芳",sender])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
message['To']=formataddr(["julia",';'.join(receivers)])   #括号里的对应收件人邮箱昵称、收件人邮箱账号

subject = '在离线识别率测试结果'
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