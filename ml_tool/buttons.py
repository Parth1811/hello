import pygame
import main

class Button:
    def __init__(self, name_, button_x_, button_y_,  update_variable_, screen_,\
        color_ = main.BACkGROUND_COLOR, button_image_ = None, size_ = \
            [main.MENU_HEIGHT, main.MENU_HEIGHT]):

        self.name = str(name_)
        self.variable = update_variable_
        self.pos_x = button_x_
        self.pos_y = button_y_
        self.color = color_
        self.button_image = button_image_
        self.size = size_
        self.screen = screen_

    def draw_button(self):
        if self.button_image == None:
            self.screen.fill(self.color, rect = [self.pos_x, self.pos_y \
                ,self.size[0],self.size[1]])
        else:
            try:
                image = pygame.image.load(self.button_image)
            except:
                print ("Invalid image path for button:" + self.name)
            image = pygame.transform.scale(image, self.size)
            self.screen.blit(image,(self.pos_x,self.pos_y))

    def is_clicked(self, mouse_x, mouse_y):
        x_flag = (mouse_x > self.pos_x) and (mouse_x < (self.pos_x+self.size[0]))
        y_flag = (mouse_y > self.pos_y) and (mouse_y < (self.pos_y+self.size[1]))
        return (x_flag and y_flag)
