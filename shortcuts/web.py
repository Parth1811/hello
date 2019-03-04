import pygame
import os

BASE_APP_HEIGHT = 400
BASE_APP_WIDTH = 600
NORMAL_FONT_SIZE = 25
LARGE_FONT_SIZE = 35

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)

WEBSITE_LIST = [
    ('EE720', 'https://www.ee.iitb.ac.in/~sarva/courses/EE720/Spring2019.html'),
    ('EE230', 'http://wel.ee.iitb.ac.in/teaching_labs/WEL%20Site/ee230/Labsheets-2019/labsheets_2019.html'),
    ('Django Github', 'https://github.com/django/django'),
    ('OverLeaf', 'https://www.overleaf.com/project'),
    ('JioSaavn', 'https://www.jiosaavn.com/'),
    ('WakaTime', 'https://wakatime.com/dashboard')
]

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

def text(screen, label, x_location, y_location, size = NORMAL_FONT_SIZE, color = BLACK):
    basicfont = pygame.font.SysFont(None, size)
    text_surface = basicfont.render(label, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x_location , y_location) #self.screen.get_rect().centerx
    text_surface.set_alpha(128)
    screen.blit(text_surface, text_rect)

def apply_settings(WEBSITE_INDEX):
    os.system('nohup firefox ' + WEBSITE_LIST[WEBSITE_INDEX][1] + ' >/dev/null 2>&1 &')

screen = pygame.display.set_mode((BASE_APP_WIDTH , BASE_APP_HEIGHT))
pygame.display.set_caption("select Website to be launced")

WEBSITE_INDEX = -1
WEBSITE_NAME = ''

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            for i, website in enumerate(WEBSITE_LIST):
                if event.key == pygame.K_1 + i:
                    WEBSITE_INDEX = i
                    WEBSITE_NAME = website[0]
            if event.key == pygame.K_RETURN:
                apply_settings(WEBSITE_INDEX)
                exit()
            if event.key == pygame.K_DOWN or event.key == pygame.K_q:
                exit()


    screen.fill(WHITE)
    text(screen, "Please select the Website to be launched", BASE_APP_WIDTH/2, BASE_APP_HEIGHT/20, LARGE_FONT_SIZE)

    for i, website in enumerate(WEBSITE_LIST):
        text(screen, str(i+1)+") "+ website[0], BASE_APP_WIDTH/2, (i+5)*BASE_APP_HEIGHT/23)

    text(screen, "Selected Website:- "+ WEBSITE_NAME, BASE_APP_WIDTH/2, BASE_APP_HEIGHT- (BASE_APP_HEIGHT/20), LARGE_FONT_SIZE, GREEN)
    pygame.display.update()
