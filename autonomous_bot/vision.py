#import qr_scanner

import us
from time import sleep
import motor
import color_detector
import ir

#define zbarcam
def zbarcam():
    os.system('sudo service motion stop')
    os.system('zbarcam /dev/video0 > qr_result.txt')
    

def check_for_block():
    if color_detector.color()!=white :
        return True

def check_function():
    qr_read=open('qr_result.txt','r')
    s=qr_read.read()
    qr_read.close()

    if not s=='':
        return True
    else:
        return False

#this is so wrong rajat fu
def scan_qr():
    ideal_qr_us_dist=19.5
    last_error=0
    timer=0.1

    #Thread( target=qr_scanner.scan)
    sleep(1.5)

    if check_function():
        return True
    while True:
        error=ideal_qr_us_dist-us.dist(qr_trig,qr_echo)
        diff_error=(error-last_error)/feedback_loop.delay
        last_error=error
         
        Kp=0.5
        Kd=0.25
        P=Kp*error
        D=Kd*diff_error
        pid_value=P+D

        if check_function:
            return True

        if us.dist(us.qr_trig,us.qr_echo)<ideal_qr_us_dist:
            motor.set_speed('b',-40-pid_value)
            sleep(0.25)
            motor.set_speed('b',0)             
            if check_function():
                return True
        
        else:
            motor.set_speed('r',-50)
            sleep(timer)
            motor.set_speed('r',50)
            sleep(0.5)
            if check_function():
                return True
            motor.set_speed('l',-50)
            sleep(timer)
            sleep(0.5)
            if check_function():
                return True
            motor.sleep('l',50)
            sleep(timer)
            sleep(0.5)
            if check_function():
                return True
            motor.set_speed('b',0)

        timer+=0.05
    motor.set_speed('b',0)
    return True
        

        

def ground_is_white():
    if ir.loop()=="black":
        return False
    else:
        return True

    