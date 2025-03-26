import os
import subprocess
import sys
from copy import deepcopy

import pygame

CURRENT_FILE_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

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
    ["Academics",
        ["ECE 602", 
            ("BrightSpace", 'https://purdue.brightspace.com/d2l/home/1096470'),
            ("Discussion", 'https://piazza.com/class/lzvfo9f8pbo35x'),
            ("Drive", 'https://drive.google.com/drive/folders/1Caz_1OrrC-fykZfbOxYt46YlQLhE8umq?usp=drive_link'),
            ("Gradescope", "https://www.gradescope.com/courses/829304"),
        ],
        ["ECE 461", 
            ("BrightSpace", 'https://purdue.brightspace.com/d2l/home/1096370'),
            ("Discussion", 'https://piazza.com/class/lzvpabcdwx83b0'),
            ("Drive", 'https://purdue0-my.sharepoint.com/:f:/g/personal/davisjam_purdue_edu/EgqgWBmDKn9Ol6AI-6XPmUcBqTYAZIc2DcudUrZ1q7aNiw'),
            ("Gradescope", "https://www.gradescope.com/courses/825720"),
            ("Asana", "https://app.asana.com/0/1207999039125077/1207999039125077"),
        ]
    ],
    ["Purdue",
        ("myPurdue", 'https://wl.mypurdue.purdue.edu/'),
        ("Outlook", 'https://outlook.office.com/mail/'),
        ('Scheduling Assitant', 'https://timetable.mypurdue.purdue.edu/Timetabling/gwt.jsp?page=sectioning'),
        ("Push Portal", 'https://myhealth.push.purdue.edu/home.aspx'),
    ],
    # ["Masters",
    #     ('Univ List', 'https://docs.google.com/spreadsheets/d/1-4-QPh9VTTqRrTzTmvqum-0r3oNe70P-DpvimYsz_z8/edit#gid=0'),
    #     ('My Masters Drive', 'https://drive.google.com/drive/folders/1GiQS_gAi7X69T-e3byqriHdHS861HUBe?usp=sharing'),
    #     ("Chad's drive", 'https://drive.google.com/drive/folders/1pKAFV7vOl1sT4xlc27T_dHoA4m18Yi4p'),
    # ],
    # ["Admission Portal",
    #     ("Carnegie Mellon University", "https://admissions.scs.cmu.edu/portal/apply_gr"),
    #     ("University of Pennslyvenia", "https://www.applyweb.com/upenng/index.ftl"),
    #     ("Johns Hopkins University", "https://applygrad.jhu.edu/apply/"),
    #     ("Georgia Institute of Technology", "https://gradapp.gatech.edu/apply/"),
    #     ("New York University", "https://apply.engineering.nyu.edu/apply/"),
    #     ("Northwestern University", "https://apply.mccormick.northwestern.edu/apply/"),
    #     ("University of Michigen", "https://www.applyweb.com/cgi-bin/app?s=umgrad"),
    #     ("University of Maryland", "https://terpengage.force.com/community/ERx_Forms__Homepage"),
    #     ("Northeastern University", "https://enroll.northeastern.edu/apply/"),
    # ],
    # ('Drivetrain', 'https://%s.drivetrain.ai/'),
    # ["Github",
    #     ('Netra Explainability', 'https://github.com/udaan-com/udaan-netra-explainability'),
    #     ('Robosub Github', 'https://github.com/auv-iitb/robosub'),
    #     ('Hello Github', 'https://github.com/Parth1811/hello'),
    # ],
    # ["Gmail",
    #     ('Gmail-parthvin', 'https://mail.google.com/mail/u/0/#inbox'),
    #     ('Gmail-parthpatil-udaan', 'https://mail.google.com/mail/u/1/#inbox'),
    #     # ('Gmail-django.parth', 'https://mail.google.com/mail/u/3/#inbox'),
    # ],
    # ('Calendar', 'https://calendar.google.com/calendar/u/1/r?hl=en-GB&pli=1'),
    # ('Placement Portal', 'https://campus.placements.iitb.ac.in/'),
    # ('Placement Blog', 'http://placements.iitb.ac.in/blog/'),
    # ["Discussion Groups",
    #     ('AUV Software', 'https://groups.google.com/forum/#!forum/software_auv'),
    #     # ('SNARE slack', 'https://app.slack.com/client/T3U3LQR6Y/C4CEKSG9E/thread/C3U3LQX7E-1582274203.072500'),
    #     # ('Django IRC', 'http://webchat.freenode.net?nick=Parth1811&channels=%23django&prompt=1'),
    #     # ('Zulip IRC', "https://chat.zulip.org/#narrow/stream/95-new-members/topic/GSoC.202020"),
    #     # ('Processing IRC', 'https://discourse.processing.org/c/summer-of-code')
    #     # ('Gitter', 'https://gitter.im/'),
    # ],
    ('OverLeaf', 'https://www.overleaf.com/project'),
    ["Google Sheets",
        ("Intern", "https://docs.google.com/spreadsheets/d/1gtHfQ5kkoTUma-_VejWQyBAvYn4Bf58Q75eeaPUa--Q/edit?gid=1713903924#gid=1713903924"),
        ("CBMC Sheet", "https://docs.google.com/spreadsheets/d/161X1THr_XqXr7HQ3FnKfecgxQCyI0aZVlrxQMHTzdoY/edit?gid=0#gid=0"),
        ("461 Handoff", "https://docs.google.com/spreadsheets/d/1T_908snvNCGikO8o4qFtUT7QTz9usmmh0pCtogHVbYE/edit?gid=0#gid=0"),
    ],
    #('JioSaavn', 'https://www.jiosaavn.com/'),
    # ('Workflowy', 'https://workflowy.com/'),
    # ('WakaTime', 'https://wakatime.com/dashboard'),
    # ('Django tickets', 'https://code.djangoproject.com/ticket/%s'),
    # ('SNARE Issues', 'https://github.com/mushorg/snare/issues/'),
    # ('TANNER Issues', 'https://github.com/mushorg/tanner/issues/'),
    #('VISA', 'https://cgifederal.secure.force.com/ApplicantHome'),
    ["Macros",
        ("Macro:\\begin{bmatrix} \\end{bmatrix}", r"\\begin{bmatrix} \\end{bmatrix}"),
        ("Macro:C++ template",\
r'''
#include <bits/stdc++.h>
using namespace std;

#define fo(i, n) for (i = 0; i < n; i++)
#define Fo(i, k, n) for (i = k; k < n ? i < n : i > n; k < n ? i += 1 : i -= 1)
#define ll long long
#define deb(x) cout << #x << "=" << x << endl
#define deb2(x, y) cout << #x << "=" << x << "," << #y << "=" << y << endl
#define pb push_back
#define all(x) x.begin(), x.end()
#define clr(x) memset(x, 0, sizeof(x))
typedef vector<int> vi;
typedef vector<ll> vl;
'''),
    ]
]

