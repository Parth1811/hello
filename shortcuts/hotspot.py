import pygame
import os
import time

BASE_APP_HEIGHT = 150
BASE_APP_WIDTH = 600
NORMAL_FONT_SIZE = 25
LARGE_FONT_SIZE = 35

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)


os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

def text(screen, label, x_location, y_location, size = NORMAL_FONT_SIZE, color = BLACK):
    basicfont = pygame.font.SysFont(None, size)
    text_surface = basicfont.render(label, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x_location , y_location) #self.screen.get_rect().centerx
    text_surface.set_alpha(128)
    screen.blit(text_surface, text_rect)


def apply_settings(command):
    if command == "connect":
        os.system("echo 1911 | sudo -S cp ~/hello/shortcuts/laptop_hotspot_auto_connect.bak /etc/NetworkManager/system-connections/laptop_hotspot")
        os.system("echo 1911 | sudo -S service network-manager restart ")
        os.system("bash ~/hello/shortcuts/hotspot_new.sh")
    if command == "disconnect":
        os.system("echo 1911 | sudo -S cp ~/hello/shortcuts/laptop_hotspot.bak /etc/NetworkManager/system-connections/laptop_hotspot")
        os.system("echo 1911 | sudo -S service network-manager restart ")

screen = pygame.display.set_mode((BASE_APP_WIDTH , BASE_APP_HEIGHT))
pygame.display.set_caption("Connect/Discoonect hotspot")

command = "connect"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                command = "connect"
            if event.key == pygame.K_2:
                command = "disconnect"
            if event.key == pygame.K_0 or event.key == pygame.K_g :
                ENV = "connect"
            if event.key == pygame.K_RETURN:
                apply_settings(command)
                exit()
            if event.key == pygame.K_DOWN or event.key == pygame.K_q:
                exit()


    screen.fill(WHITE)
    text(screen, "Select to connect or discoonect to the hotspot", BASE_APP_WIDTH/2, BASE_APP_HEIGHT/15, LARGE_FONT_SIZE)

    text(screen, str(1)+") "+"Connect", BASE_APP_WIDTH/2, (3)*BASE_APP_HEIGHT/10)
    text(screen, str(2)+") "+"Disconnect", BASE_APP_WIDTH/2, (4)*BASE_APP_HEIGHT/10)

    text(screen, "Selected Command:- "+ command, BASE_APP_WIDTH/2, BASE_APP_HEIGHT- (BASE_APP_HEIGHT/8), LARGE_FONT_SIZE, GREEN)
    pygame.display.update()
