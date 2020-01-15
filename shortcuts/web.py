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
ORANGE  = (255,143,00)  #(0, 172, 193)
BLUE    = (30,136,229)  #(0,77,64)

GLOBAL_WEBSITE_LIST = [
    ["Academic",
        ('EE 328', 'https://moodle.iitb.ac.in/course/view.php?id=11857'),
        ('EE 302', 'https://moodle.iitb.ac.in/course/view.php?id=11855'),
        ('EE 344', 'https://moodle.iitb.ac.in/course/view.php?id=11202'),
        ('EE 338', 'https://moodle.iitb.ac.in/course/view.php?id=11201'),
        ('EE 334', 'https://moodle.iitb.ac.in/course/view.php?id=11200'),
        ('EE 324', 'https://moodle.iitb.ac.in/course/view.php?id=11197'),
        ('Asc', 'https://asc.iitb.ac.in/'),
        ('Drive', 'https://drive.google.com/drive/u/1/folders/19elCjP7PwvlOHL322LcHzfyDuF8_97H7'),
    ],

    ["Github",
        ('Robosub Github', 'https://github.com/auv-iitb/robosub'),
        ('Hello Github', 'https://github.com/Parth1811/hello'),
        ('RTD WIP Issue', 'https://github.com/readthedocs/readthedocs.org/issues/5445'),
    ],

    ["Gmail",
        ('Gmail-parth4iitb', 'https://mail.google.com/mail/u/1/#inbox'),
        ('Gmail-django.parth', 'https://mail.google.com/mail/u/2/#inbox'),
    ],

    ["Discussion Groups",
        ('AUV Software', 'https://groups.google.com/forum/#!forum/software_auv'),
        ('AboutCode IRC', 'https://gitter.im/aboutcode-org/discuss#'),
        ('ReadTheDocs IRC', 'https://gitter.im/rtfd/readthedocs.org'),
        ('Django IRC', 'http://webchat.freenode.net?nick=Parth1811&channels=%23django&prompt=1'),
    ],

    ('OverLeaf', 'https://www.overleaf.com/project'),
    #('JioSaavn', 'https://www.jiosaavn.com/'),
    ('Workflowy', 'https://workflowy.com/'),
    ('WakaTime', 'https://wakatime.com/dashboard'),
    ('Django tickets', 'https://code.djangoproject.com/ticket/'),
    #('VISA', 'https://cgifederal.secure.force.com/ApplicantHome'),
]

WEBSITE_LIST = deepcopy(GLOBAL_WEBSITE_LIST)
PREV_WEBSITE_LIST = None
NEXT_WEBSITE_LIST = None
NESTED_WEBSITE_NAME = ''

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

def text(screen, label, x_location, y_location, size = NORMAL_FONT_SIZE, color = WHITE, background_color = (0,0,0,0), center=True):
    basicfont = pygame.font.SysFont(None, size)
    text_surface2 = basicfont.render(label, True, color)
    text_surface2.set_alpha(128)
    text_surface = basicfont.render(label, True, color)
    text_surface.fill(background_color)
    text_surface.blit(text_surface2, (0,0))
    text_rect = text_surface.get_rect()
    text_rect.center = (x_location , y_location) #self.screen.get_rect().centerx
    text_pos = text_rect if center else (x_location , y_location)
    screen.blit(text_surface, text_pos)

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
                    if (event.key == pygame.K_0 + i) or (event.key == pygame.K_KP0 + i):
                        TICKET_NO += str(i)
                if event.key == pygame.K_BACKSPACE:
                    TICKET_NO = TICKET_NO[:-1]
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
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
    os.system('nohup google-chrome ' + WEBSITE_LIST[WEBSITE_INDEX][1] + ' >/dev/null 2>&1 &')

screen = pygame.display.set_mode((BASE_APP_WIDTH , BASE_APP_HEIGHT))
pygame.display.set_caption("select Website to be launced")
image = pygame.image.load('/home/parth/hello/shortcuts/firefox.jpg')
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
                if (event.key == pygame.K_1 + i) or (event.key == pygame.K_KP1 + i):
                    if type(website) == type([]):
                        NESTED_WEBSITE_NAME = website[0]
                        website.pop(0)
                        PREV_WEBSITE_LIST = WEBSITE_LIST
                        WEBSITE_LIST = website
                        NEXT_WEBSITE_LIST = None
                    else:
                        WEBSITE_INDEX = i
                        WEBSITE_NAME = website[0]
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
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
        text(screen, str(i+1)+") "+ website[0], 30, (i+3)*BASE_APP_HEIGHT/15, color = BLACK,size=LARGE_FONT_SIZE, background_color = BLUE, center=False)

    text(screen, "Selected Website:- "+ WEBSITE_NAME, BASE_APP_WIDTH/2, BASE_APP_HEIGHT- (BASE_APP_HEIGHT/20), LARGE_FONT_SIZE, BLACK, background_color = BLUE)
    pygame.display.update()
