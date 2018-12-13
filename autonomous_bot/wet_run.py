
import mapping 
import motion 
import vision
import bot_movement
import dry_run as dist
import time
from threading import Thread

def wait_for_path(direction):
    
    
    while us.dist(us.front_trig,us.front_echo)<14  or check_for_qr():
        time.sleep(0.5)
        pass
    print('block removed')
    time.sleep(1)
    dry_run.thread_forward(direction)
    #so that it goes to the next cell
    time.sleep(1)



def uturn():
	motion.turn('left')
	motion.turn('left')


def check_uturn(last_dir,current_dir):
	if not last_dir==current_dir:
		uturn()


def move_till(destination,direction):
	#determine whether right or left wall
	if direction=='right':
		first='right'
		second='left'
	elif direction=='left':
		first='left'
		second='left'

	#if first open turn right
	if dist.check(first):
		motion.turn(first)
	if callable(motion.forward):
        dist.thread_forward(first)

     #if front blocked, check for destination
    if not check('front'):
    	motion.stop()
	    if destination=='qr':
		    if dist.check_for_qr:
		    	if vision.scan_qr():
		    		wait_for_path(direction)
		    	return True
		elif destination=='box' or destination=='block':
			if vision.check_for_block():
				wait_for_path(direction)
				return True
		elif destination=='end':
			if vision.ground_is_white():
				return True
	#turn second if nothing found
	else:
		motion.turn(second)
	#call func again until destination reached
	return move_till(destination,direction)


#finally we used a bs brute force method fml .-.

def run(qr_coordinates,box_coordinates,start_coordinates,end_coordinates):
	#define current coordinate
	vision.zbarcam()
	current_coordinate=start_coordinates[0]
	direction='right'
	
	#on start
	if start_coordinate[1]-box_coordinates[1]>box_coordinates[0]:
		direction='right'
		current_coordinate=box_coordinates[1]
	else:
		direction='left'
		current_coordinate=box_coordinates[0]

	#store last direction
	last_direction=direction


	#1st block reached
	#if we have reached first block using direction,
	#check if left wall follow < right or otherwise 
	if move_till('box',direction):

		left_for_1= start_coordinates[1]-box_coordinates[1]+box_coordinates[0]
		right_for_1= box_coordinates[1]-box_coordinates[0]

		#check if on first block found on dry or 2nd

		if current_coordinate=box_coordinates[0]:
			if left_for_1>right_for_1:
				direction='right'

			else: 
				uturn()
				direction='left'

			current_coordinates=box_coordinates[1]


		else:
			if left_for_1>right_for_1:
				#direction will be inverted..
				direction='left'
			else:
				uturn()
				direction='right'

			current_coordinate=box_coordinates[0]

		#update last direction after every check
		last_direction=direction

	#2nd block reached
	if move_till('box',direction):
		#if on block 2 in rwf 
		if current_coordinate=box_coordinates[1]:
			#if block comes b4 qr in rwf.
			if box_coordinates[1]>qr_coordinates[0]:
				left_for_1=box_coordinates[1]-qr_coordinates[0]
				right_for_1=start_coordinates[1]-left_for_1
				if right_for_1>left_for_1:
					direction='right'
					
				else:
					direction='left'

				check_uturn(last_direction,direction)

			#if it comes after qr decisions inverted
			else :
				right_for_1=qr_coordinates[0]-box_coordinates[1]
				left_for_1=start_coordinates[1]-right_for_1

				if right_for_1<left_for_1:
					direction='left'
					
				else :
					direction='right'

				check_uturn(last_direction,direction)
		#if on block 1 in rwf
		else :
			right_for_1=(qr_coordinates[0]-box_coordinates[0])

			if right_for_1<0:
				left_for_1=-right_for_1
				right_for_1=start_coordinates-left_for_1
			else:
				left_for_1=start_coordinates[1]-right_for_1

			if right_for_1>left_for_1:
				direction='left'
				
			else:
				direction='right'
			
			check_uturn(last_direction,direction)
		#update
		current_coordinates=qr_coordinates[0]
		last_direction=direction



	#reached till qr
	if move_till('qr',direction):
		if box_coordinates[2]<start_coordinates[1]/2:
			#do something like right wall follow until forward blocked or turning comes
		
			direction='right'
		else:
			direction='left'
	last_direction=direction




	#reached box 3
	if move_till('box',direction):
		if box_coordinates[2]>qr_coordinates[1]:
			direction='left'
		else:
			direction='right'
		check_uturn(last_direction,direction)



	#reached qr 2
	if move_till('qr',direction):
		if end_coordinates[0]>qr_coordinates[1]:
			direction='right'
		else:
			direction='left'
		check_uturn(last_direction,direction)

	if move_till('end',direction):
		return True




# 1.thread wait for path in wet run... or use it in run

# 2.make changes to fit in buzzer

# 3.MAKE CHANGES IN FORWARD*****