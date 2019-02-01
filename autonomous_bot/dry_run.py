import vision
import motion
import time
import math
from threading import Thread
import us
import RPi.GPIO as GPIO
import wet_run
#define variables needed
#nodes=[]
number_of_boxes=0
number_of_qr=0
box_coordinates=[]
qr_coordinates=[]
GPIO.setwarnings(False)
time0=time.time()
end_coordinates=[]
start_coordinates=[0]
t=0

#call thread for forward
def thread_forward(path):
    fthread=Thread(target=motion.forward,args=[path])
    fthread.start()

#waits until block is cleared
def wait_for_path():

    while us.dist(us.front_trig,us.front_echo)<14  or check_for_qr():
        time.sleep(0.5)
        pass

    print('block removed')
    thread_forward()
    #so that it goes to the next cell
    time.sleep(1)


#method to check for qr on box with ultrasonic
def check_for_qr():
    if us.dist(us.qr_trig,us.qr_echo)<23:
        return True
    else: 
        return False


#check distance on particular direction

def check(direction):
    return_value=True
    if direction=='right':
        if us.dist(us.right_trig,us.right_echo)<15:
            return_value=False
    elif direction=='front':
        if us.dist(us.front_trig,us.front_echo)<15:
            return_value=False
    
    elif direction=='left':
        if us.dist(us.left_trig,us.left_echo)<20:
            return_value=False
    return return_value



#bot follows right wall follower algorithm to map the borders
def move(argument):

    global number_of_qr
    global number_of_boxes
    global box_coordinates
    global qr_coordinates
    global t
    global time0
    #global nodes
    

    #update variables required
    
   
    print('bot: (move called again) right wall dist=',
        us.dist(us.right_trig,us.right_echo))
    # if right is open, it will stop, turn right
    if check('right'):
       
        print('bot:right is open ')
        
        motion.stop()
        motion.turn('right')
    #move forward
    if callable(motion.forward):
        thread_forward('right')

    if not check('front'):
        #if front is blocked, it will check for boxes 
        motion.stop()
        if check_for_qr():
            number_of_qr+=1
            #if we are still in the first loop num will be <2
            if number_of_qr==1:
                #if we have not detected all boxes in the first loop
                #it will continue mapping 1st loop
                t+=time.time()-time0

                qr_coordinates.append(t)
                
                motion.turn('left')

                
                    
                time0=time.time()
            #if we have detected all boxes, move to next loop
            #we have finished mapping 1st loop
            elif number_of_qr==2:


                wait_for_path()


                time0=time.time()
            #second loop
            elif number_of_qr==3:
                t+=time.time()-time0
                qr_coordinates.append(t)
                wait_for_path()
                time0=time.time()
        

        elif vision.check_for_block():
            t+=time.time()-time0
            box_coordinates.append(t)
            wait_for_path()
            time0=time.time()
        #if nothing found it will turn left and check the ground
        else: 
            motion.turn('left')
            
            if vision.ground_is_white():
                t+=time.time()-time0
                if number_of_qr>=2:
                    end_coordinates.append(t)
                    #nodes.append('end')

                else:
                    start_coordinates.append(t)
                    #now we have to go to the qr block... 
                    #to move to the next loop
                    #set t=0 for next loop
                    if qr_coordinates[0]>start[1]-qr_coordinates[0]:
                        wet_run.uturn()
                        if wet_run.move_till('qr','left'):
                            t=0
                    else:
                        if wet_run.move_till('qr','right'):
                            t=0





    
    #elif callable(motion.forward):
  


    #put condition for finishing mapping here       

    if ( len(qr_coordinates)==2)+(number_of_boxes==3)+ (len(end_coordinates)==1)<3:
        return move()
    else:
        return [qr_coordinates,box_coordinates,start_coordinates,end_coordinates]
        #buzzer.buzz()

    








# '''
# to do-

#  forward thread            done(?)
#  time check                done
#  order                     not needed
#  mapping decide
#  wet run
#  distances check for qr

# ADD A PARAMETER TO FORWARD!!!!




