import smtplib,os
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart #发送带附件的邮件
from email import encoders

my_sender='1281198374@qq.com' #发件人邮箱账号
my_pass='vhmgggamjmtkhfhe'    #发件人邮箱密码,密码有可能过期，需要在qq查询密码
my_user='1281198374@qq.com'   #收件人为自己
def mail():
    ret=True
    try:
        #设置根属性
        msg=MIMEText('<html><h1>您好！</h1></html>','html','utf-8')
        msg['From']=formataddr(["goodsen",my_sender])#括号里的对应发件人邮箱昵称，发件人邮箱账号
        msg['To']=formataddr(["hadey",my_user])      #括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']="自动化测试"                  #邮件的主题,也可以说是标题


        #设置发件人邮件信息
        server=smtplib.SMTP_SSL("smtp.qq.com",465)  #发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender,my_pass)             #这是对应的发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[my_user,],msg.as_string())#括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()#关闭连接
        # 如果try中的语句没有执行，则会执行下面的ret=false
    except  Exception:
        ret=False
    return  ret
ret = mail()
if  ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")