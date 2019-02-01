
'''import distances
from motion import motor_speed'''
import math
import motor 


ideal_right_wall_dist=5
ideal_left_wall_dist=5
delay=0.15
total_distance=10



def adjustment_values(direction,wall_dist,integral_error,last_error):

		#defining distances
	#self.right_wall_dist=right_wall_dist
	#self.left_wall_distance=left_wall_distance



		#init errors 

	error= ideal_right_wall_dist-wall_dist
	integral_error+=error*delay
	diff_error=(error-last_error)/delay
	last_error=error

	#if it strikes the wall
	if error>4 or error<-400:
		motor.set_speed('b',-100)
		time.sleep(0.2) 
		if direction=='right':
			motor.set_speed('r',80)
		else: 
			motor.set_speed('l',80)
		time.sleep(0.3)
		motor.set_speed('b',0)

	#so that it doesnt bend towards openings after turning right
	if error<-15:
		error=-0.2

	# #as it shouldnt get hyper 
	# if error>18:
	# 	error=2


		#define tuning constants
	Kp= 0.75
	Ki=0.0
	Kd=0.32

	P=Kp*error
	I=Ki*integral_error
	D=Kd*diff_error
	print(P)
	print(I)
	print(D)
	#if integral_error>=0.15 or integral_error<=-0.15:	integral_error=0
	pid_value=P+I+D
	if pid_value >15:
		pid_value=12
	if pid_value<-15:
		pid_value=-12


	return [pid_value,integral_error,last_error]

	'''set_motor_speed('right',motion.default_motor_speed-(P+I+D))
	set_motor_speed('left',motion.default_motor_speed+(P+I+D))
'''


'''
		5:3:3
		500:375:25
		'''

