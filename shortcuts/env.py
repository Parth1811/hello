import pygame
import os

BASE_APP_HEIGHT = 400
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

def apply_settings(env_name):
    if env_name != "default":
        command = 'echo "source ~/environments/' + env_name + '/bin/activate" >> ~/.bashrc'
        os.system(command)
    else:
        default_file = os.popen("sed '/source \~\/environments/d' ~/.bashrc")
        os.system("rm ~/.bashrc")
        os.system("touch ~/.bashrc")
        output_file = open(os.path.expanduser("~/.bashrc"), "w")
        for line in default_file:
            output_file.write(line)
        default_file.close()
        output_file.close()


screen = pygame.display.set_mode((BASE_APP_WIDTH , BASE_APP_HEIGHT))
pygame.display.set_caption("select Python environment")

env_list = os.listdir('/home/parth/environments')



ENV = "default"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            for i, env_name in enumerate(env_list):
                if event.key == pygame.K_1 + i:
                    ENV = env_name
            if event.key == pygame.K_0 or event.key == pygame.K_g :
                ENV = "default"
            if event.key == pygame.K_RETURN:
                apply_settings(ENV)
                exit()
            if event.key == pygame.K_DOWN or event.key == pygame.K_q:
                exit()


    screen.fill(WHITE)
    text(screen, "Please select the python environment", BASE_APP_WIDTH/2, BASE_APP_HEIGHT/20, LARGE_FONT_SIZE)

    for i, env_name in enumerate(env_list):
        text(screen, str(i+1)+") "+env_name, BASE_APP_WIDTH/2, (i+5)*BASE_APP_HEIGHT/23)

    text(screen, "0) Default", BASE_APP_WIDTH/2, (len(env_list)+5)*BASE_APP_HEIGHT/23)
    text(screen, "Selected Environment:- "+ ENV, BASE_APP_WIDTH/2, BASE_APP_HEIGHT- (BASE_APP_HEIGHT/20), LARGE_FONT_SIZE, GREEN)
    pygame.display.update()
