#!/usr/bin/env python
#coding=utf-8

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders

class mail(object):
    MAIL_SERVER = {
                    'server_smtp' : 'smtp.mimvp.com',
                    'from' : 'yang@mimvp.com',
                    'to' : ['1058012452@qq.com','johnny.yan@sodexo.com'],
                    'user_name' : 'yang@mimvp.com',
                    'user_pass' : '123456'
    }

    @classmethod
    def send_mail(cls,  subject='', body='', attaches=[]):
        mail_server = mail.MAIL_SERVER.get('server_smtp')
        mail_from = mail.MAIL_SERVER.get('from')
        mail_to = mail.MAIL_SERVER.get('to')
        mail_to_string = ';'.join(mail.MAIL_SERVER.get('to'))
        user_name = mail.MAIL_SERVER.get('user_name')
        user_pass = mail.MAIL_SERVER.get('user_pass')
        mail_body = body


        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = mail_from
        msg['to'] = mail_to_string
        msg['date'] = formatdate()
        msg.attach(MIMEText(mail_body))

        for attach in attaches:
            part = MIMEText('application', 'octet-stream')
            part.set_payload(open(attach, 'rb').read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="%s"'%os.path.basename(attach) )
            msg.attach(part)
        try:
            smtp = smtplib.SMTP(mail_server)
            smtp.login(user_name, user_pass)
            smtp.sendmail(mail_from, mail_to, msg.as_string())
            smtp.close()
            print "send email successful"
        except Exception as ex:
            print "send email error" + str(ex)

if __name__ == "__main__":

    attaches = []
    for i in range(5):
        i += 1
        filename = "file_" + str(i)
        f = open(filename, 'w+')
        f.write("i am ithomer.net " + str(i))
        f.close()
        attaches.append(filename)
    print attaches
    # files.append("getUrl.py")
    # files.append("getUrl.py")

    mail.send_mail('test python email', 'body of www.mimvp.com', attaches)





