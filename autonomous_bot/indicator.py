import RPi.GPIO as gpio
import time

red_led=17
blue_led=27
buzzer=25

gpio.setmode(gpio.BCM)
gpio.setup(buzzer,gpio.OUT)
gpio.setup(red_led,gpio.OUT)
gpio.setup(blue_led,gpio.OUT)


def buzz():
	gpio.output(buzzer,True)


def glow(number):
	if number==1:
		pass
	if number==2:
		#set output blue 1 red 0
		gpio.output(blue_led,True)
	if number==3:
		#set red 1 blue 0 
		gpio.output(red_led,True)
	if number==4:
		gpio.output(red_led,True)
		gpio.output(blue_led,True)
		#set both zero

def stop():
	for pin in [blue_led,red_led,buzzer]:
		gpio.output(pin,False)
		#set rest all false



def end_signal():
	gpio.buzz()
	for i in 5:
		glow(1)
		time.sleep(1)
		glow(2)
		time.sleep(1)
	stop()
