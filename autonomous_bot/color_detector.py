import RPi.GPIO as GPIO
import time



s2 = 13
s3 = 19
signal = 26
NUM_CYCLES = 10


GPIO.setmode(GPIO.BCM)
GPIO.setup(signal,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(s2,GPIO.OUT)
GPIO.setup(s3,GPIO.OUT)
  
color=[white,white,white,white]
def color():
    for i in range(4):
        GPIO.output(s2,GPIO.LOW)
        GPIO.output(s3,GPIO.LOW)
        time.sleep(0.3)
        start = time.time()
        
        for impulse_count in range(NUM_CYCLES):
            GPIO.wait_for_edge(signal, GPIO.FALLING)
        duration = time.time() - start 
        red  = NUM_CYCLES / duration   
   
        GPIO.output(s2,GPIO.LOW)
        GPIO.output(s3,GPIO.HIGH)
        time.sleep(0.3)
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
            GPIO.wait_for_edge(signal, GPIO.FALLING)
        duration = time.time() - start
        blue = NUM_CYCLES / duration
    

        GPIO.output(s2,GPIO.HIGH)
        GPIO.output(s3,GPIO.HIGH)
        time.sleep(0.3)
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
            GPIO.wait_for_edge(signal, GPIO.FALLING)
        duration = time.time() - start
        green = NUM_CYCLES / duration
   
    
        
        if green<7000 and blue<7000 and red>12000:
            color[i]=red
        elif red<12000 and  blue<12000 and green>12000:
            color[i]=green
        elif green<7000 and red<7000 and blue>12000:
            color[i]=blue
        elif red>10000 and green>10000 and blue>10000 and temp==1:
            print("place the object.....")
        
    a=(color[1]==color[2])+(color[1]==color[3])
    b=(color[1]==color[2])+(color[2]==color[3])
    c=(color[3]==color[2])+(color[1]==color[3])
    
    if a==2:
        return color[1]
    elif b==2:
        return color[2]
    elif c==2 :
        return color[3]
    else:
        return white
    

         
print(color())
      
    