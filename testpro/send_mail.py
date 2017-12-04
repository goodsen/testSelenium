import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart #发送带附件的邮件

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

        #邮件正文是MIMETest
       # msg.attach(MIMEText('本邮件为自动化测试','plain','utf-8'))

        #添加附件就是加上一个MIMEBase,从本地选取文件
        with open('E:\\image.png','rb') as f:
            #设置附件的MIME和文件名，这里是html
            mime = MIMEBase('image','png', filename = 'image.png')

        #加上必要的头信息:
        mime.add_header('accept','text/html,application/xhtml+xml,'
                        'application/xml;q=0.9,image/webp,'
                        'image/apng,*/*;q=0.8')
        mime.add_header('user-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                     'AppleWebKit/537.36 (KHTML, like Gecko)'
                                     ' Chrome/62.0.3202.94 Safari/537.36')
        #把附件的内容读进来
        mime.set_payload(f.read())
        #添加到MIMEMultipaty
        msg.attach(mime)

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