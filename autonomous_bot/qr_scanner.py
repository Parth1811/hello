import os
from threading import Thread

def zbarcam():
    os.system('sudo service motion stop')
    os.system('zbarcam /dev/video0 > qr_result.txt')
    
def loop():
    while True:
        qr_read=open('qr_result.txt','w')
        s=qr_read.read()
        if s!='':
            os.system('sudo pkill zbarcam')
            print s
            break
        qr_read.close()
        

def scan():
    qr_write=open('qr_result.txt','w')
    qr_write.write('')
    thread1=Thread(target=zbarcam)
    thread1.start()
    time.sleep(0.5)
    loop()
    