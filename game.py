import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

game_display = pygame.display.set_mode((800,600))
pygame.display.set_caption("auv ML tool")

lead_x = 300
lead_y = 300
vel_x = 1
vel_y = 0

clock = pygame.time.Clock()

gameExit = False
while not gameExit:
    for event in pygame.event.get():
        print event
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            clickPos = pygame.mouse.get_pos()
            print clickPos
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x -= 10
                vel_x = -1
                vel_y = 0
            if event.key == pygame.K_RIGHT:
                lead_x += 10
                vel_x = 1
                vel_y = 0
            if event.key == pygame.K_UP:
                lead_y -= 10
                vel_x = 0
                vel_y = -1
            if event.key == pygame.K_DOWN:
                lead_y += 10
                vel_x = 0
                vel_y = 1

    lead_x += vel_x
    lead_y += vel_y

    game_display.fill(white)
    #pygame.draw.rect(game_display, black, [400,300, 10, 100])
    #pygame.draw.rect(game_display, red, [400,300, 10, 10])
    game_display.fill(red, rect= [lead_x,lead_y,10,10])
    pygame.display.update()

    clock.tick(30)

pygame.quit()

