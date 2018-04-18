import cv2
import numpy as np
import pygame
import sys
from pygame.locals import *

cap = cv2.VideoCapture('9.avi')
pygame.init()
pygame.display.set_caption("OpenCV camera stream on Pygame")
screen = pygame.display.set_mode([1280,720])
ret, frame = cap.read()

try:
    while True:
        screen.fill([0,0,0])
        frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame2 = np.rot90(frame1)
        frame3 = pygame.surfarray.make_surface(frame2)
        screen.blit(frame3, (0,0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                sys.exit(0)
except KeyboardInterrupt,SystemExit:
    pygame.quit()
    cv2.destroyAllWindows()
