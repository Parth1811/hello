import cv2
from datetime import datetime
import numpy as np
import pygame
from pygame.locals import *
import time
import sys

import buttons

BASE_FPS = 30
BASE_APP_WIDTH = 640
BASE_APP_HEIGHT = 360
MENU_HEIGHT = 25
SLIDER_HEIGHT = 8

BACkGROUND_COLOR = (55,71,79)
LIGHT_GREY = (75,91,99)
YELLOW = (255,235,59)

GLOBAL_BUTTON_ARRAY = []

def video_read(video_filename):
    capture = cv2.VideoCapture(video_filename)
    video_pass = dict()
    frame_array = []
    rect = True
    while rect:
        rect, frame = capture.read()
        frame_array.append(frame)
    frame_array = np.array(frame_array)
    video_pass["frames"] = frame_array
    video_pass["frame_count"] = frame_array.size
    video_pass["resolution"] = dict()
    video_pass["resolution"]["height"] = frame_array[0].shape[0]
    video_pass["resolution"]["width"] = frame_array[0].shape[1]
    time.sleep(3)
    video_pass["name"] = str(video_filename)
    return video_pass

def video_convert(video_pass):
    video_to_display = dict()
    video_to_display["frame_count"] = video_pass["frame_count"]-1
    video_to_display["frames"] = video_pass["frames"]
    video_to_display["frames_final"] = []
    convert_counter = 0
    while convert_counter < video_to_display["frame_count"]-1:
        frame_to_display = cv2.cvtColor(video_pass["frames"][convert_counter]\
            , cv2.COLOR_BGR2RGB)
        frame_to_display = np.rot90(frame_to_display)
        frame_to_display = cv2.resize(frame_to_display,(360,640))
        #frame_surface = pygame.surfarray.make_surface(frame_to_display)
        video_to_display["frames_final"].append(frame_to_display)
        convert_counter +=1
    return video_to_display

def draw_slider(timer,total_time,screen):
    percent_fill = float(timer) / total_time
    pixel_percent = int(percent_fill * BASE_APP_WIDTH)
    screen.fill(YELLOW, rect = [0, BASE_APP_HEIGHT, pixel_percent,SLIDER_HEIGHT] )
    screen.fill(LIGHT_GREY, rect = [pixel_percent, BASE_APP_HEIGHT, \
        BASE_APP_WIDTH,SLIDER_HEIGHT] )

def initialize_display():
    pygame.init()
    pygame.display.set_caption("MACHINE LEARNING DATABASING TOOL (AUV-IITB)")
    screen = pygame.display.set_mode([BASE_APP_WIDTH,\
        BASE_APP_HEIGHT+MENU_HEIGHT+SLIDER_HEIGHT])
    clock = pygame.time.Clock()
    return screen,clock


if __name__ == "__main__":
    video_pass = video_read('resources/test.avi')
    video_to_display = video_convert(video_pass)
    screen, clock = initialize_display()

    running = True
    timer = 0

    play_flag = True
    play_button = buttons.Button("Play",0,BASE_APP_HEIGHT+SLIDER_HEIGHT, play_flag,\
        screen, button_image_ = "resources/play.png")

    pause_button = buttons.Button("Pause",0,BASE_APP_HEIGHT+SLIDER_HEIGHT, \
        play_flag, screen,button_image_ = "resources/pause.png")
    try:
        while running:
            if timer >= video_to_display["frame_count"]:
                break
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clickPos = pygame.mouse.get_pos()
                    if play_button.is_clicked(clickPos[0],clickPos[1]):
                        play_flag = not play_flag
                if event.type == KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        timer -= 60
                        if timer < 0:
                            timer = 0
                    if event.key == pygame.K_RIGHT:
                        timer += 60
                        if timer > video_to_display["frame_count"]:
                            timer = 0
                    if event.key == pygame.K_UP:
                        play_flag = not play_flag
                    if event.key == pygame.K_DOWN:
                        sys.exit(0)

            screen.fill(BACkGROUND_COLOR)

            current_frame = video_to_display["frames_final"][timer]
            frame_surface = pygame.surfarray.make_surface(current_frame)
            screen.blit(frame_surface, (0,0))

            if play_flag:
                pause_button.draw_button()
                timer += 1
            else:
                play_button.draw_button()

            draw_slider(timer,video_to_display["frame_count"],screen)
            pygame.display.update()

            clock.tick(30)

    except:
        pygame.quit()
        cv2.destroyAllWindows()
