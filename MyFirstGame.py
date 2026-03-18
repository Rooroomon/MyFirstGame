import pygame
import sys
import random

MoveSpeed = 5
WHITE = (255, 255, 255)
circleColor = (0, 0, 255)
circlePos_x, circlePos_y = 400, 300
screenSize = (800, 600) #벽 판정 자동 설정

pygame.init()
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("My First Pygame")


clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            circleColor = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LSHIFT]:
        MoveSpeed = 10
    else:
        MoveSpeed = 5
        
    if keys[pygame.K_LEFT] and circlePos_x > 50:
        circlePos_x -= MoveSpeed
    if keys[pygame.K_RIGHT] and circlePos_x < screenSize[0] - 50:
        circlePos_x += MoveSpeed
    if keys[pygame.K_UP] and circlePos_y > 50:
        circlePos_y -= MoveSpeed
    if keys[pygame.K_DOWN] and circlePos_y < screenSize[1] - 50:
        circlePos_y += MoveSpeed
            
    screen.fill(WHITE)
    pygame.draw.circle(screen, circleColor, (circlePos_x, circlePos_y), 50)
    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
sys.exit()