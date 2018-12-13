
import time
import motor
import us
import feedback_loop


go_forward=True
def stop():
    global go_forward
    go_forward=False
    motor.set_speed('right',0)
    motor.set_speed('left',0)
    

def forward(direction):
    if direction='right':
        trigger=us.right_trig
        echo=us.right_echo
        other='left'
    if direction='left':
        trigger=us.left_trig
        echo=us.left_echo
        other='right'

    speed=80
    global go_forward
    integral_error=0
    go_forward=True

    last_error=feedback_loop.ideal_right_wall_dist_wall_dist-us.dist(trigger,echo)
    while go_forward==True:
        values=feedback_loop.adjustment_values(direction,us.dist(trigger,echo),integral_error,last_error)
        pid_value= values[0]
        print(pid_value)
        integral_error=values[1]
        last_error=values[2]

        motor.set_speed(direction,motor.default_motor_speed+pid_value)
        motor.set_speed(other,motor.default_motor_speed-pid_value)
        time.sleep(feedback_loop.delay)

        dist=us.dist(us.front_trig,us.front_echo)
        if dist<40:
            speed=35+dist
            motor.set_speed('b',speed+30)

        if us.dist(front_trig,front_echo)<15:
            stop()
    


def turn(direction):
    if direction=='right':
        motor.set_speed('r',-80)
        motor.set_speed('l',80)
        time.sleep(1)
        
    elif direction=='left':
        motor.set_speed('l',-80)
        motor.set_speed('r',80)
        time.sleep(1) #set sleep time

    motor.set_speed('b',0)
    



#forward()