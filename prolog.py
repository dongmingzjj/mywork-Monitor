import logging
import os
import time
from process import plist

def log():
    print("get data")
    d = time.strftime(r"%Y-%m-%d",time.localtime(time.time()))
    print("file read or create")
    f = open(f"logs/log{d}.txt","w")
    f.close()
    logging.basicConfig(filename=f'logs/log{d}.txt',
                     format = '%(asctime)s--%(message)s',
                     level=logging.DEBUG)
    print("process monitor is running")
    last = plist()
    while True:
        now = plist()
        if a:=(now-last):
            p = list(a)
            logging.info(",".join(p)+" start")
        if b:=(last-now):
            p = list(b)
            logging.info(",".join(p)+" end")
        last=now

    


def exam():
    logpath = "logs"
    if not os.path.exists(logpath):
        print("directory not exits,create now")
        os.mkdir(logpath)

if __name__=="__main__":
    exam()
    log()