WEBSITE_LIST = deepcopy(GLOBAL_WEBSITE_LIST)
PREV_WEBSITE_LIST = None
NEXT_WEBSITE_LIST = None
NESTED_WEBSITE_NAME = ''

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

def get_ticket_no(website_list, index, format=True):
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
                if event.unicode == "S":
                    TICKET_NO += ".stagingv2"
                    continue
                if event.unicode == "P":
                    TICKET_NO += ".preprodv2"
                    continue
                if event.key in range(pygame.K_a, pygame.K_z + 1):
                    TICKET_NO += event.unicode
                if event.key == pygame.K_BACKSPACE:
                    TICKET_NO = TICKET_NO[:-1]
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    if format:
                        website_list[index] = (website_list[index][0], website_list[index][1] % TICKET_NO)
                    else:
                        website_list[index] = (website_list[index][0], website_list[index][int(TICKET_NO)][1])
                    return
                if event.key == pygame.K_DOWN or event.key == pygame.K_q:
                    exit()


        screen.fill(WHITE)
        text(screen, str(TICKET_NO), width/2, height/2, NORMAL_FONT_SIZE, BLACK)
        pygame.display.update()


def apply_settings(WEBSITE_INDEX):
    if WEBSITE_INDEX == -1:
        return
    if WEBSITE_LIST[WEBSITE_INDEX][0] in ('Django tickets', 'RTD Issues', 'SNARE Issues', 'TANNER Issues', 'Drivetrain'):
        get_ticket_no(WEBSITE_LIST, WEBSITE_INDEX)
    if WEBSITE_LIST[WEBSITE_INDEX][0] in ('Vocab Lists'):
        get_ticket_no(WEBSITE_LIST, WEBSITE_INDEX, False)
    if WEBSITE_LIST[WEBSITE_INDEX][0].startswith("Macro:"):
        os.popen(f"echo '{WEBSITE_LIST[WEBSITE_INDEX][1]}' | pbcopy")
        return

    # os.system('nohup google-chrome ' + WEBSITE_LIST[WEBSITE_INDEX][1] + ' >/dev/null 2>&1 &')
    os.system(f'open -a "Google Chrome" "{WEBSITE_LIST[WEBSITE_INDEX][1]}"')



WEBSITE_INDEX = -1
WEBSITE_NAME = ''


if len(sys.argv) > 1:
    for index in sys.argv[1]:
        if type(WEBSITE_LIST[int(index)-1]) == type([]):
            NESTED_WEBSITE_NAME = WEBSITE_LIST[int(index)-1][0]
            WEBSITE_LIST = WEBSITE_LIST[int(index)-1][1:]
            continue
        WEBSITE_INDEX = int(index)-1

    apply_settings(WEBSITE_INDEX)
    exit()


os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

screen = pygame.display.set_mode((BASE_APP_WIDTH , BASE_APP_HEIGHT))
pygame.display.set_caption("select Website to be launced")
image = pygame.image.load(os.path.join(CURRENT_FILE_DIRECTORY, 'firefox.jpg'))
image = pygame.transform.scale(image, screen.get_size())
# pygame.transform.scale(image, screen.get_size())

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
