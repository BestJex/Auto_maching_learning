import smtplib
from email.mime.text import MIMEText
from email.header import Header
import random
import time

# 用于构建邮件头

# 发信方的信息：发信邮箱，QQ 邮箱授权码
password = ''
# 收信方邮箱
to_addr = ''
def send_email(password, to_addr):
    '''
    :param password: Email authorization code
    :param to_addr: recevier email address
    :return:{
        to_addr:收件人邮箱地址
        time:发送成功后的时间戳
    }
    '''
    from_addr = 'yikechengxushu@qq.com'
    smtp_server = 'smtp.qq.com'
    # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
    validate_num=random.randint(100000,999999)
    msg = MIMEText("你的验证码(注意，验证码仅5分钟内有效)：{}".format(validate_num), 'plain', 'utf-8')
    # 邮件头信息
    msg['From'] = Header(from_addr)
    msg['To'] = Header(to_addr)
    msg['Subject'] = Header('随机验证码')

    # 开启发信服务，这里使用的是加密传输
    server = smtplib.SMTP_SSL()
    server.connect(smtp_server, 465)
    # 登录发信邮箱
    server.login(from_addr, password)
    # 发送邮件
    server.sendmail(from_addr, to_addr, msg.as_string())
    # 关闭服务器
    server.quit()
    return {
                to_addr:validate_num,
                'send_time':time.time()
            }

password='htvviggqfrwobbfc'
print(send_email(password,to_addr))
