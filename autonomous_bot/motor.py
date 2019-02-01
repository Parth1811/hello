import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

pina=22
#a is the one which moves the right motor forward
pinb=6
#b is the one which moves the right motor backward
pinc=23
#c is the one which moves the left motor forward
pind=24
#d is the one which moves the left motor backward
l293d_pin=4

GPIO.setup(pina,GPIO.OUT)
GPIO.setup(pinb,GPIO.OUT)
GPIO.setup(pinc,GPIO.OUT)
GPIO.setup(pind,GPIO.OUT)

a=GPIO.PWM(pina,100)
a.start(0)

b=GPIO.PWM(pinb,100)
b.start(0)

c=GPIO.PWM(pinc,100)
c.start(0)

d=GPIO.PWM(pind,100)
d.start(0)



GPIO.setup(l293d_pin,GPIO.OUT) 
GPIO.output(l293d_pin, True)


max_motor_speed=100
default_motor_speed=max_motor_speed/2


def set_speed(motor_name, speed):
    GPIO.output(pina,False)
    GPIO.output(pinb,False)
    GPIO.output(pinc,False)
    GPIO.output(pind,False)
    
    
    
    if lower(motor_name[0])=='r':
        GPIO.output(pina,False)
        GPIO.output(pinb,False)

    
        if speed >0:
            GPIO.output(pina, True)
            a.ChangeDutyCycle(speed)
        if speed<0:
            GPIO.output(pinb, True)
            b.ChangeDutyCycle(speed)
                 
    if lower(motor_name[0])=='l':
        GPIO.output(pinc,False)
        GPIO.output(pind,False)
        if speed>0:
            GPIO.output(pinc, True)
            c.ChangeDutyCycle(speed)
        if speed<0:
            GPIO.output(pind, True)
            d.ChangeDutyCycle(speed)
    
    if lower(motor_name[0])=='b':
        GPIO.output(pina,False)
        GPIO.output(pinb,False)
        GPIO.output(pinc,False)
        GPIO.output(pind,False)
        
        if speed>0:
            GPIO.output(pinc, True)
            GPIO.output(pina, True)
            a.ChangeDutyCycle(speed)
            c.ChangeDutyCycle(speed)
        if speed<0:
            GPIO.output(pind, True)
            d.ChangeDutyCycle(speed)
            GPIO.output(pinb, True)
            b.ChangeDutyCycle(speed)
             
   