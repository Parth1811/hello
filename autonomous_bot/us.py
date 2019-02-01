#Libraries
import RPi.GPIO as GPIO
import time
 
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins
right_trig=16
left_trig=20
front_trig=21#red tape
qr_trig=8

right_echo=10
left_echo=9
front_echo=11
qr_echo=7


Trigger_pins=[right_trig,left_trig,front_trig,qr_trig]
Echo_pins=[right_echo,left_echo,front_echo,qr_echo]
 
#set GPIO direction (IN / OUT)
for trig_pin in Trigger_pins:
    GPIO.setup(t_pin, GPIO.OUT)
for echo_pin in Echo_pins:   
    GPIO.setup(e_pin, GPIO.IN)
 
def dist(GPIO_TRIGGER,GPIO_ECHO):
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER ,True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER ,False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
 
if __name__ == '__main__':
    try:
        while True:
            dist = dist(right_trig,right_echo)
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()