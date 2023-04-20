from time import time, localtime
class Clock:
    @staticmethod
    def Say_time():
        time()
        rez = localtime()
        print(f"{rez.tm_hour} : {rez.tm_min} : {rez.tm_sec}")
Clock.Say_time()