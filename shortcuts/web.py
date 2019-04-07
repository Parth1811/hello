from copy import deepcopy
import os
import pygame

BASE_APP_HEIGHT = 400
BASE_APP_WIDTH = 600
NORMAL_FONT_SIZE = 25
LARGE_FONT_SIZE = 35

BLACK   = (0,0,0)
WHITE   = (255,255,255)
GREEN   = (0,255,0)
ORANGE  = (255,143,00)
BLUE    = (30,136,229)  #(0,77,64)

GLOBAL_WEBSITE_LIST = [
    ["Academic",
        ('EE720', 'https://www.ee.iitb.ac.in/~sarva/courses/EE720/Spring2019.html'),
        ('EE230', 'http://wel.ee.iitb.ac.in/teaching_labs/WEL%20Site/ee230/Labsheets-2019/labsheets_2019.html'),
        ('EE214', 'https://moodle.iitb.ac.in/course/view.php?id=8950'),
        ('EE222', 'https://moodle.iitb.ac.in/mod/forum/view.php?id=69752'),
        ('EE234', 'https://moodle.iitb.ac.in/course/view.php?id=8954'),
        ('GNR652', 'https://moodle.iitb.ac.in/mod/forum/view.php?id=69912'),
    ],

    ["Github",
        ('Django Github', 'https://github.com/django/django'),
        ('Django PR Github', 'https://github.com/django/django/pulls'),
        ('Robosub Github', 'https://github.com/auv-iitb/robosub'),
        ('Hello Github', 'https://github.com/Parth1811/hello'),
    ],

    ["Gmail",
        ('Gmail-parth4iitb', 'https://mail.google.com/mail/u/1/#inbox'),
        ('Gmail-django.parth', 'https://mail.google.com/mail/u/3/#inbox'),
    ],

    ["Google Groups",
        ('Django Dev', 'https://groups.google.com/forum/#!forum/django-developers'),
        ('Django Tickets', 'https://code.djangoproject.com/'),
        ('AUV Software', 'https://groups.google.com/forum/#!forum/software_auv'),
        ('Django IRC', 'http://webchat.freenode.net?nick=Parth1811&channels=%23django&prompt=1'),
    ],

    ('OverLeaf', 'https://www.overleaf.com/project'),
    ('JioSaavn', 'https://www.jiosaavn.com/'),
    ('WakaTime', 'https://wakatime.com/dashboard'),
    ('Django tickets', 'https://code.djangoproject.com/ticket/')

]

WEBSITE_LIST = deepcopy(GLOBAL_WEBSITE_LIST)
PREV_WEBSITE_LIST = None
NEXT_WEBSITE_LIST = None
NESTED_WEBSITE_NAME = ''

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

def text(screen, label, x_location, y_location, size = NORMAL_FONT_SIZE, color = WHITE, background_color = (0,0,0,0)):
    basicfont = pygame.font.SysFont(None, size)
    text_surface2 = basicfont.render(label, True, color)
    text_surface2.set_alpha(128)
    text_surface = basicfont.render(label, True, color)
    text_surface.fill(background_color)
    text_surface.blit(text_surface2, (0,0))
    text_rect = text_surface.get_rect()
    text_rect.center = (x_location , y_location) #self.screen.get_rect().centerx
    screen.blit(text_surface, text_rect)

def get_ticket_no(website_list, index):
    width, height = BASE_APP_WIDTH/5, BASE_APP_HEIGHT/10
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Type ticket to be launced")

    TICKET_NO = ''
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                for i in range(10):
                    if event.key == pygame.K_0 +i:
                        TICKET_NO += str(i)
                if event.key == pygame.K_BACKSPACE:
                    TICKET_NO = TICKET_NO[:-1]
                if event.key == pygame.K_RETURN:
                    website_list[index] = (website_list[index][0], website_list[index][1]+TICKET_NO)
                    return
                if event.key == pygame.K_DOWN or event.key == pygame.K_q:
                    exit()


        screen.fill(WHITE)
        text(screen, str(TICKET_NO), width/2, height/2, NORMAL_FONT_SIZE, BLACK)
        pygame.display.update()


def apply_settings(WEBSITE_INDEX):
    if WEBSITE_INDEX == -1:
        return
    if WEBSITE_LIST[WEBSITE_INDEX][0] == 'Django tickets':
        get_ticket_no(WEBSITE_LIST, WEBSITE_INDEX)
    os.system('nohup chromium-browser ' + WEBSITE_LIST[WEBSITE_INDEX][1] + ' >/dev/null 2>&1 &')

screen = pygame.display.set_mode((BASE_APP_WIDTH , BASE_APP_HEIGHT))
pygame.display.set_caption("select Website to be launced")
image = pygame.image.load('/home/parth/shortcuts/firefox.jpg')
image = pygame.transform.scale(image, screen.get_size())
# pygame.transform.scale(image, screen.get_size())

WEBSITE_INDEX = -1
WEBSITE_NAME = ''

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            for i, website in enumerate(WEBSITE_LIST):
                if event.key == pygame.K_1 + i:
                    if type(website) == type([]):
                        NESTED_WEBSITE_NAME = website[0]
                        website.pop(0)
                        PREV_WEBSITE_LIST = WEBSITE_LIST
                        WEBSITE_LIST = website
                        NEXT_WEBSITE_LIST = None
                    else:
                        WEBSITE_INDEX = i
                        WEBSITE_NAME = website[0]
            if event.key == pygame.K_RETURN:
                apply_settings(WEBSITE_INDEX)
                exit()
            if event.key == pygame.K_LEFT:
                if PREV_WEBSITE_LIST == None:
                    continue
                if NESTED_WEBSITE_NAME != '':
                    WEBSITE_LIST.insert(0,NESTED_WEBSITE_NAME)
                NEXT_WEBSITE_LIST = WEBSITE_LIST
                WEBSITE_LIST = PREV_WEBSITE_LIST
                PREV_WEBSITE_LIST, NESTED_WEBSITE_NAME = None, ''
                WEBSITE_INDEX = -1
                WEBSITE_NAME = ''
            if event.key == pygame.K_RIGHT:
                if NEXT_WEBSITE_LIST == None:
                    continue
                NESTED_WEBSITE_NAME = NEXT_WEBSITE_LIST[0]
                NEXT_WEBSITE_LIST.pop(0)
                PREV_WEBSITE_LIST = WEBSITE_LIST
                WEBSITE_LIST = NEXT_WEBSITE_LIST
                NEXT_WEBSITE_LIST = None
                WEBSITE_INDEX = -1
                WEBSITE_NAME = ''
            if event.key == pygame.K_DOWN or event.key == pygame.K_q:
                exit()


    # screen.fill(WHITE)
    screen.blit(image, (0,0))
    text(screen, "Please select the " + NESTED_WEBSITE_NAME + " Website to be launched", BASE_APP_WIDTH/2, BASE_APP_HEIGHT/20, LARGE_FONT_SIZE)

    for i, website in enumerate(WEBSITE_LIST):
        text(screen, str(i+1)+") "+ website[0], BASE_APP_WIDTH/2, (i+5)*BASE_APP_HEIGHT/15, size=LARGE_FONT_SIZE, background_color = ORANGE)

    text(screen, "Selected Website:- "+ WEBSITE_NAME, BASE_APP_WIDTH/2, BASE_APP_HEIGHT- (BASE_APP_HEIGHT/20), LARGE_FONT_SIZE, BLUE)
    pygame.display.update()
