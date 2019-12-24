import smtplib
from email.mime.text import MIMEText
"""
 mail용 클래스
 자신의 id, pw를 이용하여 메일 사용
"""


class MyMail:
    def __init__(self):
        return

    # gmail을 통하여 메일 쓰기
    def send_gmail(self, id: str, pw: str, to_addr: str, title: str, msg: str):
        mail_sever = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        mail_sever.login(id, pw)
        my_addr: str = id + "@gmail.com"
        msg = MIMEText(msg)
        msg['Subject'] = title
        msg['from'] = my_addr
        msg['to'] = to_addr
        mail_sever.sendmail(my_addr, to_addr, msg.as_string())
        mail_sever.quit()
