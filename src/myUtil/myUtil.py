import time
import os


class MyUtil:
    def __init__(self):
        return

    # sleep 함수
    @staticmethod
    def sleep_sec(sec: int):
        time.sleep(sec)

    # 현재 날짜 반환
    @staticmethod
    def get_date():
        now = time.localtime()
        s = "%04d-%02d-%02d" % (now.tm_year, now.tm_mon, now.tm_mday)
        return s

    # 현재 시간 반환
    @staticmethod
    def get_time():
        now = time.localtime()
        s = "%02d:%02d:%02d" % (now.tm_hour, now.tm_min, now.tm_sec)
        return s

    # 디렉토리 생성
    @staticmethod
    def create_dir(path: str):
        if not (os.path.isdir(path)):
            os.makedirs(path)

    # 작업디렉토리 반환(실행경로와 비슷)
    @staticmethod
    def get_work_dir():
        return os.getcwd()
