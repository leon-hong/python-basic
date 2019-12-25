from src.myUtil.myUtil import MyUtil
from src.myUtil.myMail import MyMail

print("hello world")

mail = MyMail()


for i in range(0, 5):
    mail.send_gmail('dev.leonhong', '!8189809goD', 'leonhong@naver.com', 'hello', 'hello naver!')
    MyUtil.sleep_sec(30)
    print("mail send.")
