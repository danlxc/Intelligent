#! /usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
from smtplib import SMTP_SSL
# from email.MIMEText import MIMEText
# from email.MIMEMultipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

mail_host = "smtp.exmail.qq.com"
mail_user = "itservice@5irich.com"
mail_pass = "Ops@5i.com"


def send_mail(users, sub, content, *filenames):
    os.	popen("echo %s >>/tmp/ts.log" % users)
    address = 'itservice@5irich.com'
    msg = MIMEMultipart()
    msg['Subject'] = sub
    msg['From'] = address
    msg['To'] = users
    msg.attach(MIMEText(content, 'plain', 'utf-8'))

    if filenames:
        for filename in filenames:
            # 构造附件，传送当前目录下的 filename 文件
            attach = MIMEText(open(filename, 'rb').read(), 'base64', 'utf-8')
            attach["Content-Type"] = 'application/octet-stream'
            # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
            attach[
                "Content-Disposition"] = 'attachment; filename="%s"' % (filename)
            msg.attach(attach)

    try:
        s = SMTP_SSL(mail_host)
        # 测试使用的debug模式
        # s.set_debuglevel(1)
        s.ehlo(mail_host)
        s.login(mail_user, mail_pass)
        for user in users.split(','):
            s.sendmail(address, user, msg.as_string())
        s.close()
        return True
    except Exception as e:
        print(e)
        return False


if __name__ == '__main__':
    if len(sys.argv) > 4:
        send_mail(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        send_mail(sys.argv[1], sys.argv[2], sys.argv[3])
    # send_mail('liuquan@5irich.com', "sys.argv[2]", "sys.argv[3]", "test.txt", "tet.txt")
